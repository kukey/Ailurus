#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Ailurus - make Linux easier to use
#
# Copyright (C) 2007-2010, Trusted Digital Technology Laboratory, Shanghai Jiao Tong University, China.
# Copyright (C) 2009-2010, Ailurus Developers Team
#
# Ailurus is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ailurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ailurus; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

from __future__ import with_statement
import sys, os
from lib import *

#class Open_Repogen_Website:
#    __doc__ = _('* Find more repositories on http://repogen.simplylinux.ch')
#    detail = _('This item is an auxiliary item. It will not install anything. It will open web-page http://repogen.simplylinux.ch/\n'
#               'http://repogen.simplylinux.ch/ has collected a lot of useful third party repositories.')
#    category = 'repository'
#    def installed(self): 
#        return False
#    def install(self):
#        open_web_page('http://repogen.simplylinux.ch/')
#    def remove(self):
#        pass

class _repo(I):
    this_is_a_repository = True
    category = 'repository'
    fresh_cache = False

    @classmethod
    def refresh_cache(cls):
        if not _repo.fresh_cache:
            _repo.source_settings = APTSource.get_source_contents()
            _repo.fresh_cache = True
    @classmethod
    def exists_in_source(cls, seed):
        assert isinstance(seed, str)
        seed = seed.split('#')[0].strip()
        _repo.refresh_cache()
        for contents in _repo.source_settings.values():
            for line in contents:
                if seed in line.split('#')[0]: return True
        return False
    @classmethod
    def add_to_source(cls, file_name, seed):
        assert isinstance(file_name, str)
        assert isinstance(seed, str)
        assert seed[-1]!='\n'
        _repo.refresh_cache()
        if not file_name in _repo.source_settings:
            _repo.source_settings[file_name] = []
        _repo.source_settings[file_name].append(seed+'\n')
    @classmethod
    def remove_from_source(cls, seed):
        assert isinstance(seed, str)
        seed = seed.split('#')[0].strip()
        _repo.refresh_cache()
        for contents in _repo.source_settings.values():
            for i in reversed(range(len(contents))):
                line = contents[i]
                if seed in line.split('#')[0]:
                    del contents[i]
    @classmethod
    def save_source(cls):
        for file_path, contents in _repo.source_settings.items():
            if contents == []:
                run_as_root("rm -f '%s' "%file_path)
                continue
            with TempOwn(file_path) as o:
                f = open(file_path, 'w')
                f.writelines(contents)
                f.close()
    def __init__(self):
        # check
        assert isinstance(self.desc, (str,unicode) )
        assert isinstance(self.web_page, str)
        
        assert isinstance(self.apt_file, str)
        assert isinstance(self.apt_conf, list)
        for i,a in enumerate(self.apt_conf):
            is_string_not_empty(a)
            if a.endswith('\n'): raise ValueError(a)
            if '$' in a: #variable substitution
                assert '$version' in a
                self.apt_conf[i] = a.replace('$version', Config.get_Ubuntu_version() )
        assert isinstance(self.apt_content, str)
        
        if hasattr(self, 'key_url'):
            assert isinstance(self.key_url, str)
            if self.key_url:
                assert ( self.key_url.startswith('ftp://') or
                         self.key_url.startswith('http://') or
                         self.key_url.startswith('https://') )
        
        assert isinstance(self.key_id, str)
        
        # create detail
        import StringIO
        msg = StringIO.StringIO()
        if self.desc:
            print >>msg, self.desc, '\n'
        if self.apt_content:
            print >>msg, _('<i>Install packages by:</i>'), '<b>sudo apt-get install', self.apt_content, '</b>'
        print >>msg, _('<i>Web page:</i>'), self.web_page
        print >>msg, _('<i>Source setting:</i>'),
        for a in self.apt_conf:
            print >>msg, a
        self.__class__.detail = msg.getvalue()
    def installed(self):
        _repo.refresh_cache()
        for seed in self.apt_conf:
            if not self.exists_in_source(seed):
                return False
        return True
    def install(self):
        # change souce
        _repo.refresh_cache()
        for seed in self.apt_conf:
            self.add_to_source(self.apt_file, seed)
        self.save_source()
        _repo.fresh_cache = False
        # add key
        if hasattr(self, 'key_url'):
            if self.key_url: #if has key
                download(self.key_url, '/tmp/key.gpg')
                run_as_root('apt-key add /tmp/key.gpg')
        else:
            raise NotImplementedError
    def remove(self):
        # change source
        _repo.refresh_cache()
        for seed in self.apt_conf:
            self.remove_from_source(seed)
        self.save_source()
        _repo.fresh_cache = False
        # remove key
        if self.key_id:
            run_as_root('apt-key del '+self.key_id, ignore_error=True)

def get_owner_and_name(ppa):
    assert not ppa.startswith("ppa:")
    ppa_owner = ppa.split("/")[0]
    try:
        ppa_name = ppa.split("/")[1]
    except IndexError, e:
        ppa_name = "ppa"
    return (ppa_owner, ppa_name)

def get_deb_line(ppa_owner, ppa_name, distro_codename):
    return "deb http://ppa.launchpad.net/%s/%s/ubuntu %s main" % (
        ppa_owner, ppa_name, distro_codename)

def get_repos_file_name(ppa_owner, ppa_name, distro_codename):
    return "%s-%s-%s.list" % (ppa_owner, ppa_name, distro_codename)

def get_signing_key(ppa_owner, ppa_name):
    import urllib2, re
    lp_url = ('https://launchpad.net/api/beta/~%s/+archive/%s' % (
        ppa_owner, ppa_name))
    try:
        req = urllib2.Request(lp_url)
        req.add_header("Accept","application/json")
        lp_page = urllib2.urlopen(req).read()
        signing_key_fingerprint = re.findall(
            '\"signing_key_fingerprint\": \"(\w*)\"', lp_page)[0]
        return signing_key_fingerprint
    except URLError, e:
        import traceback, sys
        traceback.print_exc(file = sys.stderr)
        return None

def add_signing_key(signing_key_fingerprint):
    run_as_root_in_terminal("apt-key adv --keyserver keyserver.ubuntu.com --recv " + signing_key_fingerprint)

def del_signing_key(signing_key_fingerprint):
    run_as_root_in_terminal("apt-key del " + signing_key_fingerprint)

class _launchpad(I):
    this_is_a_repository = True
    category = 'repository'
    def __init__(self):
        assert isinstance(self.ppa, str)
        if hasattr(self, 'content'): assert isinstance(self.content, str)
        if hasattr(self, 'desc'): assert isinstance(self.desc, (unicode, str))
        self.ppa_owner, self.ppa_name = get_owner_and_name(self.ppa)
        self.deb_config = get_deb_line(self.ppa_owner, self.ppa_name, Config.get_Ubuntu_version())
        self.repos_file_name = '/etc/apt/sources.list.d/' + get_repos_file_name(self.ppa_owner, self.ppa_name, Config.get_Ubuntu_version())

        import StringIO
        msg = StringIO.StringIO()
        if hasattr(self, 'desc'): print >>msg, self.desc
        if hasattr(self, 'content'):
            print >>msg, _('<i>Install packages by:</i>'), '<b>sudo apt-get install', self.content, '</b>'
        print >>msg, _('<i>Web page:</i>'), 'http://launchpad.net/~%s/+archive/%s' % (self.ppa_owner, self.ppa_name)
        print >>msg, _('<i>Source setting:</i>'), self.deb_config
        self.__class__.detail = msg.getvalue()
    def install(self):
        _repo.refresh_cache()
        _repo.add_to_source(self.repos_file_name, self.deb_config)
        _repo.save_source()
        _repo.fresh_cache = False
        signing_key = get_signing_key(self.ppa_owner, self.ppa_name)
        if signing_key: add_signing_key(signing_key)
    def installed(self):
        _repo.refresh_cache()
        return _repo.exists_in_source(self.deb_config)
    def remove(self):
        _repo.refresh_cache()
        _repo.remove_from_source(self.deb_config)
        _repo.save_source()
        _repo.fresh_cache = False
        signing_key = get_signing_key(self.ppa_owner, self.ppa_name)
        if signing_key: del_signing_key(signing_key)

# Hide it in Lucid. Since Firefox is 3.6.3 in Lucid.
class Repo_Firefox_3_6(_launchpad):
    __doc__ = _('Firefox 3.6 (stable)')
    license = TRI_LICENSE(MPL, GPL, LGPL)
    ppa = 'mozillateam/firefox-stable'
    content = 'firefox'
    def support(self):
        return Config.get_Ubuntu_version() in ['hardy', 'intrepid', 'jaunty', 'karmic']

class Repo_PlayOnLinux(_repo):
    __doc__ = _('PlayOnLinux (stable)')
    license = LGPL
    def __init__(self):
        self.desc = _('PlayOnLinux is a front-end for wine. '
            'It helps to install Windows Games and softwares on Linux.')
        self.apt_content = 'playonlinux'
        self.web_page = 'http://www.playonlinux.com/en/download.html'
        self.apt_file = '/etc/apt/sources.list.d/playonlinux.list'
        self.apt_conf = [ 'deb http://deb.playonlinux.com/ $version main' ]
        self.key_url = '' #no key
        self.key_id = '' #no key
        _repo.__init__(self)

class Repo_WINE(_repo):
    __doc__ = _('WINE (beta version)')
    license = LGPL + ' http://wiki.winehq.org/Licensing'
    def __init__(self):
        self.desc = _('This repository contains the latest version of Wine. '
            'Wine is for running Windows applications on Linux.')
        self.apt_content = 'wine wine-gecko'
        self.web_page = 'https://launchpad.net/~ubuntu-wine/+archive/ppa'
        self.apt_file = '/etc/apt/sources.list.d/winehq.list'
        self.apt_conf = [ 'deb http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu $version main' ]
        self.key_url = 'http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x5A9A06AEF9CB8DB0'
        self.key_id = 'F9CB8DB0'
        _repo.__init__(self)

class Repo_Ailurus(_launchpad):
    __doc__ = _('Ailurus (stable)')
    license = GPL
    ppa = 'ailurus'
    content = 'ailurus'

class Repo_AWN_Development(_launchpad):
    __doc__ = _('AWN (beta version)')
    license = GPL
    desc = _('AWN is a MacOS X like panel for GNOME. '
            'This repository provides the latest version of AWN.')
    content = 'avant-window-navigator-trunk'
    ppa = 'awn-testing'

class Repo_Blueman(_launchpad):
    __doc__ = _('Blueman (stable)')
    license = GPL
    desc = _('Blueman is a graphical blue-tooth manager.')
    content = 'blueman'
    ppa = 'blueman'

class Repo_Christine(_launchpad):
    __doc__ = _('Christine (stable)')
    license = GPL
    desc = _('Christine is a small media player.')
    content = 'christine'
    ppa = 'markuz'

class Repo_Chromium_Daily(_launchpad):
    __doc__ = _('Chromium (beta version)')
    license = BSD
    desc = _('Chromium is the open source version of Google Chrome.')
    content = 'chromium-browser'
    ppa = 'chromium-daily'

class Repo_GTG(_launchpad):
    __doc__ = _('Getting things GNOME (stable)')
    license = GPL
    desc = _('"Getting things GNOME" is a simple, powerful and flexible organization tool.')
    content = 'gtg'
    ppa = 'gtg'

class Repo_GNOMEColors(_launchpad):
    __doc__ = _('GNOME colors (stable)')
    license = GPL
    desc = _('This repository contains some themes.')
    content = 'gnome-colors'
    ppa = 'gnome-colors-packagers'

class Repo_GlobalMenu(_launchpad):
    __doc__ = _('GNOME Global Menu (stable)')
    license = GPL
    desc = _('GNOME Global Menu is the globally-shared menu bar of all applications.')
    content = 'gnome-globalmenu'
    ppa = 'globalmenu-team'

class Repo_Medibuntu(_repo):
    __doc__ = _('Medibuntu (stable)')
    license = GPL
    def __init__(self):
        self.desc = _('This is a repository providing packages which cannot be included into the Ubuntu distribution for legal reasons. '
            'There are many packages in this repository. The list of packages is in http://packages.medibuntu.org/')
        self.apt_content = ''
        self.web_page = 'http://packages.medibuntu.org/'
        self.apt_file = '/etc/apt/sources.list.d/medibuntu.list'
        self.apt_conf = [ 'deb http://packages.medibuntu.org/ $version free non-free' ]
        self.key_url = 'http://packages.medibuntu.org/medibuntu-key.gpg'
        self.key_id = '0C5A2783'
        _repo.__init__(self)

class Repo_Moovida(_launchpad):
    __doc__ = _('Moovida (stable)')
    license = GPL
    desc = _('Moovida is a cross platform media player.')
    content = 'moovida'
    ppa = 'moovida-packagers'

class Repo_Shutter(_launchpad):
    __doc__ = _('Shutter (stable)')
    license = GPL
    desc = _('Shutter is a powerful screenshot program.')
    content = 'shutter'
    ppa = 'shutter'
    
#class Repo_Synapse(_repo):
#    __doc__ = _('Synapse (stable)')
#    license = GPL
#    def __init__(self):
#        self.desc = _('Synapse is an instant messager.')
#        self.apt_content = 'synapse'
#        self.web_page = 'http://synapse.im/download/'
#        self.apt_file = '/etc/apt/sources.list.d/synapse.list'
#        self.apt_conf = [ 'deb http://ppa.launchpad.net/firerabbit/ppa/ubuntu $version main' ]
#        self.key_url = 'http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x83419668F12469157BCD4BE904508D5C1654E635'
#        self.key_id = '1654E635'
#        _repo.__init__(self)

class Repo_X_Server_Updates(_launchpad):
    __doc__ = _('X server updates (stable)')
    license = GPL
    desc = _('This repository provides latest versions of X.org drivers, libraries.')
    content = ( 'fglrx-installer xfree86-driver-synaptics xserver-xorg-input-vmmouse xserver-xorg-video-ati ' +
                             'xserver-xorg-video-intel xserver-xorg-video-nv' )
    ppa = 'ubuntu-x-swat/x-updates'
        
class Repo_WebkitGTK(_launchpad):
    __doc__ = _('WebkitGTK (stable)')
    license = LGPL
    desc = _('WebkitGTK is the port of Webkit to the GTK+ platform.')
    content = 'webkit pywebkitgtk'
    ppa = 'webkit-team'
    
class Repo_XBMC(_launchpad):
    __doc__ = _('XBMC (stable)')
    license = GPL
    desc = _('XBMC is an open source software media player and entertainment hub for digital media.')
    content = 'xbmc'
    ppa = 'team-xbmc'

class Repo_IBus_Jaunty(_launchpad):
    __doc__ = _('IBus (stable)')
    license = GPL
    content = 'ibus ibus-table ibus-pinyin'
    ppa = 'ibus-dev/ibus-1.2-jaunty'
    def support(self):
        return Config.get_Ubuntu_version() == 'jaunty'

class Repo_IBus_Intrepid(_launchpad):
    __doc__ = _('IBus (stable)')
    license = GPL
    content = 'ibus ibus-table ibus-pinyin'
    ppa = 'ibus-dev/ibus-1.2-intrepid'
    def support(self):
        return Config.get_Ubuntu_version() == 'intrepid'

class Repo_IBus_Karmic(_launchpad):
    __doc__ = _('IBus (stable)')
    license = GPL
    content = 'ibus ibus-table ibus-pinyin'
    ppa = 'ibus-dev/ibus-1.2-karmic'
    def support(self):
        return Config.get_Ubuntu_version() == 'karmic'

class Repo_Canonical_Partner(_repo):
    __doc__ = _('Partners of Canonical')
    def __init__(self):
        self.desc = _('This repository provides many packages from partners of Canonical.')
        self.apt_content = 'acroread uex symphony accountz-baz'
        self.web_page = 'http://archive.canonical.com/ubuntu/dists/'
        self.apt_file = '/etc/apt/sources.list.d/partners-of-canonical.list'
        self.apt_conf = [ 'deb http://archive.canonical.com/ubuntu $version partner ' ]
        self.key_url = ''
        self.key_id = ''
        _repo.__init__(self)

class Repo_RSSOwl(_repo):
    __doc__ = _('RSSOwl (stable)')
    license = EPL
    def __init__(self):
        self.desc = _('RSSOwl is an RSS reader.')
        self.apt_content = 'rssowl'
        self.web_page = 'http://packages.rssowl.org/README'
        self.apt_file = '/etc/apt/sources.list.d/rssowl.list'
        self.apt_conf = [ 'deb http://packages.rssowl.org/ubuntu $version main' ]
        self.key_url = 'http://packages.rssowl.org/project/rene.moser.pubkey'
        self.key_id = 'E53168C7'
        _repo.__init__(self)

class Repo_Gmchess(_launchpad):
    __doc__ = _('Gmchess (stable)')
    license = GPL
    Chinese = True
    desc = _('This is a Chinese chess game.')
    content = 'gmchess'
    ppa = 'gmchess'

class Repo_Exaile(_launchpad):
    __doc__ = _('Exaile (beta version)')
    license = GPL
    desc = _('A music manager and player for GTK+ written in Python.')
    content = 'exaile'
    ppa = 'exaile-devel'

class Repo_Audacious(_launchpad):
    __doc__ = _('Audacious (beta version)')
    license = GPL
    desc = _('An advanced audio player.It focused on audio quality and supporting a wide range of audio codecs.')
    content = 'audacious audacious-plugins'
    ppa = 'dupondje'
        
class Repo_Tor(_repo):
    __doc__ = _('Tor (stable)')
    license = BSD
    def __init__(self):
        self.desc = _('An open network that helps you defend against a form of network surveillance that threatens personal freedom and privacy, '
        'confidential business activities and relationships, and state security known as traffic analysis.')
        self.apt_content = 'tor privoxy vidalia'
        self.web_page = 'http://deb.torproject.org/'
        self.apt_file = '/etc/apt/sources.list.d/tor.list'
        self.apt_conf = [ 'deb http://deb.torproject.org/torproject.org $version main' ]
        self.key_url = ''
        self.key_id = '886DDD89'
        _repo.__init__(self)

class Repo_RedNoteBook(_repo):
    __doc__ = _('RedNoteBook (stable)')
    license = GPL
    def __init__(self):
        self.desc = _('This is a desktop diary application.')
        self.apt_content = 'rednotebook'
        self.web_page = 'http://robin.powdarrmonkey.net/ubuntu/'
        self.apt_file = '/etc/apt/sources.list.d/rednotebook.list'
        self.apt_conf = [ 'deb http://robin.powdarrmonkey.net/ubuntu $version/' ]
        self.key_url = 'http://robin.powdarrmonkey.net/ubuntu/repository.key'
        self.key_id = 'FF95D333'
        _repo.__init__(self)
    def support(self):
        return Config.get_Ubuntu_version() != 'lucid'

class Repo_Pidgin_Develop(_launchpad):
    __doc__ = _('Pidgin (beta version)')
    license = GPL
    desc = _('A free chat client used by millions. Connect easily to MSN, Google Talk, Yahoo, AIM and other chat networks all at once.')
    content = 'pidgin'
    ppa = 'pidgin-developers'

class Repo_Songbird(_launchpad):
    __doc__ = _('Songbird (beta version)')
    license = GPL
    desc = _('Music player which integrates with online content via plugins. Site contains project news, download, add-ons directory, help, and how to contribute.')
    content = 'songbird'
    ppa = 'songbird-daily'

class Repo_OSD_Lyrics(_launchpad):
    __doc__ = _('OSD-Lyrics (stable)')
    license = GPL
    desc = _('It displays lyrics. It supports many media players.')
    content = 'osdlyrics'
    ppa = 'osd-lyrics'

class Repo_Mplayer_VOD(_launchpad):
    __doc__ = _('Mplayer-VOD (stable)')
    license = GPL
    desc = _('A movie player for Linux. Supports reading from network, dvd, vcd, file, pipes, and v4l.')
    content = 'mplayer'
    ppa = 'homer-xing/mplayer-vod'
    def support(self):
        return False

class Repo_Acire(_launchpad):
    __doc__ = _('Acire (stable)')
    license = GPL
    content = 'acire'
    ppa = 'acire-team/acire-releases'
