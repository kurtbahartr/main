#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.system("python3 -m build --wheel --no-isolation backend")
    # python3modules.compile("backend")

def install():
    shelltools.system("python3 -m installer --destdir=%s backend/dist/*.whl" % get.installDIR())
    # python3modules.install("backend")

    # pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README")
