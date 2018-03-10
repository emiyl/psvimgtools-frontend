
import os
import shutil
import defs
from easyinstallers.VitaShell import signTo


def run():
    CMA = defs.getCmaDir()
    if not os.path.exists(CMA + "/EXTRACTED/APP/VITASHELL"):
        shutil.copytree(defs.getWorkingDir()+"/easyinstallers/VitaShell/VITASHELL" , CMA + "/EXTRACTED/APP/VITASHELL")
    signTo.vp_start_gui()


