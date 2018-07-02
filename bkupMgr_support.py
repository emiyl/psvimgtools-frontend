


import sys

import backupType
import backupType_support

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


def cmaDir():
    import cmaDir
    cmaDir.vp_start_gui()
    sys.stdout.flush()

def reSign():
    import backupType
    import backupType_support
    backupType_support.action("resign")
    backupType.vp_start_gui()
    sys.stdout.flush()

def sign():
    import backupType
    import backupType_support
    backupType_support.action("sign")
    backupType.vp_start_gui()
    sys.stdout.flush()

def unsign():
    import backupType
    import backupType_support
    backupType_support.action("unsign")
    backupType.vp_start_gui()
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
    import bkupMgr
    bkupMgr.vp_start_gui()


