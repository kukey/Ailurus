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
import traceback
import sys, os
from lib import *

def __fedora_version():
    import sys, traceback
    try: 
        with open('/etc/fedora-release') as f:
            value = f.read().strip()
        return [row(_('Fedora version:'), value, D+'other_icons/fedora.png')]
	  if int(vaule[14:17])<12:
		import gtk
		button_preupgrade=gtk.Button(_('preupgrade').center(#这里不知道改写多少，而且这个按钮的位置也不会写，请升哥完善))
		button_preupgrade.connect('click',RPM.preupgrade())
    except: 
        traceback.print_exc(file=sys.stderr)
        return []

def get():
    return [__fedora_version]
