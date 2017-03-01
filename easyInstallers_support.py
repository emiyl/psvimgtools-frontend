
import fnmatch
import os
import sys
from symbol import import_from
import defs
import easyinstallers.ARK.main as ARK
import easyinstallers.HiddenApps.main as HiddenApps
import easyinstallers.VHBL.main as VHBL
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
        ARK.vp_start_gui()
    elif plugin == 'VHBL':
        VHBL.vp_start_gui()
    elif plugin == 'HiddenApps':
        HiddenApps.run()
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

