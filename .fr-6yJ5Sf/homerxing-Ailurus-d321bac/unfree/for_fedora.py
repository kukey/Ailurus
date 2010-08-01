#coding: utf8
#
# Ailurus - a simple application installer and GNOME tweaker
#
# Copyright (C) 2009-2010, Ailurus developers and Ailurus contributors
# Copyright (C) 2007-2010, Trusted Digital Technology Laboratory, Shanghai Jiao Tong University, China.
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
# don't change sys.path
from lib import *
from libapp import *
assert FEDORA

class urls:
    realplayer = 'http://software-dl.real.com/079f1e1c74ca25924402/unix/RealPlayer11GOLD.rpm'
    eset_antivirus_32 = 'http://download.eset.com/special/eav_linux/ueav.i386.linux'
    eset_antivirus_64 = 'http://download.eset.com/special/eav_linux/ueav.x86_64.linux'
    google_earch = 'http://dl.google.com/earth/client/current/GoogleEarthLinux.bin'
    google_chrome_32 = 'http://dl.google.com/linux/direct/google-chrome-stable_current_i386.rpm'
    google_chrome_64 = 'http://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm'
    alipay = 'http://blog.alipay.com/wp-content/2008/10/aliedit.tar.gz'
    amenace = 'http://www.viewizard.com/download/amenace12.tar.bz2'
    hittex = 'http://plutothesis.googlecode.com/files/PlutoThesis_UTF8_1.9.2.20090424.zip'
    eioffice = 'http://evermoresw.com.cn/EverMore/EIOPersonal/EIOffice_Personal_Lin.tar.gz'
    eioffice_clipart = 'http://evermoresw.com.cn/EverMore/EIOPersonal/Resource/EIOffice_Clipart.tar.gz'
    eioffice_help = 'http://evermoresw.com.cn/EverMore/EIOPersonal/Resource/EIOffice_HelpFiles.tar.gz'
    eioffice_scienceeditor = 'http://evermoresw.com.cn/EverMore/EIOPersonal/Resource/EIOffice_ScienceEditorImages.tar.gz'
    eioffice_templates = 'http://evermoresw.com.cn/EverMore/EIOPersonal/Resource/EIOffice_Templates.tar.gz'
    adobe_repos_rpm = 'http://linuxdownload.adobe.com/linux/i386/adobe-release-i386-1.0-1.noarch.rpm'
    rpmfusion_repos_free = 'http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm'
    rpmfusion_repos_nonfree = 'http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm'
    nvidia_32 = 'ftp://download.nvidia.com/XFree86/Linux-x86/195.36.24/NVIDIA-Linux-x86-195.36.24-pkg1.run'
    nvidia_64 = 'ftp://download.nvidia.com/XFree86/Linux-x86_64/195.36.24/NVIDIA-Linux-x86_64-195.36.24-pkg2.run'
    picasa_32 = 'http://dl.google.com/linux/rpm/testing/i386/picasa-3.0-current.i386.rpm'
    adobeair_32 = 'http://airdownload.adobe.com/air/lin/download/latest/adobeair.i386.rpm'

class _repo(I):
    this_is_a_repository = True
    category = 'repository'
    @classmethod
    def exist(cls, path):
        import os
        return os.path.exists(path)
    @classmethod
    def enabled(cls, path):
        with open(path) as f:
            lines = f.readlines()
        return 'enabled=1\n' in lines
    @classmethod
    def enable(cls, path, only_enable_first_appearance = False):
        with open(path) as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if lines[i].startswith('enabled='):
                lines[i] = 'enabled=1\n'
                if only_enable_first_appearance: break
        with TempOwn(path):
            with open(path, 'w') as f:
                f.writelines(lines)
    @classmethod
    def disable(cls, path):
        with open(path) as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if lines[i].startswith('enabled='):
                lines[i] = 'enabled=0\n'
        with TempOwn(path):
            with open(path, 'w') as f:
                f.writelines(lines)

class Repo_Adobe(I):
    'Adobe'
    detail = _('This repository provides flash-plugin and Adobe Reader.')
    category = 'repository'
    def __init__(self):
        self.path = '/etc/yum.repos.d/adobe-linux-i386.repo'
    def installed(self):
        return _repo.exist(self.path) and _repo.enabled(self.path)
    def install(self):
        if _repo.exist(self.path):
            _repo.enable(self.path)
        else:
            file = '/tmp/adobe-release-i386-1.0-1.noarch.rpm'
            wget(urls.adobe_repos_rpm, file)
            RPM.install_local(file)
    def remove(self):
        if _repo.exist(self.path):
            _repo.disable(self.path)
    def visible(self):
        return is32()

class Repo_Skype(I):
    'Skype'
    category = 'repository'
    def __init__(self):
        self.path = '/etc/yum.repos.d/skype.repo'
    def installed(self):
        return _repo.exist(self.path) and _repo.enabled(self.path)
    def install(self):
        if _repo.exist(self.path):
            _repo.enable(self.path)
        else:
            with TempOwn(self.path):
                with open(self.path, 'w') as f:
                    f.write('[skype]\n'
                        'name=Skype Repository\n'
                        'baseurl=http://download.skype.com/linux/repos/fedora/updates/i586/\n'
                        'enabled=1\n'
                        'gpgchek=0\n')
    def remove(self):
        if _repo.exist(self.path):
            _repo.disable(self.path)
    def visible(self):
        return is32()

class Repo_RPMFusion_Free(I):
    __doc__ = _('RPM Fusion (Free)')
    category = 'repository'
    detail = _('RPM Fusion provides software that not in the standard repositories.')
    def __init__(self):
        self.paths = ['/etc/yum.repos.d/rpmfusion-free.repo', '/etc/yum.repos.d/rpmfusion-free-updates.repo']
    def installed(self):
        for path in self.paths:
           value = _repo.exist(path) and _repo.enabled(path)
           if not value: return False
        return True
    def install(self):
        all_exists = True
        for path in self.paths:
            if not _repo.exist(path):
                all_exists = False
        
        if all_exists:
            for path in self.paths:
                _repo.enable(path, only_enable_first_appearance = True)
        else:
            file = '/tmp/rpmfusion-free-release-stable.noarch.rpm'
            wget(urls.rpmfusion_repos_free, file)
            RPM.install_local(file)
    def remove(self):
        for path in self.paths:
            if _repo.exist(path): _repo.disable(path)

class Repo_RPMFusion_NonFree(I):
    __doc__ = _('RPM Fusion (Non-Free)')
    category = 'repository'
    detail = _('RPM Fusion provides software that not in the standard repositories.')
    def __init__(self):
        self.paths = ['/etc/yum.repos.d/rpmfusion-nonfree.repo', '/etc/yum.repos.d/rpmfusion-nonfree-updates.repo']
    def installed(self):
        for path in self.paths:
           value = _repo.exist(path) and _repo.enabled(path)
           if not value: return False
        return True
    def install(self):
        all_exists = True
        for path in self.paths:
            if not _repo.exist(path):
                all_exists = False
        
        if all_exists:
            for path in self.paths:
                _repo.enable(path, only_enable_first_appearance = True)
        else:
            file = '/tmp/rpmfusion-nonfree-release-stable.noarch.rpm'
            wget(urls.rpmfusion_repos_nonfree, file)
            RPM.install_local(file)
    def remove(self):
        for path in self.paths:
            if _repo.exist(path): _repo.disable(path)

class Repo_Google(I):
    'Google'
    category = 'repository'
    detail = _('This repository provides Picasa and Google Desktop.')
    def __init__(self):
        self.path = '/etc/yum.repos.d/google.repo'
    def installed(self):
        return _repo.exist(self.path) and _repo.enabled(self.path)
    def install(self):
        if _repo.exist(self.path): _repo.enable(self.path, False)
        else:
            with TempOwn(self.path):
                with open(self.path, 'w') as f:
                    f.write('[Google]\n'
                        'name=Google - i386\n'
                        'baseurl=http://dl.google.com/linux/rpm/stable/i386\n'
                        'enabled=1\n'
                        'gpgcheck=1\n'
                        '\n'
                        '[GoogleTesting]\n'
                        'name=Google Testing - i386\n'
                        'baseurl=http://dl.google.com/linux/rpm/testing/i386\n'
                        'enabled=1\n'
                        'gpgcheck=1\n')
            wget('https://dl-ssl.google.com/linux/linux_signing_key.pub', '/tmp/key.gpg')
            RPM.import_key('/tmp/key.gpg')
    def remove(self):
        if _repo.exist(self.path): _repo.disable(self.path)

class Repo_Google_Chrome(I):
    'Google Chrome'
    category = 'repository'
    detail = _('This repository provides Google Chrome.')
    def __init__(self):
        self.path = '/etc/yum.repos.d/google-chrome.repo'
    def installed(self):
        return _repo.exist(self.path) and _repo.enabled(self.path)
    def install(self):
        if _repo.exist(self.path): _repo.enable(self.path)
        else:
            with TempOwn(self.path):
                if is32(): arch = 'i386'
                else: arch = 'x86_64'
                
                with open(self.path, 'w') as f:
                    f.write('[google-chrome]\n'
                        'name=google-chrome\n'
                        'baseurl=http://dl.google.com/linux/rpm/stable/%s\n'
                        'enabled=1\n'
                        'gpgcheck=1\n'
                        'gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub\n' % arch
                        )
            wget('https://dl-ssl.google.com/linux/linux_signing_key.pub', '/tmp/key.gpg')
            RPM.import_key('/tmp/key.gpg')
    def remove(self):
        if _repo.exist(self.path): _repo.disable(self.path)

class Repo_VirtualBox(I):
    'VirtualBox'
    category = 'repository'
    detail = _('This repository provides VirtualBox.')
    download_url = 'http://www.virtualbox.org/wiki/Linux_Downloads'
    def __init__(self):
        self.path = '/etc/yum.repos.d/virtualbox.repo'
    def installed(self):
        return _repo.exist(self.path) and _repo.enabled(self.path)
    def install(self):
        if _repo.exist(self.path): _repo.enable(self.path)
        else:
            with TempOwn(self.path):
                with open(self.path, 'w') as f:
                    f.write('[virtualbox]\n'
                        'name=Fedora $releasever - $basearch - VirtualBox\n'
                        'baseurl=http://download.virtualbox.org/virtualbox/rpm/fedora/$releasever/$basearch\n'
                        'enabled=1\n'
                        'gpgcheck=1\n'
                        'gpgkey=http://download.virtualbox.org/virtualbox/debian/sun_vbox.asc\n'
                        )
            wget('http://download.virtualbox.org/virtualbox/debian/sun_vbox.asc', '/tmp/key.gpg')
            RPM.import_key('/tmp/key.gpg')
    def remove(self):
        if _repo.exist(self.path): _repo.disable(self.path)

class GStreamer_Codecs (_rpm_install) :
    __doc__ = _('Multi-media codec')
    category = 'others'
    depends = Repo_RPMFusion_Free
    pkgs = ('gstreamer gstreamer-plugins-bad gstreamer-plugins-bad-extras gstreamer-plugins-base'
            'gstreamer-plugins-good gstreamer-plugins-ugly')

class Adobe_Flash_Player(_rpm_install):
    __doc__ = _('Adobe Flash plugin for web browser')
    category = 'flash'
    depends = Repo_Adobe
    pkgs = 'flash-plugin'

class AdobeReader(_rpm_install):
    __doc__ = _('Adobe PDF Reader')
    download_url = 'http://get.adobe.com/reader/'
    category = 'business'
    depends = Repo_Adobe
    def __init__(self):
        package_dict = {
                   'zh_HK':'AdobeReader_cht',
                   'zh_TW':'AdobeReader_cht',
                   'zh_CN':'AdobeReader_chs',
                   'de':'AdobeReader_deu',
                   'en':'AdobeReader_enu',
                   'es':'AdobeReader_esp',
                   'it':'AdobeReader_ita',
                   'nl':'AdobeReader_nld',
                   'pt':'AdobeReader_ptb',
                   }
        value = Config.get_locale()
        if not value.startswith('zh'): value = value.split('_')[0]
        try:
            self.pkgs = package_dict[value]
        except KeyError:
            self.pkgs = package_dict['en']
    def visible(self):
        return is32()

# Do not install Realplayer. It cannot be removed by yum :(

class GoogleChrome(I):
    __doc__ = _('Google Chrome browser')
    detail = _(
        'This is the web browser from Google. \n'
        'You can change themes by opening web-page https://tools.google.com/chrome/intl/pt/themes/index.html in Google Chrome.')
    category = 'browser'
    def install(self):
        if is32():
            f = R(urls.google_chrome_32).download()
        else:
            f = R(urls.google_chrome_64).download()
        RPM.install_local(f)
    def installed(self):
        return RPM.installed('google-chrome-stable')
    def remove(self):
        return RPM.remove('google-chrome-stable')
    def get_reason(self, f):
        if RPM.installed('google-chrome-unstable'):
            print >>f, _('You have installed "google-chrome-unstable".'),
        if RPM.installed('google-chrome-beta'):
            print >>f, _('You have installed "google-chrome-beta".'),

class GoogleEarth(I):
    __doc__ = _('Google Earth')
    detail = _('Please install it in /opt/google-earth. Otherwise it cannot be detected.')
    category = 'others'
    def install(self):
        f = R(urls.googleearch).download()
        os.system('chmod a+x ' + f)
        run_as_root_in_terminal(f)
    def installed(self):
        return os.path.exists('/opt/google-earth')
    def remove(self):
        run_as_root_in_terminal('/opt/google-earth/uninstall')
           
class VirtualBox(_rpm_install):
    'SUN VirtualBox 3'
    detail = _('It is the only professional virtual machine which is freely available '
       'under the terms of GPL. '
       'Official site: http://www.virtualbox.org/wiki/Downloads')
    category = 'simulator'
    depends = Repo_VirtualBox
    pkgs = 'virtualbox'

class Skype(_rpm_install):
    'Skype'
    detail = _('With Skype you can make free calls over the Internet to other people. ')
    category = 'chat'
    depends = Repo_Skype
    pkgs = 'skype'
    def visible(self):
        return is32()

class Repo_Chromium(I):
    'Chromium'
    detail = _('Open source web browser')
    def __init__(self):
        self.path = '/etc/yum.repos.d/chromium.repo'
    def installed(self):
        return _repo.exist(self.path) and _repo.enabled(self.path)
    def install(self):
        if _repo.exist(self.path):
            _repo.enable(self.path)
        else:
            with TempOwn(self.path):
                with open(self.path, 'w') as f:
                    f.write('[chromium]\n'
                            'name=Chromium Test Packages\n'
                            'baseurl=http://spot.fedorapeople.org/chromium/F$releasever/\n'
                            'enabled=1\n'
                            'gpgcheck=0\n')
    def remove(self):
        if _repo.exist(self.path):
            _repo.disable(self.path)

class ESETNOD32(I):
    __doc__ = 'ESET NOD32'
    detail = _('Anti virus and anti spyware')
    download_url = 'http://beta.eset.com/linux'
    category = 'antivirus'
    def install(self):
        if is32():
            f = R(urls.eset_antivirus_32).download()
        else:
            f = R(urls.eset_antivirus_64).download()
        run('chmod +x ' + f)
        run_as_root(f)
        if not is32():
            # Fix bug because /usr/lib/libesets_pac.so cannot run on x86_64
            with TempOwn('/etc/ld.so.preload'):
                with open('/etc/ld.so.preload') as f:
                    content = f.read()
                with open('/etc/ld.so.preload', 'w') as f:
                    for item in content.split():
                        if 'libesets_pac.so' not in item:
                            print >>f, item, 
    def installed(self):
        return os.path.exists('/opt/eset/esets/bin/esets_gil')
    def remove(self):
        run_as_root('/opt/eset/esets/bin/esets_gil')

class AdobeAIR(I):
    __doc__ = 'Adobe AIR'
    detail = _('Use HTML, JavaScript and Flash to build desktop applications')
    download_url = 'http://get.adobe.com/air/'
    category = 'ide'
    def install(self):
        f = R(urls.adobeair_32).download()
        RPM.install_local(f)
    def installed(self):
        return RPM.installed('adobeair')
    def remove(self):
        RPM.remove('adobeair')
    def visible(self):
        return is32()

class Picasa(I):
    __doc__ = 'Picasa'
    detail = _('An image organizer and image viewer, plus photo-sharing function')
    download_url = urls.picasa_32
    category = 'photo'
    def install(self):
        f = R(urls.picasa_32).download()
        RPM.install_local(f)
    def installed(self):
        return RPM.installed('picasa')
    def remove(self):
        RPM.remove('picasa')
    def visible(self):
        return is32()