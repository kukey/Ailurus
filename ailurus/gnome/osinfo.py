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

def row(text, value, icon=D+'umut_icons/i_default.png', tooltip = None):
    return (text, value, icon, tooltip)

def get():
    import os, re
    ret = []
    
    try:
        with open('/usr/share/gnome-about/gnome-version.xml') as f:
            for line in f:
                if 'platform' in line:
                    platform = re.search('<platform>(.+)</platform>', line).group(1)
                elif 'minor' in line:
                    minor = re.search('<minor>(.+)</minor>', line).group(1)
                elif 'micro' in line:
                    micro = re.search('<micro>(.+)</micro>', line).group(1)
                    break
        string = "%s.%s.%s" % (platform, minor, micro)
        ret.append( row(_('GNOME version:'), string, D+'umut_icons/i_gnome.png' ) )
    except:
        traceback.print_exc(file=sys.stderr)
        
    try: ret.append( row(_('GNOME locale:'), os.environ['LANG'], D+'umut_icons/i_locale.png' ) )
    except: traceback.print_exc(file=sys.stderr)

    return ret
