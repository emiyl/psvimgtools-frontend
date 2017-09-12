


import sys

import shutil
import tkMessageBox

import defs


def createBackup(emulator,backup,account):
    print emulator,account,backup
    import unsign_support
    unsign_support.goUnsign(cmaBackup=backup,account=account,load="PGAME",resign=".")
    from distutils.dir_util import copy_tree
    print "Copying "+defs.getWorkingDir()+"/easyinstallers/EmuBubble/FILES/"+emulator+" To "+defs.getCmaDir()+"/EXTRACTED/PGAME/"+backup+"/game/ux0_pspemu_temp_game_PSP_GAME_"+backup+"/"
    copy_tree(defs.getWorkingDir()+"/easyinstallers/EmuBubble/FILES/"+emulator,defs.getCmaDir()+"/EXTRACTED/PGAME/"+backup+"/game/ux0_pspemu_temp_game_PSP_GAME_"+backup+"/")
    import sign_support
    sign_support.goSign(account,"PGAME",backup,True)
    print "Removing: "+defs.getCmaDir()+"/EXTRACTED/PGAME/"+backup
    shutil.rmtree(defs.getCmaDir()+"/EXTRACTED/PGAME/"+backup+"/")
    tkMessageBox.showinfo(title="Emulator Bubble",message=emulator+" Backup Created! (remember to refresh QCMA)")
    emububble.destroy_New_Toplevel_1()
    import easyinstallers.EmuBubble.chooseBackup as CB
    CB.destroy_Unsign_Backup()


def folder(dir):
    defs.openFolder(defs.getWorkingDir()+"/easyinstallers/EmuBubble/FILES/"+dir)

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import emububble
    emububble.vp_start_gui()


