

import sys

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


def accMan():
    import accMgr
    accMgr.vp_start_gui()
    sys.stdout.flush()

def bkupMgr():
    import bkupMgr
    bkupMgr.vp_start_gui()
    sys.stdout.flush()

def esyInstall():
    import easyInstallers
    easyInstallers.vp_start_gui()
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
    import main
    main.vp_start_gui()


