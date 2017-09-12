
import os
import shutil
import tkMessageBox

import defs
from easyinstallers.HiddenApps import signTo


def run():
    CMA = defs.getCmaDir()
    if not os.path.exists(CMA + "/EXTRACTED/APP/HIDENAPPS"):
        shutil.copytree(defs.getWorkingDir()+"/easyinstallers/HiddenApps/HIDENAPPS" , CMA + "/EXTRACTED/APP/HIDENAPPS")
    signTo.vp_start_gui()


