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
from libapp import *
from third_party_repos import *

class PBC(I):
    __doc__ = _('PBC (Pairing-Based Cryptography) library')
    detail = ( _('Install Pairing-Based Cryptography library, powered by Stanford University.\n') +
               _('Official site: <span color="blue"><u>http://crypto.stanford.edu/pbc/</u></span> .') )
    category = 'dev'
    license = GPL
    def install(self):
        if get_arch()==32:
            fdev=R(
['http://voltar.org/pbcfiles/libpbc-dev_0.5.4-1_i386.deb'],
182700, 'f2493c4c8ad0515babf28b1c5241583d993ad169'
).download()
        else:
            fdev=R(
['http://voltar.org/pbcfiles/libpbc-dev_0.5.4-1_amd64.deb'],
206752, '6ebfb58ddb53f8c63c475f871f843e2e5c2ec676'
).download()

        if get_arch()==32:
            f=R(
['http://voltar.org/pbcfiles/libpbc0_0.5.4-1_i386.deb'],
87122, '4424b14adee23683eff979c4efe33f493f2d2a55'
).download()
        else:
            f=R(
['http://voltar.org/pbcfiles/libpbc0_0.5.4-1_amd64.deb'],
96028, 'db19a612666605a18db319976b92c492e5371b91'
).download()

        DPKG.install_deb(f, fdev)
        
    def installed(self):
        return APT.installed('libpbc0') and APT.installed('libpbc-dev')
    
    def remove(self):
        APT.remove('libpbc0', 'libpbc-dev')
   
class Build_Essential(_apt_install):
    'Build-essential'
    detail = _('By installing build-essential, you will get g++, make, gdb and libc.')
    category = 'dev'
    license = GPL
    pkgs = 'build-essential'

class POSIX_ManPages(_apt_install):
    __doc__ = _('POSIX library manual pages')
    detail = _('Install manual pages about Linux system calls, library calls, and POSIX libraries.')
    category = 'dev'
    license = GPL
    pkgs = 'manpages-dev manpages-posix manpages-posix-dev'

class Ctags_Cscope(_apt_install):
    __doc__ = _('Ctags and Cscope: Popular source code parsers')
    category = 'dev'
    license = GPL
    pkgs = 'exuberant-ctags cscope'

class GMP(_apt_install):
    __doc__ = _('GNU multiprecision arithmetic library')
    category = 'dev'
    license = GPL
    pkgs = 'libgmp3-dev'

class Ncurses_and_qt3mt(_apt_install):
    __doc__ = _('Ncurses5 and QT3')
    detail = _('libncurses5 is a library controlling writing to the console screen.\n'
               'libqt3-mt is Trolltech Qt library, version 3.') 
    license = GPL
    category = 'dev'
    pkgs = 'libncurses5-dev libqt3-mt-dev'
        
class Svn_Git_bzr(_apt_install):
    __doc__ = _('Subversion, Git and Bzr: Popular version control systems')
    license = GPL
    category = 'dev'
    pkgs = 'subversion git-core bzr'
        
class AutoTools(_apt_install):
    __doc__ = _('Autoconf and Automake: Generate configure scripts and Makefiles')
    license = GPL
    category = 'dev'
    pkgs = 'autoconf automake'
        
class FreeGLut3(_apt_install):
    __doc__ = _('OpenGL library')  
    detail = _('This is a library for writing OpenGL programs.')
    license = GPL
    category = 'dev'
    pkgs = 'freeglut3-dev'
        
class Boost(_apt_install):
    __doc__ = _('Boost library')
    license = GPL
    category = 'dev'
    pkgs = 'libboost-dev'

class SDL(_apt_install):
    __doc__ = _('SDL library')
    detail = _('This is a library for writing SDL programs.\n'
               'SDL is a cross-platform multimedia library designed to provide low level access to audio'
               ' keyboard, mouse, joystick, 3D hardware via OpenGL, and 2D video framebuffer.')
    category = 'dev'
    license = LGPL
    pkgs = 'libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev'
    
#class PipeViewer(_apt_install):
#    __doc__ = _('pv: a pipe viewer')
#    detail = _('A terminal-based tool for monitoring the progress of data through a pipeline.')
#    license = AL + ' http://www.ivarch.com/programs/quickref/pv.shtml')
#    pkgs = 'pv'

# Auto-apt depends on postfix. But 'posifix' cannot be installed in Lucid :(
#class AutoApt(_apt_install):
#    'Auto-apt'
#    detail = _('"auto-apt run ./configure" can help you install the packages which are not installed.')
#    license = GPL
#    pkgs = 'auto-apt'

class CheckInstall(_apt_install):
    'CheckInstall'
    detail = _('Checkinstall help you build deb package.')
    license = GPL
    pkgs = 'checkinstall'
        
class Umbrello(_apt_install):
    __doc__ = _('Umbrello: UML modelling')
    detail = _('Umbrello help you do UML modelling.')
    license = GPL
    category = 'dev'
    pkgs = 'umbrello'

class Ubuntu_Studio_Theme(_apt_install):
    __doc__ = _('Ubuntu Studio Theme')
    license = GPL
    category = 'appearance'
    pkgs = 'ubuntustudio-theme ubuntustudio-icon-theme ubuntustudio-wallpapers ubuntustudio-gdm-theme'
    
class MiniCom_Ckermit(_apt_install):
    __doc__ = _('Minicom and Kermit: Communication software for embedded MCU boards')
    license = GPL
    category = 'embedded'
    pkgs = 'minicom ckermit'

class VirtualBox(_apt_install):
    __doc__ = _('VirtualBox open source edition')
    detail = _('It is the only professional virtual machine which is freely available '
       'under the terms of GPL. '
       'Official site: http://www.virtualbox.org/wiki/Downloads')
    license = GPL
    category = 'vm'
    pkgs = 'virtualbox-ose'

class GNOMEArtNextGen(I):
    __doc__ = _('GNOMEArtNG: Choose 100+ GNOME themes')
    detail = _('It is able to customize the backgrounds, application look, window borders, icons, GNOME splash and GDM window. '
       'More than 100 themes can be installed, which are downloaded from http://art.gnome.org . '
       'The official site of GNOMEArtNG is http://developer.berlios.de/projects/gnomeartng/')
    category = 'appearance'
    license = GPL
    def install(self):
        if Config.get_Ubuntu_version() == 'hardy':

            file = R(
['http://download.berlios.de/gnomeartng/gnomeartng-0.7.0-hardy.deb'],
471212, '52c556fafa9664284dcff9851528f3e5aae00ebe').download()
        
        elif Config.get_Ubuntu_version() == 'intrepid':
        
            file = R(
['http://download.berlios.de/gnomeartng/gnomeartng-0.7.0-intrepid.deb'],
444822, '4dc42fd446ebd8e615cf6490d6ecc94a403719b8').download()
        
        elif Config.get_Ubuntu_version() == 'jaunty':
        
            file = R(
['http://download.berlios.de/gnomeartng/gnomeartng-0.7.0-jaunty.deb'],
441222, 'c9134ad3405c660e6e07333994ca38d494f0f90f').download()
        
        elif Config.get_Ubuntu_version() == 'karmic':
        
            file = R(
['http://ailurus.googlecode.com/files/gnomeartng-0.7.0-karmic.deb',],
441558, 'b2b834b1bfc76f01dce370b60ea706f6ed35e4da').download()

        else:
            raise Exception('GNOMEArtNextGen', Config.get_Ubuntu_version())

        DPKG.install_deb(file)
        
        try: # Do not raise error, when this file cannot be downloaded.
            thumb = R(['http://download.berlios.de/gnomeartng/thumbs.tar.gz'],
               15575567, '7b7dcc3709d23383c1433f90abea5bea583202f9').download()
        except:
            return
        import os
        path = os.path.expanduser('~/.gnome2/gnome-art-ng/')
        if not os.path.exists(path): run('mkdir '+path)
        with Chdir(path) as o:
            run('tar xf '+thumb)
    def installed(self):
        return APT.installed('gnomeartng')
    def remove(self):
        APT.remove('gnomeartng')
    def support(self):
        return Config.get_Ubuntu_version() in ['hardy', 'intrepid', 'jaunty', 'karmic']
           
class QtiPlot(_apt_install) :
    __doc__ = _('QtiPlot: The equivalence of "Origin" plotting application in Linux')
    detail = _('It is the indispensable plotting application for writing Physics experiments reports.')
    category = 'math'
    license = GPL
    pkgs = 'qtiplot'

class Extcalc(_apt_install):
    __doc__ = _('Extcalc: A multifunctional graphic calculator')
    category = 'math'
    license = GPL
    pkgs = 'extcalc'
        
class StartupManager(_apt_install):
    __doc__ = _('Startup Manager: Change GRUB settings and themes')   
    detail = _('Startup manager helps you change GRUB settings and themes.')
    license = GPL
    category = 'appearance'
    pkgs = 'startupmanager'
        
class Zhcon(_apt_install):
    __doc__ = _('Zhcon')
    detail = _('Zhcon helps you display Chinese characters in TTY terminal.\n'
               'You can launch it by "zhcon --utf8".')
    Chinese = True
    license = GPL
    pkgs = 'zhcon'
        
class PowerTop(_apt_install):
    'PowerTop'
    detail = _('Powertop helps you save power for your laptop.')
    license = GPL
    pkgs = 'powertop'
        
class Nautilus_Actions(_apt_install):
    __doc__ = _('"Actions configuration" entry')
    detail = _('It allows the configuration of programs to be launched on files selected.\n'
               '<span color="red">This entry is not in context menu. It is in "System"->"Preferences" menu.</span>')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-actions'
        
class Nautilus_Filename_Repairer(_apt_install):
    __doc__ = _('"Repair filename" entry')
    detail = _('When any file with wrong encoding filename is right clicked,\n show a "Repair filename" menu item.')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-filename-repairer'

class Nautilus_Gksu(_apt_install):
    __doc__ = _('"Open as administrator" entry')
    detail = _('Launch selected files with administration privileges using the context menu.\nOpen selected folder with administration privileges.')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-gksu'

class Nautilus_Audio_Convert(_apt_install):
    __doc__ = _('"Convert audio files" entry')
    detail = _('Converts between WAV, OGG, MP3, MPC, FLAC, APE and AAC files.\n'
               'These packages will also be installed: \n'
               '<i>lame libid3-3.8.3-dev flac faac faad mppenc</i>')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-script-audio-convert lame libid3-3.8.3-dev flac faac faad mppenc'
    def install(self):
        _apt_install.install(self)
        run('nautilus-script-manager enable ConvertAudioFile')

class Nautilus_Image_Converter(_apt_install):
    __doc__ = _('"Resize/Rotate images" entries')
    detail = _('Resize or rotate selected images.')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-image-converter'
        
class Nautilus_Script_Collection_Svn(_apt_install):
    __doc__ = _('"Subversion commands" entries')
    detail = _('"Subversion commands" entries')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-script-collection-svn'
    def install(self):
        _apt_install.install(self)
        run('nautilus-script-manager enable Subversion')
        
class Nautilus_Open_Terminal(_apt_install):
    __doc__ = _('"Open in terminal" entry')
    detail = _('Open a terminal in current folder.')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-open-terminal'
        
class Nautilus_Share(_apt_install):
    __doc__ = _('"Share folders" entry')
    detail = _('Share folders by Samba.')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-share'
        
class Nautilus_Wallpaper(_apt_install):
    __doc__ = _('"Set as wallpaper" entry')
    detail = _('"Set as wallpaper" entry')
    license = GPL
    category = 'nautilus'
    pkgs = 'nautilus-wallpaper'
