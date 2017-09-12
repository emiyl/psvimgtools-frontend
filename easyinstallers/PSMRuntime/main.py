
import os
import shutil
import tkMessageBox

import defs
from easyinstallers.PSMRuntime import signTo


def run():
    CMA = defs.getCmaDir()
    if not os.path.exists(CMA + "/EXTRACTED/APP/PCSI00011"):
        shutil.copytree(defs.getWorkingDir() + "/easyinstallers/PSMRuntime/PCSI00011", CMA + "/EXTRACTED/APP/PCSI00011")
    signTo.vp_start_gui()


