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
from apps_eclipse import *

class Disable_SELinux(I):
    __doc__ = _('Put Selinux in permissive mode, instead of enforcing mode.')
    def installed(self):
        with open('/etc/sysconfig/selinux') as f:
            c = f.read()
        if 'SELINUX=enforcing' in c: return False
        with open('/etc/selinux/config') as f:
            c = f.read()
        if 'SELINUX=enforcing' in c: return False
        return True
    def install(self):
        run_as_root_in_terminal('/usr/sbin/setenforce 0')
        for path in ['/etc/sysconfig/selinux', '/etc/selinux/config']:
            with TempOwn(path) as o:
                with open(path) as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if 'SELINUX=enforcing' in line: lines[i] = 'SELINUX=permissive\n'
                with open(path, 'w') as f:
                    f.writelines(lines)
    def remove(self):
        run_as_root_in_terminal('/usr/sbin/setenforce 0')
        for path in ['/etc/sysconfig/selinux', '/etc/selinux/config']:
            with TempOwn(path) as o:
                with open(path) as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if 'SELINUX=permissive' in line: lines[i] = 'SELINUX=enforcing\n'
                with open(path, 'w') as f:
                    f.writelines(lines)
        run_as_root_in_terminal('/usr/sbin/setenforce 1')

class Disable_Sudo(I):
    __doc__ = _('Disable "sudo". Prevent yourself from using "sudo".')
    def installed(self):
        return False
    def install(self):
        run_as_root_in_terminal(D+'../support/disable_sudo.py')
    def remove(self):
        pass

class Enable_Sudo(I):
    __doc__ = _('Enable "sudo"')
    detail = _('If you enabled "sudo" and you want to execute commands as root, '
               'you can type command "sudo COMMAND" instead of complicated command "su -c \'COMMAND\'". '
               '<span color="red">Due to restriction on filesystem permission, '
               'Ailurus cannot detect whether "sudo" is enabled.</span> ')
    def installed(self):
        return False
    def install(self):
        run_as_root_in_terminal(D+'../support/enable_sudo.py')
    def remove(self):
        pass
