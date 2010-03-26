#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Ailurus - make Linux easier to use
#
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
from lib import *

class I:
    'Base class for all app installers'
    @classmethod
    def init(cls):
        pass
    @classmethod
    def install(cls):
        raise NotImplemented
    @classmethod
    def installed(cls):
        raise NotImplemented
    @classmethod
    def remove(cls):
        raise NotImplemented

class gconf_key(I):
    'Must subclass me and set "cls.set_value" and "cls.add_value"'
    @classmethod
    def __check_key(cls, key):
        if key=='':
            raise ValueError
        import re
        if re.match(r'^(/[a-zA-Z0-9-_]+)+$',key) is None:
            raise ValueError
    @classmethod
    def __check_list(cls, List):
        if len(List)==0:
            raise ValueError
        for e in List:
            if type(e)!=str:
                raise ValueError
            if e=='':
                raise ValueError
    @classmethod
    def __check(cls):
        cls.set_value # check existing
        cls.add_value # check existing
        if type(cls.set_value)!=tuple or type(cls.add_value)!=tuple:
            raise TypeError
        for e in cls.set_value:
            if type(e)!=tuple:
                raise TypeError
            if len(e)!=3:
                raise TypeError
            if type(e[0])!=str:
                raise TypeError
            cls.__check_key(e[0])
            if type(e[1])!=bool and type(e[1])!=int and type(e[1])!=float and type(e[1])!=str:
                raise TypeError
            if type(e[2])!=bool and type(e[2])!=int and type(e[2])!=float and type(e[2])!=str:
                raise TypeError
        for e in cls.add_value:
            if type(e)!=tuple:
                raise TypeError
            if len(e)!=2:
                raise TypeError
            if type(e[0])!=str:
                raise TypeError
            cls.__check_key(e[0])
            if type(e[1])!=list:
                raise TypeError
            cls.__check_list(e[1])
    @classmethod
    def install(cls):
        cls.__check()
        import gconf
        G = gconf.client_get_default()
        if len(cls.set_value) or len(cls.add_value):
            print _("Change GConf values:")
        for key, newvalue, oldvalue in cls.set_value:
            G.set_value(key, newvalue)
            print _("Key:"), "\x1b[1;33m%s\x1b[m"%key,
            print _("New value:"), "\x1b[1;33m%s\x1b[m"%newvalue
        for key, to_add_list in cls.add_value:
            List = G.get_list(key, gconf.VALUE_STRING)
            for to_add in to_add_list:
                try:
                    List.remove(to_add)
                except ValueError:
                    pass
                List.insert(0, to_add)
            G.set_list(key, gconf.VALUE_STRING, List)
            print _("Key:"), "\x1b[1;33m%s\x1b[m"%key
            print _("Appended items:"), "\x1b[1;33m%s\x1b[m"%to_add_list
    @classmethod
    def installed(cls):
        cls.__check()
        import gconf
        G = gconf.client_get_default()
        for key, newvalue, oldvalue in cls.set_value:
            try:
                value=G.get_value(key)
                if type(value)!=float and value!=newvalue:
                    return False
                if type(value)==float and  abs(value-newvalue)>1e-6:
                    return False
            except ValueError: #key does not exist
                return False
        for key, to_add_list in cls.add_value:
            List = G.get_list(key, gconf.VALUE_STRING)
            for to_add in to_add_list:
                if not to_add in List:
                    return False
        return True
    @classmethod
    def _get_reason(cls, f):
        import gconf
        G = gconf.client_get_default()
        for key, newvalue, oldvalue in cls.set_value:
            try: value = G.get_value(key)
            except: value = None
            if ( type(value)!=float and value!=newvalue ) or ( type(value)==float and abs(value-newvalue)>1e-6 ):
                print >>f, _('The value of "%(key)s" is not "%(value)s".')%{'key':key, 'value':newvalue},
        for key, to_add_list in cls.add_value:
            List = G.get_list(key, gconf.VALUE_STRING)
            #evaluate "not_in" list
            not_in = []
            for to_add in to_add_list:
                if not to_add in List:
                    not_in.append(to_add)
            #output
            if not_in:
                print >>f, _('"%(value)s" is not in "%(key)s".')%{'value':' '.join(not_in), 'key':key}, 
    @classmethod
    def remove(cls):
        cls.__check()
        import gconf
        G = gconf.client_get_default()
        if len(cls.set_value) or len(cls.add_value):
            print _("Change GConf values:")
        for key, newvalue, oldvalue in cls.set_value:
            G.set_value(key, oldvalue)
            print _("Key:"), "\x1b[1;33m%s\x1b[m"%key,
            print _("New value:"), "\x1b[1;33m%s\x1b[m"%oldvalue
        for key, to_remove_list in cls.add_value:
            List = G.get_list(key, gconf.VALUE_STRING)
            for to_remove in to_remove_list:
                try:
                    List.remove(to_remove)
                except ValueError:
                    pass
            G.set_list(key, gconf.VALUE_STRING, List)
            print _("Key:"), "\x1b[1;33m%s\x1b[m"%key
            print _("Removed items:"), "\x1b[1;33m%s\x1b[m"%to_remove_list
    @classmethod
    def support(cls):
        try:
            import gconf
            return True
        except:
            return False 

class apt_install(I):
    'Must subclass me and set "pkgs".'
    @classmethod
    def __check(cls):
        cls.pkgs # check exists
        if type(cls.pkgs) != str:
            raise TypeError
        if cls.pkgs == '' :
            raise ValueError
        for pkg in cls.pkgs.split():
            import re
            if re.match(r'^[a-zA-Z0-9.-]+$', pkg) is None:
                raise ValueError, pkg
            if pkg[0]=='-':
                raise ValueError, pkg
    @classmethod
    def install(cls):
        cls.__check()
        APT.install(*cls.pkgs.split())
    @classmethod
    def installed(cls):
        cls.__check()
        for pkg in cls.pkgs.split():
            if not APT.installed(pkg):
                return False
        return True
    @classmethod
    def _get_reason(cls, f):
        #evaluate
        not_in = []
        for pkg in cls.pkgs.split():
            if not APT.installed(pkg):
                not_in.append(pkg)
        #output
        print >>f, _('The packages "%s" are not installed.') % ' '.join(not_in),
    @classmethod
    def remove(cls):
        cls.__check()
        APT.remove(*cls.pkgs.split())

class path_lists(I):
    @classmethod
    def __check(cls):
        if not isinstance(cls.paths, list):
            raise TypeError
        if len(cls.paths)==0: 
            raise ValueError
        for path in cls.paths:
            if not isinstance(path, str):
                raise TypeError
            if path=='':
                raise ValueError
    @classmethod
    def install(cls):
        raise NotImplementedError
    @classmethod
    def installed(cls):
        cls.__check()
        for path in cls.paths:
            import os
            if not os.path.exists(path):
                return False
        return True
    @classmethod
    def remove(cls):
        cls.__check()
        for path in cls.paths:
            gksudo('rm "%s" -rf'%path)
    @classmethod
    def _get_reason(cls, f):
        import os
        #evaluate
        no_list = []
        for path in cls.paths:
            if not os.path.exists(path): no_list.append(path)
        #output
        if no_list:
            print >>f, _('"%s" does not exist.')%' '.join(no_list),

class ff_extension(I):
    'Firefox Extension'
    category = 'firefox'
    logo = 'default.png'
    @classmethod
    def init(cls):
        if not hasattr(ff_extension, 'ext_path'):
            ff_extension.ext_path =  FirefoxExtensions.get_extensions_path()
        
        assert cls.name, 'No %s.name'%cls.__class__.__name__
        assert isinstance(cls.name, unicode)
        assert cls.R, 'No %s.R'%cls.__class__.__name__
        assert isinstance(cls.R, R)
        assert isinstance(cls.desc, unicode) or isinstance(cls.desc, str) 
        assert isinstance(cls.download_url, str)
        assert isinstance(cls.range, str)
        import StringIO
        text = StringIO.StringIO()
        if cls.desc:
            print >>text, cls.desc
        print >>text, _("<span color='red'>This extension cannot be removed by Ailurus. It can be removed in 'Tools'->'Add-ons' menu of firefox.</span>")
        print >>text, _('It can be used in Firefox version %s')%cls.range
        print >>text, _('It can be obtained from '), cls.download_url
        cls.__class__.detail = text.getvalue()
        text.close()
    @classmethod
    def install(cls):
        f = cls.R.download()
        if f.endswith('.xpi') or f.endswith('.jar'):
            run('cp %s %s'%(f, ff_extension.ext_path) )
            delay_notify_firefox_restart()
        else:
            raise NotImplementedError(cls.name, f)
    @classmethod
    def __exists_in_ext_path(cls):
        try:
            f = cls.R.filename
            import os
            return os.path.exists(ff_extension.ext_path+'/'+f)
        except:
            return False
    @classmethod
    def installed(cls):
        return FirefoxExtensions.installed(cls.name) or cls.__exists_in_ext_path()
    @classmethod
    def remove(cls):
        raise NotImplementedError

class download_one_file(I):
    @classmethod
    def install(cls):
        assert isinstance(cls.R, R)
        f = cls.R.download()
        run('cp %s %s'%(f, cls.file) )
    @classmethod
    def installed(cls):
        import os
        return os.path.exists(cls.file)
    @classmethod
    def remove(cls):
        run('''rm -f '%s' '''%cls.file)
    @classmethod
    def get_reason(cls, f):
        import os
        if not os.path.exists(cls.file):
            print >>f, _('"%s" does not exist.')%cls.file,

class rpm_install(I):
    @classmethod
    def _check(cls):
        assert isinstance(cls.pkgs, str)
    @classmethod
    def install(cls):
        cls._check()
        RPM.install(cls.pkgs)
    @classmethod
    def installed(cls):
        cls._check()
        for p in cls.pkgs.split():
            if not RPM.installed(p): return False
        return True
    @classmethod
    def remove(cls):
        cls._check()
        RPM.remove(cls.pkgs)
    @classmethod
    def _get_reason(cls, f):
        cls._check()
        #evaluate
        not_in = []
        for pkg in cls.pkgs.split():
            if not RPM.installed ( pkg ):
                not_in.append(pkg)
        #output
        print >>f, _('The packages "%s" are not installed.')%' '.join(not_in),
