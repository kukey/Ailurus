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

#class software(self):
#	name=platform.dist()[0:1]
#	if name==('fedora')
#		self=RPM()
#	else name==('ubuntu')
#		self=APT()
#	else name==('debain')
#		pass

#def backup():
#	try:
#		t=open("/etc/samba/smb.conf","r").read()
#		n=open("smbbackup","w")
#		n.write(t)
#	except IOError:
#		notify('intall samba','ailurus found you not install samba and will heip you install it')
#		RPM.install('samba')
#		return scanandbankup()
#	finally:
#		n.close()
		
def confisamba(string):
	string='system-config-samba'
	RPM.installed('samba')
	if False:
		RPM.install('samba')
	RPM.installed(string)
	if False:
		notify('intall config tools','airlurus will help you install this')
		RPM.install('system-config-samba')
	run_as_root('system-config-samba')
	
def runsamba(string):
	string='/etc/init.d/smb start'
	run_as_root(string)

def stopsamba(string):
	string='/etc/init.d/smb stop'
	run_as_root(string)

