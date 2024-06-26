#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi")
    shelltools.system("./autogen.sh")
    autotools.configure()

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")
