
import os
import shutil
import tkMessageBox

import defs

def run():
    CMA = defs.getCmaDir()
    if not os.path.exists(CMA + "/EXTRACTED/APP/PCSI00011"):
        shutil.copytree(defs.getWorkingDir() + "/easyinstallers/PSMRuntime/PCSI00011", CMA + "/EXTRACTED/APP/PCSI00011")
    import easyinstallers.PSMRuntime.signTo as signTo
    signTo.vp_start_gui()


