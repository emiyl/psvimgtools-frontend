
import os
import shutil
import defs
from easyinstallers.hencore import signTo


def run():
    CMA = defs.getCmaDir()
    if not os.path.exists(CMA + "/EXTRACTED/APP/PCSG90096"):
        shutil.copytree(defs.getWorkingDir()+"/easyinstallers/hencore/PCSG90096" , CMA + "/EXTRACTED/APP/PCSG90096")
    signTo.vp_start_gui()


