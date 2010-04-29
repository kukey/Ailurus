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

def _g1():
    return [
['Patan.com.ar', _('Argentina'), 'http://ubuntu.patan.com.ar/ubuntu/', 'ubuntu.patan.com.ar',],
['iiNet', _('Australia'), 'http://ftp.iinet.net.au/pub/ubuntu/', 'ftp.iinet.net.au',],
['Netspace Online Systems', _('Australia'), 'http://ftp.netspace.net.au/pub/ubuntu/', 'ftp.netspace.net.au',],
['AARNet Pty Ltd', _('Australia'), 'http://mirror.aarnet.edu.au/pub/ubuntu/archive/', 'mirror.aarnet.edu.au',],
['Internode', _('Australia'), 'http://mirror.internode.on.net/pub/ubuntu/ubuntu/', 'mirror.internode.on.net',],
['Netspace Online Systems', _('Australia'), 'http://mirror.netspace.net.au/pub/ubuntu/', 'mirror.netspace.net.au',],
['Optus.net', _('Australia'), 'http://mirror.optus.net/ubuntu/', 'mirror.optus.net',],
['Pacnet Australia', _('Australia'), 'http://mirror.pacific.net.au/linux/ubuntu/', 'mirror.pacific.net.au',],
['WAIA', _('Australia'), 'http://mirror.waia.asn.au/ubuntu/', 'mirror.waia.asn.au',],
['Inode Telekommunikationsdienstleistungs GmbH', _('Austria'), 'http://ubuntu.inode.at/ubuntu/', 'ubuntu.inode.at',],
['lagis Internet Serviceprovider GmbH', _('Austria'), 'http://ubuntu.lagis.at/ubuntu/', 'ubuntu.lagis.at',],
['University of Klagenfurt', _('Austria'), 'http://ubuntu.uni-klu.ac.at/ubuntu/', 'ubuntu.uni-klu.ac.at',],
['Vienna University of Technology', _('Austria'), 'http://gd.tuwien.ac.at/opsys/linux/ubuntu/archive/', 'gd.tuwien.ac.at',],
['Rue Beltelecom, Datacenter', _('Belarus'), 'http://mirror.datacenter.by/ubuntu/', 'mirror.datacenter.by',],
['RUE Beltelecom, MGTS', _('Belarus'), 'http://ftp.byfly.by/ubuntu/', 'ftp.byfly.by',],
['linux.org.by mirror', _('Belarus'), 'http://linux.org.by/ubuntu/', 'linux.org.by',],
['BELNET', _('Belgium'), 'http://ftp.belnet.be/mirror/ubuntu.com/ubuntu/', 'ftp.belnet.be',],
['Infogroep', _('Belgium'), 'http://gaosu.rave.org/ubuntu/', 'gaosu.rave.org',],
['Skynet Belgacom', _('Belgium'), 'http://ubuntu.mirrors.skynet.be/pub/ubuntu.com/ubuntu/', 'ubuntu.mirrors.skynet.be',],
['BiHnet ISP, BH Telecom', _('Bosnia and Herzegovina'), 'http://archive.ubuntu.com.ba/ubuntu/', 'archive.ubuntu.com.ba',],
['Globo.com', _('Brazil'), 'http://mirror.globo.com/ubuntu/archive/', 'mirror.globo.com',],
['C3SL/UFPR', _('Brazil'), 'http://br.archive.ubuntu.com/ubuntu/', 'br.archive.ubuntu.com',],
['PoP-SC/RNP', _('Brazil'), 'http://ubuntu.mirror.pop-sc.rnp.br/ubuntu/', 'ubuntu.mirror.pop-sc.rnp.br',],
['Edugraf - INE - CTC - UFSC', _('Brazil'), 'http://espelhos.edugraf.ufsc.br/ubuntu/', 'espelhos.edugraf.ufsc.br',],
['University of Sao Paulo', _('Brazil'), 'http://sft.if.usp.br/ubuntu/', 'sft.if.usp.br:',],
['LAS-IC-Unicamp', _('Brazil'), 'http://www.las.ic.unicamp.br/pub/ubuntu/', 'rsync.las.ic.unicamp.br',],
['Interlegis', _('Brazil'), 'http://ubuntu.interlegis.gov.br/ubuntu/', 'ubuntu.interlegis.gov.br',],
['IPACCT', _('Bulgaria'), 'http://ubuntu.ipacct.com/ubuntu/', 'ubuntu.ipacct.com',],
['hitsol.net', _('Bulgaria'), 'http://ubuntu.hitsol.net/ubuntu/', 'ubuntu.hitsol.net',],
['Linux-BG.org', _('Bulgaria'), 'http://ubuntu.linux-bg.org/ubuntu/', 'ubuntu.linux-bg.org',],
['nano-box.net', _('Bulgaria'), 'http://ubuntu.nano-box.net/ubuntu/', 'ubuntu.nano-box.net',],
['University of Waterloo Computer Science Club', _('Canada'), 'http://mirror.csclub.uwaterloo.ca/ubuntu/', 'mirror.csclub.uwaterloo.ca',],
['Shaw Cable', _('Canada'), 'http://ubuntu.arcticnetwork.ca/', 'ubuntu.arcticnetwork.ca',],
['iWeb Technologies Inc.', _('Canada'), 'http://ubuntu.mirror.iweb.ca/', 'ubuntu.mirror.iweb.ca',],
['Savoir-faire Linux', _('Canada'), 'http://gpl.savoirfairelinux.net/pub/mirrors/ubuntu/', 'gpl.savoirfairelinux.net',],
['Department of Computer Science, University of Calgary', _('Canada'), 'http://mirror.cpsc.ucalgary.ca/mirror/ubuntu.com/packages/', 'mirror.cpsc.ucalgary.ca',],
['Memorial University of Newfoundland', _('Canada'), 'ftp://ftp.cs.mun.ca/pub/mirror/ubuntu/', 'ftp.cs.mun.ca',],
['Ubuntu-mirror-rafal-ca', _('Canada'), 'http://ubuntu.mirror.rafal.ca/ubuntu/', 'ubuntu.mirror.rafal.ca',],
['TECNOERA', _('Chile'), 'http://ftp.tecnoera.com/ubuntu/', 'ftp.tecnoera.com',],
['Departamento de Fisica, Universidad de Chile', _('Chile'), 'http://cl.archive.ubuntu.com/ubuntu/', 'cl.archive.ubuntu.com',],
['Escuela de Ingeniería Informática - PUCV', _('Chile'), 'http://mirror.gnucv.cl/ubuntu/', 'mirror.gnucv.cl',],
['cn99', _('China'), 'http://ubuntu.cn99.com/ubuntu/', 'ubuntu.cn99.com',],
['LUPA', _('China'), 'http://mirror.lupaworld.com/ubuntu/', 'mirror.lupaworld.com',],
['Rootguide.org', _('China'), 'http://mirror.rootguide.org/ubuntu/', 'mirror.rootguide.org',],
['NetEase', _('China'), 'http://mirrors.163.com/ubuntu/', 'mirrors.163.com',],
['Shanghai Linux User Group', _('China'), 'http://mirrors.shlug.org/ubuntu/', 'mirrors.shlug.org',],
['Ubuntu@UESTC', _('China'), 'http://ubuntu.dormforce.net/ubuntu/', 'ubuntu.dormforce.net',],
['SRT', _('China'), 'http://ubuntu.srt.cn/ubuntu/', 'ubuntu.srt.cn',],
['Universidad Nacional De Colombia Grupo SoLiUN - Makuruma', _('Colombia'), 'http://matematicas.unal.edu.co/ubuntu/', 'matematicas.unal.edu.co',],
['Universidad de Costa Rica', _('Costa Rica'), 'http://mirrors.ucr.ac.cr/ubuntu/', 'mirrors.ucr.ac.cr',],
['Faculty of civil engineering, Zagreb', _('Croatia'), 'http://hr.archive.ubuntu.com/ubuntu/', 'hr.archive.ubuntu.com',],
['Cytanet', _('Cyprus'), 'http://mirrors.cytanet.com.cy/linux/ubuntu/archive/', 'mirrors.cytanet.com.cy',],
['Silicon Hill', _('Czech Republic'), 'http://ftp.sh.cvut.cz/MIRRORS/ubuntu/', 'ftp.sh.cvut.cz',],
['UPC Česká republika, a.s.', _('Czech Republic'), 'http://archive.ubuntu.mirror.dkm.cz/', 'ubuntu.mirror.dkm.cz',],
['CZ.NIC, z.s.p.o.', _('Czech Republic'), 'http://cz.archive.ubuntu.com/ubuntu/', 'cz.archive.ubuntu.com',],
['Czech Technical University Prague', _('Czech Republic'), 'http://ftp.cvut.cz/ubuntu/', 'ftp.cvut.cz',],
['Czech Technical University Prague', _('Czech Republic'), 'http://ubuntu.sh.cvut.cz/', 'ubuntu.sh.cvut.cz',],
['Ignum, s.r.o.', _('Czech Republic'), 'http://ucho.ignum.cz/ubuntu/', 'ucho.ignum.cz',],
['Advokatni kancelar Kindl&Partneri', _('Czech Republic'), 'http://ubuntu.supp.name/ubuntu/', 'ubuntu.supp.name',],
['KLID', _('Denmark'), 'http://ftp.klid.dk/ftp/ubuntu/', 'ftp.klid.dk',],
['dotsrc.org', _('Denmark'), 'http://mirrors.dotsrc.org/ubuntu/', 'mirrors.dotsrc.org',],
['UNI-C', _('Denmark'), 'http://mirror.uni-c.dk/ubuntu/', 'mirror.uni-c.dk',],
['Elion Enterprises Ltd', _('Estonia'), 'http://ftp.estpak.ee/ubuntu/', 'ftp.estpak.ee',],
['CSC / Funet', _('Finland'), 'http://mirrors.nic.funet.fi/ubuntu/', 'mirrors.nic.funet.fi',],
['CSC / Funet', _('Finland'), 'http://www.nic.funet.fi/pub/mirrors/archive.ubuntu.com/', 'rsync.nic.funet.fi',],
['Free', _('France'), 'http://ubuntu-archive.mirrors.proxad.net/ubuntu/', 'ubuntu-archive.mirrors.proxad.net',],
['Fondation d\'entreprise Free', _('France'), 'http://ftp.free.org/mirrors/archive.ubuntu.com/ubuntu/', 'ftp.free.org',],
['OVH', _('France'), 'http://mirror.ovh.net/ubuntu/', 'mirror.ovh.net',],
['CRIHAN', _('France'), 'http://ftp.crihan.fr/ubuntu/', 'ftp.crihan.fr',],
['Orange Business Services', _('France'), 'http://ftp.oleane.net/ubuntu/', 'ftp.oleane.net',],
['Université de Nantes', _('France'), 'http://ubuntu.univ-nantes.fr/ubuntu/', 'ubuntu.univ-nantes.fr',],
['LIP6/UPMC', _('France'), 'http://www-ftp.lip6.fr/pub/linux/distributions/Ubuntu/', 'ftp.lip6.fr',],
['CIRIL', _('France'), 'http://wwwftp.ciril.fr/pub/linux/ubuntu/archives/', 'ftp.ciril.fr',],
['Florian Entreprise', _('France'), 'http://archive.monubuntu.fr/', 'archive.monubuntu.fr',],
['Université de Picardie', _('France'), 'http://ftp.u-picardie.fr/mirror/ubuntu/ubuntu/', 'ftp.u-picardie.fr',],
['IPSL', _('France'), 'http://distrib-coffee.ipsl.jussieu.fr/ubuntu/', 'distrib-coffee.ipsl.jussieu.fr',],
['Universite Reims Champagne-Ardenne', _('France'), 'http://ubuntu.univ-reims.fr/ubuntu/', 'ubuntu.univ-reims.fr',],
['LoLiTa', _('French Polynesia'), 'http://pf.archive.ubuntu.com/ubuntu/', 'pf.archive.ubuntu.com',],
['Open Consultants', _('Georgia'), 'http://ubuntu.eriders.ge/ubuntu/', 'ubuntu.eriders.ge',],
['Technische Universität Dresden', _('Germany'), 'http://ubuntu.mirror.tudos.de/ubuntu/', 'ubuntu.mirror.tudos.de',],
['Esslingen University of Applied Sciences', _('Germany'), 'http://ftp-stud.hs-esslingen.de/ubuntu/', 'ftp-stud.hs-esslingen.de',],
['University of Kaiserslautern', _('Germany'), 'http://ftp.uni-kl.de/pub/linux/ubuntu/', 'ftp.uni-kl.de',],
['NetCologne', _('Germany'), 'http://mirror.netcologne.de/ubuntu/', 'mirror.netcologne.de',],
['intergenia AG', _('Germany'), 'http://ubuntu.intergenia.de/ubuntu/', 'ubuntu.intergenia.de',],
['Freie Universität Berlin', _('Germany'), 'ftp://ftp.fu-berlin.de/linux/ubuntu/', 'ftp.fu-berlin.de',],
['RRZN, Leibniz Universität Hannover', _('Germany'), 'ftp://ftp.rrzn.uni-hannover.de/pub/mirror/linux/ubuntu', 'ftp.rrzn.uni-hannover.de',],
['RRZN', _('Germany'), 'ftp://ftp.rrzn.uni-hannover.de/pub/mirror/linux/ubuntu/', 'ftp.rrzn.uni-hannover.de',],
['StudNet Bonn', _('Germany'), 'http://ftp.stw-bonn.de/ubuntu/', 'ftp.stw-bonn.de',],
['TU-Ilmenau', _('Germany'), 'http://ftp.tu-ilmenau.de/mirror/ubuntu/', 'ftp.tu-ilmenau.de',],
['Universität Bayreuth', _('Germany'), 'http://ftp.uni-bayreuth.de/linux/ubuntu/ubuntu/', 'rsync.uni-bayreuth.de',],
['Universität Erlangen-Nürnberg', _('Germany'), 'http://ftp.uni-erlangen.de/mirrors/ubuntu/', 'ftp.uni-erlangen.de',],
['Universität Münster', _('Germany'), 'http://ftp.uni-muenster.de/pub/mirrors/ftp.ubuntu.com/ubuntu/', 'ftp.uni-muenster.de',],
['GWDG', _('Germany'), 'http://ftp5.gwdg.de/pub/linux/debian/ubuntu/', 'ftp5.gwdg.de',],
['FH-Aachen', _('Germany'), 'http://mirror.bauhuette.fh-aachen.de/ubuntu/', 'mirror.bauhuette.fh-aachen.de',],
['SunSITE.RWTH-Aachen.de', _('Germany'), 'http://sunsite.informatik.rwth-aachen.de/ftp/pub/Linux/ubuntu/ubuntu/', 'sunsite.informatik.rwth-aachen.de',],
['University of Leipzig', _('Germany'), 'http://suse.uni-leipzig.de/pub/releases.ubuntu.com/ubuntu/', 'suse.uni-leipzig.de',],
['University of Mannheim', _('Germany'), 'http://swtsrv.informatik.uni-mannheim.de/pub/linux/distributions/ubuntu/', 'swtsrv.informatik.uni-mannheim.de',],
['UNITED COLO GmbH', _('Germany'), 'http://ubuntu.unitedcolo.de/ubuntu/', 'ubuntu.unitedcolo.de',],
['University of Applied Sciences Wolfenbuettel', _('Germany'), 'http://archive.ubuntu.uasw.edu/', 'ftp.uasw.edu',],
['Charite Berlin', _('Germany'), 'http://debian.charite.de/ubuntu/', 'debian.charite.de',],
['Host Europe', _('Germany'), 'http://ftp.hosteurope.de/mirror/archive.ubuntu.com/', 'ftp.hosteurope.de',],
['OSNT.org', _('Germany'), 'http://www.osnt.org/ubuntu/', 'www.osnt.org',],
['Ftp-stud-fht-esslingen-de', _('Germany'), 'http://ftp-stud.fht-esslingen.de/Mirrors/ubuntu/', 'ftp-stud.fht-esslingen.de',],
['Technische Universität Chemnitz', _('Germany'), 'http://ftp.tu-chemnitz.de/pub/linux/ubuntu/', 'ftp.tu-chemnitz.de',],
['University of Crete', _('Greece'), 'http://ftp.cc.uoc.gr/mirrors/linux/ubuntu/packages/', 'ftp.cc.uoc.gr',],
['Democritus University of Thrace', _('Greece'), 'http://ftp.duth.gr/pub/ubuntu/', 'ftp.duth.gr',],
['National Technical University of Athens', _('Greece'), 'http://ftp.ntua.gr/pub/linux/ubuntu/', 'ftp.ntua.gr',],
['National Technical University of Athens', _('Greece'), 'http://gr.archive.ubuntu.com/ubuntu/', 'gr.archive.ubuntu.com',],
['OTENET', _('Greece'), 'http://ubuntu.otenet.gr/', 'ftp.otenet.gr',],
['Tele Greenland A/S', _('Greenland'), 'http://mirror.greennet.gl/ubuntu/', 'mirror.greennet.gl',],
['Hostrino', _('Hong Kong'), 'http://ftp.hostrino.com/pub/ubuntu/archive/', 'ftp.hostrino.com',],
['Budapest University of Technology and Economics CrySyS Lab', _('Hungary'), 'http://ubuntu.mirrors.crysys.hu/', 'mirrors.crysys.hu',],
['FSN.hu Foundation ', _('Hungary'), 'http://ftp.freepark.org/ubuntu/', 'ftp.freepark.org',],
['Szechenyi Istvan University', _('Hungary'), 'http://ubuntu.sth.sze.hu/ubuntu/', 'ubuntu.sth.sze.hu',],
['KFKI.hu', _('Hungary'), 'http://ftp.kfki.hu/linux/ubuntu/', 'ftp.kfki.hu',],
['Ubuntu-lhi-is', _('Iceland'), 'http://ubuntu.lhi.is/ubuntu/', 'ubuntu.lhi.is',],
['Indian Institute of Technology, Kanpur', _('India'), 'http://mirror.cse.iitk.ac.in/ubuntu/', 'mirror.cse.iitk.ac.in',],
[' Honesty Net Solutions (I) Pvt Ltd', _('India'), 'http://ubuntuarchive.hnsdc.com/', 'ubuntuarchive.hnsdc.com',],
['Indian Institute of Technology, Bombay', _('India'), 'ftp://ftp.iitb.ac.in/distributions/ubuntu/archives/', 'ftp.iitb.ac.in',],
['Indian Institute of Technology Madras', _('India'), 'http://ftp.iitm.ac.in/ubuntu/', 'ftp.iitm.ac.in',],
['University of Indonesia', _('Indonesia'), 'http://kambing.ui.ac.id/ubuntu/', 'kambing.ui.ac.id',],
['EEPIS-ITS', _('Indonesia'), 'http://kebo.vlsm.org/ubuntu/', 'kebo.vlsm.org',],
['Universitas Diponegoro', _('Indonesia'), 'http://repo.undip.ac.id/ubuntu/', 'repo.undip.ac.id',],
['PT Telekomunikasi Indonesia', _('Indonesia'), 'http://dl2.foss-id.web.id/ubuntu/', 'dl2.foss-id.web.id',],
['IndikaNet', _('Indonesia'), 'http://ubuntu.indika.net.id/ubuntu/', 'ubuntu.indika.net.id',],
['PT Pasifik Satelit Nusantara', _('Indonesia'), 'http://ubuntu.pesat.net.id/archive/', 'ubuntu.pesat.net.id',],
['University of Jember', _('Indonesia'), 'http://mirror.unej.ac.id/ubuntu/', 'mirror.unej.ac.id',],
['HEAnet', _('Ireland'), 'http://ftp.heanet.ie/pub/ubuntu/', 'ftp.heanet.ie',],
['Esat Net', _('Ireland'), 'http://ftp.esat.net/mirrors/archive.ubuntu.com/', 'ftp.esat.net',],
['Israel Internet Association', _('Israel'), 'http://mirror.isoc.org.il/pub/ubuntu/', 'mirror.isoc.org.il',],
['InternetONE SRL', _('Italy'), 'http://mirror.internetone.it/ubuntu/', 'mirror.internetone.it',],
['Fastbull', _('Italy'), 'http://ubuntu.fastbull.org/ubuntu/', 'ubuntu.fastbull.org',],
['GARR/CILEA mirror service', _('Italy'), 'http://ubuntu.mirror.garr.it/mirrors/ubuntu-archive/', 'ubuntu.mirror.garr.it',],
['ICT Valle Umbra s.r.l.', _('Italy'), 'http://ubuntu.ictvalleumbra.it/ubuntu/', 'ubuntu.ictvalleumbra.it',],
['University of Genoa', _('Italy'), 'http://giano.com.dist.unige.it/ubuntu/', 'giano.com.dist.unige.it',],
['JAIST', _('Japan'), 'http://ftp.jaist.ac.jp/pub/Linux/ubuntu/', 'ftp.jaist.ac.jp',],
['RIKEN', _('Japan'), 'http://ftp.riken.jp/Linux/ubuntu/', 'ftp.riken.jp',],
['UNIVERSITY OF TOYAMA with Ubuntu Japanese LoCo', _('Japan'), 'http://ubuntutym.u-toyama.ac.jp/ubuntu/', 'ubuntutym.u-toyama.ac.jp',],
['Yamagata University', _('Japan'), 'http://ftp.yz.yamagata-u.ac.jp/pub/linux/ubuntu/archives/', 'ftp.yz.yamagata-u.ac.jp',],
['K.K. Ashisuto with Ubuntu Japanese LoCo', _('Japan'), 'http://ubuntu-ashisuto.ubuntulinux.jp/ubuntu/', 'ubuntu-ashisuto.ubuntulinux.jp',],
['mithril-linux.org (offered by Debian-JP Project member)', _('Japan'), 'http://ubuntu.mithril-linux.org/archives/', 'ubuntu.mithril-linux.org',],
['KDDI R&D Laboratories Inc.', _('Japan'), 'http://www.ftp.ne.jp/Linux/packages/ubuntu/archive/', 'rsync.kddilabs.jp',],
['Neolabs LLP', _('Kazakhstan'), 'http://mirror.neolabs.kz/ubuntu/', 'mirror.neolabs.kz',],
['SPACE.KZ LLP', _('Kazakhstan'), 'http://mirror.space.kz/ubuntu/', 'mirror.space.kz',],
['Daum Communications Corp.', _('Republic of Korea'), 'http://ftp.daum.net/ubuntu/', 'ftp.daum.net',],
['KAIST', _('Republic of Korea'), 'http://kr.archive.ubuntu.com/ubuntu/', 'kr.archive.ubuntu.com',],
['Kyung Hee University Linux User Group', _('Republic of Korea'), 'http://mirror.khlug.org/ubuntu/', 'mirror.khlug.org',],
['Qualitynet', _('Kuwait'), 'http://ubuntu.qualitynet.net/ubuntu/', 'ubuntu.qualitynet.net',],
['IKEEN', _('Kyrgyzstan'), 'http://ubuntu.mega.kg/ubuntu/', 'ubuntu.mega.kg',],
['University of Latvia', _('Latvia'), 'http://ubuntu-arch.linux.edu.lv/ubuntu/', 'ubuntu-arch.linux.edu.lv',],
['mirror.soften.ktu.lt', _('Lithuania'), 'http://mirror.soften.ktu.lt/ubuntu/', 'mirror.soften.ktu.lt',],
['LitNET', _('Lithuania'), 'http://ftp.litnet.lt/ubuntu/', 'ftp.litnet.lt',],
['Multimedia University (MMU)', _('Malaysia'), 'http://archive.mmu.edu.my/ubuntu/', 'archive.mmu.edu.my',],
['UPM', _('Malaysia'), 'http://mirror.upm.edu.my/ubuntu/', 'mirror.upm.edu.my',],
['MMU', _('Malaysia'), 'http://ubuntu.mmu.edu.my/ubuntu/', 'ubuntu.mmu.edu.my',],
['Universiti Putra Malaysia (UPM)', _('Malaysia'), 'http://www.mirror.upm.edu.my/ubuntu/', 'www.mirror.upm.edu.my',],
['OSCC', _('Malaysia'), 'http://mirror.oscc.org.my/ubuntu/', 'mirror.oscc.org.my',],
['Byte Craft', _('Malaysia'), 'http://ubuntu.bytecraft.com.my/ubuntu/', 'ubuntu.bytecraft.com.my',],
['Malta Linux User Group', _('Malta'), 'http://mirror.linux.org.mt/ubuntu/', 'mirror.linux.org.mt',],
['Facultad de Ciencias, UNAM', _('Mexico'), 'http://tezcatl.fciencias.unam.mx/ubuntu/', 'tezcatl.fciencias.unam.mx',],
['Universidad Juarez del Estado de Durango - UJED', _('Mexico'), 'http://ubuntu.ujed.mx/ubuntu/', 'ubuntu.ujed.mx',],
['BSD.MD', _('Republic of Moldova'), 'http://mirrors.bsd.md/ubuntu/', 'rsync.bsd.md',],
['Mongolian Open Source Initiative NGO', _('Mongolia'), 'http://archive.ubuntu.mnosi.org/ubuntu/', 'archive.ubuntu.mnosi.org',],
['Polytechnic of Namibia', _('Namibia'), 'http://ubuntu-archive.polytechnic.edu.na/ubuntu/', 'ftp.polytechnic.edu.na',],
['Mitra Network Private Limited', _('Nepal'), 'http://archive.mitra.net.np/ubuntu/', 'archive.mitra.net.np',],
['Cambrium BV.', _('Netherlands'), 'http://ubuntu.mirror.cambrium.nl/ubuntu/', 'ubuntu.mirror.cambrium.nl',],
['BIT B.V.', _('Netherlands'), 'http://nl.archive.ubuntu.com/ubuntu/', 'nl.archive.ubuntu.com',],
['University of Twente, The Netherlands', _('Netherlands'), 'http://ftp.snt.utwente.nl/pub/os/linux/ubuntu-archive/', 'ftp.snt.utwente.nl',],
['Liteserver', _('Netherlands'), 'http://mirror.liteserver.nl/pub/ubuntu/', 'mirror.liteserver.nl',],
['Eweka Internet Services BV', _('Netherlands'), 'http://ubuntuarchive.eweka.nl/ubuntu/', 'ubuntuarchive.eweka.nl',],
['Telfort', _('Netherlands'), 'http://ftp.telfort.nl/ubuntu/', 'ftp.telfort.nl',],
['Technische Universiteit Delft', _('Netherlands'), 'http://ftp.tudelft.nl/archive.ubuntu.com/', 'ftp.tudelft.nl',],
['mirrors.nl.eu.kernel.org', _('Netherlands'), 'http://mirrors.nl.eu.kernel.org/ubuntu/', 'mirrors.nl.eu.kernel.org',],
['PCextreme B.V.', _('Netherlands'), 'http://nl3.archive.ubuntu.com/ubuntu/', 'nl3.archive.ubuntu.com',],
['Rijksuniversiteit Groningen', _('Netherlands'), 'http://osmirror.rug.nl/ubuntu/', 'osmirror.rug.nl',],
['ftp.tiscali.nl-archive', _('Netherlands'), 'http://ubuntu.tiscali.nl/', 'ubuntu.tiscali.nl',],
['Ftpserv-tudelft-nl', _('Netherlands'), 'ftp://ftpserv.tudelft.nl/pub/Linux/archive.ubuntu.com/', 'ftpserv.tudelft.nl',],
['Nautile', _('New Caledonia'), 'http://ubuntu.nautile.nc/ubuntu/', 'ubuntu.nautile.nc',],
['Citylink', _('New Zealand'), 'http://ftp.citylink.co.nz/ubuntu/', 'ftp.citylink.co.nz',],
['Vodafone', _('New Zealand'), 'http://mirror.ihug.co.nz/ubuntu/', 'mirror.ihug.co.nz',],
['ihug', _('New Zealand'), 'http://nz2.archive.ubuntu.com/ubuntu/', 'nz2.archive.ubuntu.com',],
['UNINETT/University of Oslo', _('Norway'), 'http://ftp.uninett.no/ubuntu/', 'ftp.uninett.no',],
['The Student Society in Trondhjem, Norway', _('Norway'), 'http://no.archive.ubuntu.com/ubuntu/', 'no.archive.ubuntu.com',],
['University of Bergen', _('Norway'), 'http://ubuntu.uib.no/archive/', 'ubuntu.uib.no',],
['Web.com.ph Inc.', _('Philippines'), 'http://mirror.web.com.ph/ubuntu/', 'mirror.web.com.ph',],
['Wroclaw Centre for Networking and Supercomputing', _('Poland'), 'http://ftp.wcss.pl/ubuntu/', 'ftp.wcss.pl',],
['Vectra', _('Poland'), 'http://ftp.vectranet.pl/ubuntu/', 'ftp.vectranet.pl',],
['Ftp-man-szczecin-pl', _('Poland'), 'ftp://ftp.man.szczecin.pl/pub/Linux/ubuntu/', 'ftp.man.szczecin.pl',],
['Piotrkosoft.net - Data Storage Center', _('Poland'), 'http://piotrkosoft.net/pub/mirrors/ubuntu/', 'rsync.piotrkosoft.net',],
['Ubuntu-task-gda-pl', _('Poland'), 'http://ubuntu.task.gda.pl/ubuntu/', 'ubuntu.task.gda.pl',],
['Dep. de Ciência de Computadores - FCUP', _('Portugal'), 'http://ubuntu.dcc.fc.up.pt/', 'ubuntu.dcc.fc.up.pt',],
['University of Coimbra, Dep. Informatics Engineering', _('Portugal'), 'http://archive.ubuntumirror.dei.uc.pt/ubuntu/', 'archive.ubuntumirror.dei.uc.pt',],
['Rede das Novas Licenciaturas - Instituto Superior Técnico', _('Portugal'), 'http://ftp.rnl.ist.utl.pt/pub/ubuntu/archive/', 'ftp.rnl.ist.utl.pt',],
['nfsi telecom ', _('Portugal'), 'http://mirrors.nfsi.pt/ubuntu/', 'mirrors.nfsi.pt',],
['NEACM - University of Porto', _('Portugal'), 'http://neacm.fe.up.pt/ubuntu/', 'neacm.fe.up.pt',],
['sdAEIST', _('Portugal'), 'http://darkstar.ist.utl.pt/ubuntu/archive/', 'darkstar.ist.utl.pt',],
['DEIS-ISEC', _('Portugal'), 'http://deis-mirrors.isec.pt/ubuntu/', 'deis-mirrors.isec.pt',],
['GLUA', _('Portugal'), 'ftp://ftp.ua.pt/pub/ubuntu/', 'ftp.ua.pt',],
['Mosel ESTG-IPleiria', _('Portugal'), 'http://mosel.estg.ipleiria.pt/mirror/distros/ubuntu/archive/', 'mosel.estg.ipleiria.pt',],
['Carnegie Mellon - Qatar', _('Qatar'), 'http://ubuntu.qatar.cmu.edu/ubuntu/', 'ubuntu.qatar.cmu.edu',],
['West University of Timisoara', _('Romania'), 'http://ftp.info.uvt.ro/ubuntu/', 'ftp.info.uvt.ro',],
['Agency ARNIEC/RoEduNet', _('Romania'), 'http://ftp.roedu.net/mirrors/ubuntulinux.org/ubuntu/', 'ftp.roedu.net',],
['University POLITEHNICA of Bucharest', _('Romania'), 'http://mirror.pub.ro/ubuntu/', 'mirror.pub.ro',],
['UPC Romania', _('Romania'), 'http://ftp.astral.ro/mirrors/ubuntu.com/ubuntu/', 'ftp.astral.ro',],
['ArLUG (Arad Linux Users Group)', _('Romania'), 'http://mirror.arlug.ro/pub/ubuntu/ubuntu/', 'mirror.arlug.ro',],
['Romanian Linux Users Group', _('Romania'), 'http://ftp.gts.lug.ro/ubuntu/', 'ftp.gts.lug.ro',],
['Corbina Telecom', _('Russian Federation'), 'ftp://ftp.corbina.net/pub/Linux/ubuntu/', 'ftp.corbina.net',],
['COMSTAR-Direct', _('Russian Federation'), 'http://ftp.mtu.ru/pub/ubuntu/archive/', 'ftp.mtu.ru',],
['Golden Telecom Inc', _('Russian Federation'), 'http://mirror.rol.ru/ubuntu/', 'mirror.rol.ru',],
['Yandex', _('Russian Federation'), 'http://mirror.yandex.ru/ubuntu/', 'mirror.yandex.ru',],
['Corbina', _('Russian Federation'), 'http://mirror2.corbina.ru/ubuntu/', 'mirror2.corbina.ru',],
['Moscow Institute of Physics and Technology', _('Russian Federation'), 'ftp://ftp.mipt.ru/mirror/ubuntu/', 'ftp.mipt.ru',],
['Novosibirsk State University', _('Russian Federation'), 'http://linux.nsu.ru/ubuntu/', 'linux.nsu.ru',],
['Ftp-chg-ru', _('Russian Federation'), 'http://ftp.chg.ru/pub/Linux/ubuntu/archive/', 'ftp.chg.ru',],
['AlexAnis Home', _('Russian Federation'), 'http://89.148.222.236/ubuntu/', '89.148.222.236',],
['KACST/ISU', _('Saudi Arabia'), 'http://ubuntu.mirrors.isu.net.sa/ubuntu/', 'ubuntu.mirrors.isu.net.sa',],
['Institute of Physics Belgrade', _('Serbia'), 'http://rpm.scl.rs/linux/ubuntu/archive/', 'rpm.scl.rs',],
['RC ETF', _('Serbia'), 'http://ubuntu.etf.bg.ac.rs/ubuntu/', 'ubuntu.etf.bg.ac.rs',],
['ezNetworking Solutions Pte. Ltd.', _('Singapore'), 'http://ubuntu.oss.eznetsols.org/ubuntu/', 'rsync.oss.eznetsols.org',],
['ITU, Science, National University of Singapore', _('Singapore'), 'http://ftp.science.nus.edu.sg/ubuntu/', 'ftp.science.nus.edu.sg',],
['Nanyang Technological University Open Source Society', _('Singapore'), 'http://linux.ntuoss.org/ubuntu/', 'linux.ntuoss.org',],
['YNET & kubuntu.sk', _('Slovakia'), 'http://ubuntu.ynet.sk/ubuntu/', 'ubuntu.ynet.sk',],
['Antik computers & communications s.r.o.', _('Slovakia'), 'http://ftp.antik.sk/ubuntu/', 'ftp.antik.sk',],
['Energotel, a.s.', _('Slovakia'), 'http://ftp.energotel.sk/pub/linux/ubuntu/', 'rsync.energotel.sk',],
['Arnes', _('Slovenia'), 'http://ftp.arnes.si/pub/mirrors/ubuntu/', 'ftp.arnes.si',],
['lihnidos.org', _('Slovenia'), 'http://mirror.lihnidos.org/ubuntu/ubuntu/', 'mirror.lihnidos.org',],
['Telkom SAIX', _('South Africa'), 'http://ubuntu.saix.net/ubuntu-archive/', 'ftp.saix.net',],
['TENET', _('South Africa'), 'http://ubuntu.mirror.ac.za/ubuntu-archive/', 'ubuntu.mirror.ac.za',],
['UCT LEG', _('South Africa'), 'http://ftp.leg.uct.ac.za/ubuntu/', 'ftp.leg.uct.ac.za',],
['CICA', _('Spain'), 'http://ubuntu.cica.es/ubuntu/', 'ubuntu.cica.es',],
['Universidade da Coruña', _('Spain'), 'http://ftp.udc.es/ubuntu/', 'rsync.udc.es',],
['Ourense Software Libre', _('Spain'), 'http://mirror.ousli.org/ubuntu/', 'mirror.ousli.org',],
['Universidad Rey Juan Carlos - ETSIT - Dpto Sistemas Telemáticos y Computación', _('Spain'), 'http://peloto.pantuflo.es/ubuntu/', 'peloto.pantuflo.es',],
['Universidad de Zaragoza', _('Spain'), 'http://softlibre.unizar.es/ubuntu/archive/', 'softlibre.unizar.es',],
['RedIRIS', _('Spain'), 'http://sunsite.rediris.es/mirror/ubuntu-archive/', 'ftp.rediris.es',],
['Universidad Carlos III de Madrid - Oficina de Software Libre', _('Spain'), 'http://ubuntu.uc3m.es/ubuntu/', 'ubuntu.uc3m.es',],
['DAFI de la Universidad de Murcia', _('Spain'), 'http://dafi.inf.um.es/ubuntu/', 'dafi.inf.um.es',],
['Grupo Universitario de Informática', _('Spain'), 'http://ftp.gui.uva.es/sites/ubuntu.com/ubuntu/', 'ftp.gui.uva.es',],
['Caliu', _('Spain'), 'http://ftp.caliu.cat/pub/distribucions/ubuntu/archive/', 'ftp.caliu.cat',],
['Delegación de Alumnos de Teleco - ETSIT - UPM', _('Spain'), 'http://ftp.dat.etsit.upm.es/ubuntu/', 'ftp.dat.etsit.upm.es',],
['GRN Serveis telemàtics', _('Spain'), 'http://ubuntu.grn.cat/ubuntu/', 'ubuntu.grn.cat',],
['SchoolNet - Sri Lanka (under Ministry of Education)', _('Sri Lanka'), 'http://archive.ubuntu.schoolnet.lk/ubuntu/', 'archive.ubuntu.schoolnet.lk',],
['Academic Computer Club, Umeå University', _('Sweden'), 'http://se.archive.ubuntu.com/ubuntu/', 'se.archive.ubuntu.com',],
['SUNET', _('Sweden'), 'http://ftp.sunet.se/pub/os/Linux/distributions/ubuntu/ubuntu/', 'ftp.sunet.se',],
['DF - The Computer Society at the Lund Institute of Technology. ', _('Sweden'), 'http://ftp.df.lth.se/ubuntu/', 'ftp.df.lth.se',],
['DatorSektionen Högskolan Jönköping', _('Sweden'), 'http://ftp.ds.karen.hj.se/ubuntu/', 'ftp.ds.karen.hj.se',],
['mirrors.se.eu.kernel.org', _('Sweden'), 'http://mirrors.se.eu.kernel.org/ubuntu/', 'mirrors.se.eu.kernel.org',],
['Stockholm University', _('Sweden'), 'http://ubuntu.mirror.su.se/ubuntu/', 'ubuntu.mirror.su.se',],
['Port80', _('Sweden'), 'http://ftp.port80.se/ubuntu/', 'rsync.port80.se',],
['SWITCH', _('Switzerland'), 'http://mirror.switch.ch/ftp/mirror/ubuntu/', 'mirror.switch.ch',],
['NCHC, Taiwan', _('Taiwan'), 'http://free.nchc.org.tw/ubuntu/', 'free.nchc.org.tw',],
['NCTUCC', _('Taiwan'), 'http://debian.nctu.edu.tw/ubuntu/', 'debian.nctu.edu.tw',],
['Chung-Hua University', _('Taiwan'), 'ftp://ftp.chu.edu.tw/Linux/Ubuntu/archives/', 'ftp.chu.edu.tw',],
['Providence University , CCI', _('Taiwan'), 'http://ftp.cs.pu.edu.tw/Linux/Ubuntu/ubuntu/', 'ftp.cs.pu.edu.tw',],
[' Yuan Ze University Department of Computer Science', _('Taiwan'), 'http://ftp.cse.yzu.edu.tw/pub/Linux/Ubuntu/ubuntu/', 'ftp.cse.yzu.edu.tw',],
['NCHU', _('Taiwan'), 'http://ftp.nchu.edu.tw/Linux/Ubuntu/', 'ftp.nchu.edu.tw',],
['TaiChung County Education Network Center', _('Taiwan'), 'http://ftp.tcc.edu.tw/Linux/ubuntu/', 'ftp.tcc.edu.tw',],
['TKU-TamKangUniversity', _('Taiwan'), 'http://ftp.tku.edu.tw/ubuntu/', 'ftp.tku.edu.tw',],
['National Center for High-Performance Computing(NCHC)', _('Taiwan'), 'http://ftp.twaren.net/Linux/Ubuntu/ubuntu/', 'ftp.twaren.net',],
['National Taitung University', _('Taiwan'), 'http://mirror.nttu.edu.tw/ubuntu/', 'mirror.nttu.edu.tw',],
['National Taiwan University', _('Taiwan'), 'http://tw.archive.ubuntu.com/ubuntu/', 'tw.archive.ubuntu.com',],
['NCTUCSCC', _('Taiwan'), 'http://ubuntu.cs.nctu.edu.tw/ubuntu/', 'ubuntu.cs.nctu.edu.tw',],
['Shu-Te University', _('Taiwan'), 'http://ubuntu.stu.edu.tw/ubuntu/', 'ubuntu.stu.edu.tw',],
['National Chi Nan University', _('Taiwan'), 'http://ftp.ncnu.edu.tw/Linux/ubuntu/ubuntu/', 'ftp.ncnu.edu.tw',],
['TAIWAN MIRROR', _('Taiwan'), 'http://www.mirror.tw/pub/ubuntu/ubuntu/', 'ftp.mirror.tw',],
['Office of Computer Services, Kasetsart University', _('Thailand'), 'http://mirror1.ku.ac.th/ubuntu/', 'mirror1.ku.ac.th',],
['Thai National Mirror', _('Thailand'), 'http://mirror.in.th/osarchive/ubuntu/', 'mirror.in.th',],
['School of Information Technology, KMUTT', _('Thailand'), 'http://ubuntu-archive.sit.kmutt.ac.th/', 'ubuntu-archive.sit.kmutt.ac.th',],
['Ankara Universitesi', _('Turkey'), 'http://ftp.ankara.edu.tr/ubuntu/', 'ftp.ankara.edu.tr',],
['Linux Kullanicilari Dernegi', _('Turkey'), 'http://ftp.linux.org.tr/ubuntu/', 'ftp.linux.org.tr',],
['Middle East Technical University', _('Turkey'), 'http://ftp.metu.edu.tr/ubuntu/', 'ftp.metu.edu.tr',],
['Bilgi University', _('Turkey'), 'http://russell.cs.bilgi.edu.tr/ubuntu/', 'russell.cs.bilgi.edu.tr',],
['Turkey GNU Organization', _('Turkey'), 'http://ubuntu.gnu.gen.tr/ubuntu/', 'ubuntu.gnu.gen.tr',],
['Mirohost.net', _('Ukraine'), 'http://mirror.mirohost.net/ubuntu/', 'mirror.mirohost.net',],
['www.dnepr.com', _('Ukraine'), 'http://mirrors.dnepr.com/pub/mirrors/ubuntu/', 'mirrors.dnepr.com',],
['XCP + HELL', _('Ukraine'), 'http://ubuntu.org.ua/ubuntu/', 'ubuntu.org.ua',],
['University Of Kent UK Mirror Service', _('United Kingdom'), 'http://www.mirrorservice.org/sites/archive.ubuntu.com/ubuntu/', 'rsync.mirrorservice.org',],
['Bytemark Hosting', _('United Kingdom'), 'http://mirror.bytemark.co.uk/ubuntu/', 'mirror.bytemark.co.uk',],
['Ticklers.org', _('United Kingdom'), 'http://ftp.ticklers.org/archive.ubuntu.org/ubuntu/', 'ftp.ticklers.org',],
['XILO Communications Ltd.', _('United Kingdom'), 'http://mirror.as29550.net/archive.ubuntu.com/', 'mirror.as29550.net',],
['Oxford University Computing Services', _('United Kingdom'), 'http://mirror.ox.ac.uk/sites/archive.ubuntu.com/ubuntu/', 'mirror.ox.ac.uk',],
['Goscomb Technologies Limited', _('United Kingdom'), 'http://mirror.sov.uk.goscomb.net/ubuntu/', 'mirror.sov.uk.goscomb.net',],
['Datahop Ltd.', _('United Kingdom'), 'http://ubuntu.datahop.net/ubuntu/', 'ubuntu.datahop.net',],
['Canonical Ltd.', _('United Kingdom'), 'http://archive.ubuntu.com/ubuntu/', 'archive.ubuntu.com',],
['The Positive Internet Company', _('United Kingdom'), 'http://ubuntu.positive-internet.com/ubuntu/', 'ubuntu.positive-internet.com',],
['Retrosnub Internet Services', _('United Kingdom'), 'http://ubuntu.retrosnub.co.uk/ubuntu/', 'ubuntu.retrosnub.co.uk',],
['Virgin Media', _('United Kingdom'), 'http://ubuntu.virginmedia.com/archive/', 'mirrors.virginmedia.com',],
['Argonne National Laboratory', _('United States'), 'http://mirror.anl.gov/pub/ubuntu/', 'mirror.anl.gov',],
['FDCServers.net LLC', _('United States'), 'http://76.73.4.58/ubuntu/', '76.73.4.58',],
['University of Chicago - Astronomy Department Public Mirror', _('United States'), 'http://astromirror.uchicago.edu/ubuntu/', 'astromirror.uchicago.edu',],
['Michigan State University College of Engineering', _('United States'), 'ftp://ftp.egr.msu.edu/pub/ubuntu/archive/', 'ftp.egr.msu.edu',],
['University of South Florida', _('United States'), 'http://ftp.usf.edu/pub/ubuntu/', 'ftp.usf.edu',],
['Portland State University', _('United States'), 'http://mirrors.cat.pdx.edu/ubuntu/', 'mirrors.cat.pdx.edu',],
['Northeastern University College of Computer Science', _('United States'), 'http://mirrors.ccs.neu.edu/ubuntu/', 'ftp.ccs.neu.edu',],
['Easynews', _('United States'), 'http://mirrors.easynews.com/linux/ubuntu/', 'mirrors.easynews.com:',],
['Rochester Institute of Technology', _('United States'), 'http://mirrors.rit.edu/ubuntu/', 'mirrors.rit.edu',],
['mirrors.us.kernel.org', _('United States'), 'http://mirrors.us.kernel.org/ubuntu/', 'mirrors.us.kernel.org',],
['Xmission', _('United States'), 'http://mirrors.xmission.com/ubuntu/', 'mirrors.xmission.com',],
['TDS Internet Services', _('United States'), 'http://ubuntu.mirrors.tds.net/pub/ubuntu/', 'ubuntu.mirrors.tds.net',],
['MIT Media Lab', _('United States'), 'http://ubuntu.media.mit.edu/ubuntu/', 'ubuntu.media.mit.edu',],
['UUNET Customer Security Support', _('United States'), 'http://ubuntu.secsup.org/', 'ubuntu.secsup.org',],
['Walla Walla University', _('United States'), 'http://ubuntu.wallawalla.edu/ubuntu/', 'ftp.wallawalla.edu',],
['Wikimedia Foundation', _('United States'), 'http://ubuntu.wikimedia.org/ubuntu/', 'ubuntu.wikimedia.org',],
['University of Minnesota Ubuntu Archive', _('United States'), 'http://mirror.cs.umn.edu/ubuntu/', 'mirror.cs.umn.edu',],
['Carnegie Mellon Computer Club', _('United States'), 'http://www.club.cc.cmu.edu/pub/ubuntu/', 'www.club.cc.cmu.edu',],
['Georgia Tech. Software Library', _('United States'), 'http://www.gtlib.gatech.edu/pub/ubuntu/', 'rsync.gtlib.gatech.edu',],
['Duke University', _('United States'), 'http://archive.linux.duke.edu/ubuntu/', 'archive.linux.duke.edu',],
['Michigan Tech Linux Users\' Group', _('United States'), 'http://lug.mtu.edu/ubuntu/', 'lug.mtu.edu',],
['University of Tennessee', _('United States'), 'http://mira.sunsite.utk.edu/ubuntu/', 'mira.sunsite.utk.edu',],
['Clarkson University', _('United States'), 'http://mirror.clarkson.edu/pub/ubuntu/', 'mirror.clarkson.edu',],
['Columbia University', _('United States'), 'http://mirror.cc.columbia.edu/pub/linux/ubuntu/archive/', 'mirror.cc.columbia.edu',],
['HOSEF', _('United States'), 'http://mirror.hosef.org/ubuntu/', 'mirror.hosef.org',],
['University of Idaho', _('United States'), 'http://mirror.its.uidaho.edu/pub/ubuntu/', 'mirror.its.uidaho.edu',],
['Telus', _('United States'), 'http://mirror.peer1.net/ubuntu/', 'mirror.peer1.net',],
['University of Maryland', _('United States'), 'http://mirror.umoss.org/ubuntu/', 'mirror.umoss.org',],
['JHU ACM', _('United States'), 'http://mirrors.acm.jhu.edu/ubuntu/', 'mirrors.acm.jhu.edu',],
['Cavecreek Web Hosting', _('United States'), 'http://mirrors.cavecreek.net/ubuntu/', 'mirrors.cavecreek.net',],
['Pavlov Media', _('United States'), 'http://mirrors.pavlovmedia.net/ubuntu/', 'mirrors.pavlovmedia.net',],
['University of California at Merced', _('United States'), 'http://samaritan.ucmerced.edu/ubuntu/', 'samaritan.ucmerced.edu',],
['Washington State University', _('United States'), 'http://ubuntu.eecs.wsu.edu/', 'ubuntu.eecs.wsu.edu',],
['Frontier Communications', _('United States'), 'http://ubuntu.mirror.frontiernet.net/ubuntu/', 'ubuntu.mirror.frontiernet.net',],
['OSU Open Source Lab', _('United States'), 'http://ubuntu.osuosl.org/ubuntu/', 'ubuntu.osuosl.org',],
['Secured Servers LLC', _('United States'), 'http://ubuntu.securedservers.com/', 'ubuntu.securedservers.com',],
['Boston University Linux Users Group', _('United States'), 'http://www.lug.bu.edu/mirror/ubuntu/', 'ftp.lug.bu.edu',],
['Clarkson University', _('United States'), 'http://mirror.clarkson.edu/ubuntu/', 'mirror.clarkson.edu',],
['WVU LCSEE', _('United States'), 'http://mirror.lcsee.wvu.edu/ubuntu/', 'mirror.lcsee.wvu.edu',],
['University of California at Davis', _('United States'), 'http://mirror.math.ucdavis.edu/ubuntu/', 'mirror.math.ucdavis.edu',],
['Bloomsburg University', _('United States'), 'http://mirrors.bloomu.edu/ubuntu/', 'mirrors.bloomu.edu',],
['Indiana University', _('United States'), 'http://ftp.ussg.iu.edu/linux/ubuntu/', 'ftp.ussg.iu.edu',],
['The University of Texas at Austin', _('United States'), 'http://ftp.utexas.edu/ubuntu/', 'ftp.utexas.edu',],
['Computer Science at WMU', _('United States'), 'http://mirrors.cs.wmich.edu/ubuntu/', 'mirrors.cs.wmich.edu',],
['University of Utah', _('United States'), 'http://ubuntu.cs.utah.edu/ubuntu/', 'ubuntu.cs.utah.edu',],
['Oakland University', _('United States'), 'http://ubuntu.secs.oakland.edu/', 'ubuntu.secs.oakland.edu',],
['Sharq Telekom', _('Uzbekistan'), 'http://ubuntu.uz/ubuntu/', 'ubuntu.uz',],
['FPT Telecom', _('Viet Nam'), 'http://mirror-fpt-telecom.fpt.net/ubuntu/', 'mirror-fpt-telecom.fpt.net',],
]
    
def _g2():
    return [ 
['Shanghai Jiao Tong University', _('China'), 'http://ftp.sjtu.edu.cn/ubuntu/', 'ftp.sjtu.edu.cn', ],
['University of Science and Technology', _('China'), 'http://debian.ustc.edu.cn/ubuntu/', 'debian.ustc.edu.cn', ],
['LUPA', _('China'), 'http://mirror.lupaworld.com/ubuntu/', 'mirror.lupaworld.com', ],
['Rootguide', _('China'), 'http://mirror.rootguide.org/ubuntu/', 'mirror.rootguide.org', ],
['Shanghai Linux User Group', _('China'), 'http://cn.archive.ubuntu.com/ubuntu/', 'mirrors.shlug.org', ],
['CN99', _('China'), 'http://ubuntu.cn99.com/ubuntu/', 'ubuntu.cn99.com', ],
['University of Electronic Science and Technology', _('China'), 'http://ubuntu.uestc.edu.cn/ubuntu/', 'ubuntu.uestc.edu.cn', ],
['Netease', _('China'), 'http://mirrors.163.com/ubuntu/', 'mirrors.163.com', ],
['Sohu', _('China'), 'http://mirrors.sohu.com/ubuntu/', 'mirrors.sohu.com', ],
['University of Geosciences', _('China'), 'http://www.tofree.org/ubuntu/', 'www.tofree.org', ],
['National Taiwan University', _('Taiwan'), 'http://ubuntu.csie.ntu.edu.tw/', 'ubuntu.csie.ntu.edu.tw', ],
['Beijing Jiao Tong University', _('China'), 'http://mirror.bjtu.edu.cn/ubuntu/', 'mirror.bjtu.edu.cn', ],
['Ubuntu Repository @ Peru', _('Peru'), 'http://pe.archive.ubuntu.com/ubuntu/', 'pe.archive.ubuntu.com', ],
['Ubuntu Repository @ Ghana', _('Ghana'), 'http://gh.archive.ubuntu.com/ubuntu/', 'gh.archive.ubuntu.com', ],
['Alfred State College', _('United States'), 'http://mirror.alfredstate.edu/ubuntu/', 'mirror.alfredstate.edu', ],
]

def get_candidate_repositories():
    ret = []
    
    all_servers = set()
    for e in _g1() + _g2():
        assert len(e) ==4
        assert '://' in e[2]
        assert '.' in e[3], e
        server = e[3]
        if not server in all_servers:
            all_servers.add(server)
            ret.append(e)
    
    return ret

def get_current_official_repositories():
    'Return the official repositories currently in use'

    version = Config.get_Ubuntu_version()
    s1 = ' %s-backports ' % version
    s2 = ' %s-proposed ' % version
    s3 = ' %s-security ' % version
    s4 = ' %s-updates ' % version

    repos = set()
    
    for file in APTSource.apt_source_files_list():
        with open(file) as f:
            for line in f:
                # skip blank lines or comments
                line = line.split('#')[0].strip()
                if len(line)==0: continue
                # get server
                import re
                match = re.match(r'^deb(-src)? [a-z]+://([^/]+)/.*$', line)
                if match:
                    server = match.group(2)
                    if server.endswith('archive.ubuntu.com'):
                        repos.add(line.split()[1])
                    elif (s1 in line) or (s2 in line) or (s3 in line) or (s4 in line): 
                        repos.add(line.split()[1])
                    
    return repos

def get_all_current_repositories():
    'Return all repositories currently in use. For example, Launchpad.'

    repos = set()
    
    for file in APTSource.apt_source_files_list():
        with open(file) as f:
            for line in f:
                # skip blank lines or comments
                line = line.split('#')[0].strip()
                if len(line)==0: continue
                # get server
                import re
                match = re.match(r'^deb(-src)? [a-z]+://([^/]+)/.*$', line)
                if match:
                    repos.add(line.split()[1])
                    
    return repos

def change_repositories_in_source_files(changes):
    'Input a dict: old_server->new_url'
    'Change servers in all source files'

    if not isinstance(changes, dict): raise TypeError
    for key, value in changes.items():
        is_string_not_empty(key)
        assert ':' in key
        is_string_not_empty(value)
        assert ':' in value
    
    for file in APTSource.apt_source_files_list():
        # read content
        with open(file) as f:
            contents = f.readlines()
            
        # do replacement
        changed = False
        for i, line in enumerate(contents):
            # skip blank lines and commented lines
            line = line.split('#', 1)[0].strip()
            if len(line)==0: continue
            for old, new in changes.items():
                if old in line:
                    list = line.split(' ', 3)
                    list[1] = new
                    contents[i] = ' '.join(list)+'\n'
                    changed = True
                    break
        
        # write back
        if changed:
            with TempOwn(file) as o:
                with open(file, 'w') as f:
                    f.writelines(contents)
