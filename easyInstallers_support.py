
import tkMessageBox
import defs
import easyinstallers.Whitelister.main as Whitelister
import easyinstallers.ARK.main as ARK
import easyinstallers.HiddenApps.main as HiddenApps
import easyinstallers.VHBL.main as VHBL
import easyinstallers.UriCaller.main as UriCaller
import easyinstallers.PSMRuntime.main as PSMRuntime
import easyinstallers.Skype.main as Skype
import easyinstallers.RemoveFeatured.main as RemoveFeatured
import easyinstallers.CmBackup.main as cmbackup
import easyinstallers.EmuBubble.main as emububble
import easyinstallers.ClonePSP.main as clonePSP
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

def set_Tk_var():
    global accounts
    accounts = StringVar()


def install(plugin):
    if plugin == 'ARK':
        if tkMessageBox.askyesno(title="3.65?",message="ARK WILL NOT WORK ON 3.65+\nDo you still want to continue?"):
                ARK.vp_start_gui()
    elif plugin == 'VHBL':
        VHBL.vp_start_gui()
    elif plugin == 'HiddenApps':
        HiddenApps.run()
    elif plugin == 'Whitelister':
        Whitelister.vp_start_gui()
    elif plugin == 'UriCaller':
        UriCaller.vp_start_gui()
    elif plugin == 'PSMRuntime':
        PSMRuntime.run()
    elif plugin == 'Skype':
        if tkMessageBox.askyesno(title="3.65?",message="SKYPE WILL NOT WORK ON 3.65+\nDo you still want to continue?"):
                Skype.run()
    elif plugin == 'RemoveFeatured':
        RemoveFeatured.vp_start_gui()
    elif plugin == 'CmBackup':
        cmbackup.vp_start_gui()
    elif plugin == 'EmuBubble':
        emububble.vp_start_gui()
    elif plugin == 'ClonePSP':
        clonePSP.vp_start_gui()

    else:
        ### Load Custom EasyInstaller. ###
        defs.executePy(defs.getWorkingDir()+'/easyinstallers/'+plugin+'/main.py')

    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global root
    global w
    global top_level
    w = gui
    top_level = top
    root = top


def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import easyInstallers
    easyInstallers.vp_start_gui()

