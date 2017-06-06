import os
import sys
import tkMessageBox

import shutil
from random import randint

import defs

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


def random(oldTitleId2,account):
    print "Generating Random TitleID"
    newTitleId2="PSVIM"+str(randint(1111,9999))
    print "TitleID: "+newTitleId2
    set(newTitleId2,oldTitleId2,account)
    sys.stdout.flush()

def set(newTitleId,oldTitleId,account):
    newTitleId = str(newTitleId).upper()
    if len(newTitleId) != 9:
        tkMessageBox.showerror(title="Length Error",message="The TitleID you entered is NOT 9 characters Long.")
        sys.exit()
    if not defs.doesStringContain("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",newTitleId):
        tkMessageBox.showerror(title="Character Error",message="The TitleID contains an invalid character")
        sys.exit()
    with open(defs.getCmaDir()+'/EXTRACTED/PGAME/'+oldTitleId+"/sce_sys/param.sfo", 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(oldTitleId, newTitleId)
    with open(defs.getCmaDir()+'/EXTRACTED/PGAME/'+oldTitleId+"/sce_sys/param.sfo", 'w') as file:
        file.write(filedata)
    print "param.sfo Patched"

    with open(defs.getCmaDir()+'/EXTRACTED/PGAME/'+oldTitleId+"/game/ux0_pspemu_temp_game_PSP_GAME_"+oldTitleId+"/VITA_PATH.TXT", 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(oldTitleId, newTitleId)
    with open(defs.getCmaDir()+'/EXTRACTED/PGAME/'+oldTitleId+"/game/ux0_pspemu_temp_game_PSP_GAME_"+oldTitleId+"/VITA_PATH.TXT", 'w') as file:
        file.write(filedata)
    print "VITA_PATH.TXT Patched"

    os.rename(defs.getCmaDir()+'/EXTRACTED/PGAME/'+oldTitleId+"/game/ux0_pspemu_temp_game_PSP_GAME_"+oldTitleId,defs.getCmaDir()+'/EXTRACTED/PGAME/'+oldTitleId+"/game/ux0_pspemu_temp_game_PSP_GAME_"+newTitleId)
    print "ux0_pspemu_temp_game_PSP_GAME_"+oldTitleId+" Renamed to "+"ux0_pspemu_temp_game_PSP_GAME_"+newTitleId

    os.rename(defs.getCmaDir()+'/EXTRACTED/PGAME/'+oldTitleId,defs.getCmaDir()+'/EXTRACTED/PGAME/'+newTitleId)
    print oldTitleId+" Renamed to "+newTitleId

    print "Patching Complete.."
    print "Signing.."
    import sign_support
    sign_support.goSign(acc=account,ld="PGAME",bkup=newTitleId,resign=True)
    print "Removing... "+defs.getCmaDir()+'/EXTRACTED/PGAME/'+newTitleId
    shutil.rmtree(defs.getCmaDir()+'/EXTRACTED/PGAME/'+newTitleId)
    destroy_window()
    tkMessageBox.showinfo(title="Done!",message="PSP Bubble Cloned with TitleID "+newTitleId)
    sys.stdout.flush()

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
    import clone
    clone.vp_start_gui()


