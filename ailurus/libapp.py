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
from lib import *

__all__ = ['_set_gconf', '_apt_install', '_path_lists', '_ff_extension', '_download_one_file', '_rpm_install']

class _set_gconf(I):
    'Must subclass me and set "self.set" and "self.add"'
    def __check_key(self, key):
        if key=='':
            raise ValueError
        import re
        if re.match(r'^(/[a-zA-Z0-9-_]+)+$',key) is None:
            raise ValueError
    def __check_list(self, List):
        if len(List)==0:
            raise ValueError
        for e in List:
            if type(e)!=str:
                raise ValueError
            if e=='':
                raise ValueError
    def __check(self):
        self.set # check existing
        self.add # check existing
        if type(self.set)!=tuple or type(self.add)!=tuple:
            raise TypeError
        for e in self.set:
            if type(e)!=tuple:
                raise TypeError
            if len(e)!=3:
                raise TypeError
            if type(e[0])!=str:
                raise TypeError
            self.__check_key(e[0])
            if type(e[1])!=bool and type(e[1])!=int and type(e[1])!=float and type(e[1])!=str:
                raise TypeError
            if type(e[2])!=bool and type(e[2])!=int and type(e[2])!=float and type(e[2])!=str:
                raise TypeError
        for e in self.add:
            if type(e)!=tuple:
                raise TypeError
            if len(e)!=2:
                raise TypeError
            if type(e[0])!=str:
                raise TypeError
            self.__check_key(e[0])
            if type(e[1])!=list:
                raise TypeError
            self.__check_list(e[1])
    def __init__(self):
        raise NotImplementedError
    def install(self):
        self.__check()
        import gconf
        G = gconf.client_get_default()
        if len(self.set) or len(self.add):
            print '\x1b[1;32m', _("Change GConf values:"), '\x1b[m'
        for key, newvalue, oldvalue in self.set:
            G.set_value(key, newvalue)
            print "\x1b[1;32m%s\x1b[m"%_("Key:"), key,
            print "\x1b[1;32m%s\x1b[m"%_("New value:"), newvalue
        for key, to_add_list in self.add:
            List = G.get_list(key, gconf.VALUE_STRING)
            for to_add in to_add_list:
                try:
                    List.remove(to_add)
                except ValueError:
                    pass
                List.insert(0, to_add)
            G.set_list(key, gconf.VALUE_STRING, List)
            print "\x1b[1;32m%s\x1b[m"%_("Key:"), key
            print "\x1b[1;32m%s\x1b[m"%_("Appended items:"), to_add_list
    def installed(self):
        self.__check()
        import gconf
        G = gconf.client_get_default()
        for key, newvalue, oldvalue in self.set:
            try:
                value=G.get_value(key)
                if type(value)!=float and value!=newvalue:
                    return False
                if type(value)==float and  abs(value-newvalue)>1e-6:
                    return False
            except ValueError: #key does not exist
                return False
        for key, to_add_list in self.add:
            List = G.get_list(key, gconf.VALUE_STRING)
            for to_add in to_add_list:
                if not to_add in List:
                    return False
        return True
#    def _get_reason(self, f):
#        import gconf
#        G = gconf.client_get_default()
#        for key, newvalue, oldvalue in self.set:
#            try: value = G.get_value(key)
#            except: value = None
#            if ( type(value)!=float and value!=newvalue ) or ( type(value)==float and abs(value-newvalue)>1e-6 ):
#                print >>f, _('The value of "%(key)s" is not "%(value)s".')%{'key':key, 'value':newvalue},
#        for key, to_add_list in self.add:
#            List = G.get_list(key, gconf.VALUE_STRING)
#            #evaluate "not_in" list
#            not_in = []
#            for to_add in to_add_list:
#                if not to_add in List:
#                    not_in.append(to_add)
#            #output
#            if not_in:
#                print >>f, _('"%(value)s" is not in "%(key)s".')%{'value':' '.join(not_in), 'key':key}, 
    def remove(self):
        self.__check()
        import gconf
        G = gconf.client_get_default()
        if len(self.set) or len(self.add):
            print '\x1b[1;31m', _("Change GConf values:"), '\x1b[m'
        for key, newvalue, oldvalue in self.set:
            G.set_value(key, oldvalue)
            print "\x1b[1;31m%s\x1b[m"%_("Key:"), key,
            print "\x1b[1;31m%s\x1b[m"%_("New value:"), oldvalue
        for key, to_remove_list in self.add:
            List = G.get_list(key, gconf.VALUE_STRING)
            for to_remove in to_remove_list:
                try:
                    List.remove(to_remove)
                except ValueError:
                    pass
            G.set_list(key, gconf.VALUE_STRING, List)
            print "\x1b[1;31m%s\x1b[m"%_("Key:"), key
            print "\x1b[1;31m%s\x1b[m"%_("Removed items:"), to_remove_list
    def support(self):
        try:
            import gconf
            return True
        except:
            return False 

class _apt_install(I):
    'Must subclass me and set "pkgs".'
    def __check(self):
        self.pkgs # check exists
        if type ( self.pkgs ) != str:
            raise TypeError
        if self.pkgs == '' :
            raise ValueError, 'self.pkgs is empty.'
        for pkg in self.pkgs.split():
            import re
            if re.match(r'^[a-zA-Z0-9.-]+$', pkg) is None:
                raise ValueError, pkg
            if pkg[0]=='-':
                raise ValueError, pkg
    def install(self):
        self.__check()
        APT.install(*self.pkgs.split())
    def installed(self):
        self.__check()
        for pkg in self.pkgs.split():
            if not APT.installed ( pkg ):
                return False
        return True
    def get_reason(self, f):
        all_pkgs = self.pkgs.split()
        if len(all_pkgs) > 1:
            not_installed = [p for p in all_pkgs if not APT.installed(p)]
            if len(not_installed) != len(all_pkgs):
                print >>f, _('Because the packages "%s" are not installed.')%' '.join(not_installed),
    def remove(self):
        self.__check()
        APT.remove(*self.pkgs.split() )
    def installation_command(self):
        return _('Command:') + ' sudo apt-get install ' + self.pkgs

class _path_lists(I):
    def __check(self):
        if not isinstance(self.paths, list):
            raise TypeError
        if len(self.paths)==0: 
            raise ValueError
        for path in self.paths:
            if not isinstance(path, str):
                raise TypeError
            if path=='':
                raise ValueError
    def __init__(self):
        raise NotImplementedError
    def install(self):
        raise NotImplementedError
    def installed(self):
        self.__check()
        for path in self.paths:
            import os
            if not os.path.exists(path):
                return False
        return True
    def remove(self):
        self.__check()
        for path in self.paths:
            run_as_root('rm "%s" -rf'%path)
    def get_reason(self, f):
        import os
        not_exist = [p for p in self.paths if not os.path.exists(p)]
        if not_exist:
            print >>f, _('Because "%s" does not exist.')%' '.join(not_exist),

class _ff_extension(I):
    'Firefox Extension'
    category = 'firefox'
    def __init__(self):
        if not hasattr(_ff_extension, 'ext_path'):
            _ff_extension.ext_path =  FirefoxExtensions.get_extensions_path()
        
        assert self.name, 'No %s.name'%self.__class__.__name__
        assert isinstance(self.name, unicode)
        assert self.R, 'No %s.R'%self.__class__.__name__
        assert isinstance(self.R, R)
        assert isinstance(self.desc, unicode) or isinstance(self.desc, str) 
        assert isinstance(self.download_url, str)
        assert isinstance(self.range, str)
        import StringIO
        text = StringIO.StringIO()
        if self.desc:
            print >>text, self.desc
        print >>text, _("<span color='red'>This extension cannot be removed by Ailurus. It can be removed in 'Tools'->'Add-ons' menu of firefox.</span>")
        print >>text, _('It can be used in Firefox version %s')%self.range
        print >>text, _('It can be obtained from '), self.download_url
        self.__class__.detail = text.getvalue()
        text.close()
    def install(self):
        f = self.R.download()
        if f.endswith('.xpi') or f.endswith('.jar'):
            run('cp %s %s'%(f, _ff_extension.ext_path) )
            delay_notify_firefox_restart()
        else:
            raise NotImplementedError(self.name, f)
    def __exists_in_ext_path(self):
        try:
            f = self.R.filename
            import os
            return os.path.exists(_ff_extension.ext_path+'/'+f)
        except:
            return False
    def installed(self):
        return FirefoxExtensions.installed(self.name) or self.__exists_in_ext_path()
    def remove(self):
        print '\x1b[1;31m', _("This extension cannot be removed by Ailurus. It can be removed in 'Tools'->'Add-ons' menu of firefox."), '\x1b[m'
        raise NotImplementedError

class _download_one_file(I):
    def install(self):
        assert isinstance(self.R, R)
        f = self.R.download()
        run('cp %s %s'%(f, self.file) )
    def installed(self):
        import os
        return os.path.exists(self.file)
    def remove(self):
        run('''rm -f '%s' '''%self.file)
    def get_reason(self, f):
        import os
        if not os.path.exists(self.file):
            print >>f, _('Because "%s" does not exist.')%self.file,

class _rpm_install(I):
    def _check(self):
        assert isinstance(self.pkgs, str)
    def install(self):
        self._check()
        RPM.install(self.pkgs)
    def installed(self):
        self._check()
        for p in self.pkgs.split():
            if not RPM.installed(p): return False
        return True
    def remove(self):
        self._check()
        RPM.remove(self.pkgs)
    def get_reason(self, f):
        self._check()
        all_pkgs = self.pkgs.split()
        if len(all_pkgs) > 1:
            not_installed = [p for p in all_pkgs if not RPM.installed(p)]
            if len(not_installed) != len(all_pkgs):
                print >>f, _('Because the packages "%s" are not installed.')%' '.join(not_installed),
    def installation_command(self):
        return _('Command:') + (' su -c "yum install %s"' % self.pkgs)
