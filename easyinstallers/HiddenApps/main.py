
import os
import shutil
import tkMessageBox

import defs

def run():
    CMA = defs.getCmaDir()
    if not os.path.exists(CMA + "/EXTRACTED/APP/HIDENAPPS"):
        shutil.copytree(defs.getWorkingDir()+"/easyinstallers/HiddenApps/HIDENAPPS" , CMA + "/EXTRACTED/APP/HIDENAPPS")
    import easyinstallers.HiddenApps.signTo as signTo
    signTo.vp_start_gui()


