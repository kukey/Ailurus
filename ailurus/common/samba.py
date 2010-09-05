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

from lib import *
import platform


def backup():
	try:
		t=open("/etc/samba/smb.conf","r").read()
		n=open("smbbackup","w")
		n.write(t)
	except IOError:
		notify('please install samba')
	finally:
		n.close()
        t.close()

def confisamba(string):
	string='system-config-samba'
	run_as_root(string)
    if CommandFailError:
        notify('please install system-config-samba.')

#def runsamba(string):
#	string='/etc/init.d/smb start;/etc/init.d/nmb start'
#	run_as_root_in_terminal(string)
#   this will touch off AVC

#def stopsamba(string):
#	string='/etc/init.d/smb stop;/etc/inti.d/nmb stop'
#	run_as_root_in_terminal(string)
#   this always touch off commandfailerror?
