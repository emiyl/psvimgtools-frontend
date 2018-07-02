


import accSelect
import accSelect_support
import sign
import sign_support
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

def action(ImportType):
    global x
    x = ImportType

def getImportType():
    return x




def psm():
    if x == "unsign":
        accSelect_support.loadPSM()
        accSelect.vp_start_gui()

    elif x == "sign":
        sign_support.loadPSM()
        sign.vp_start_gui()
    elif x == "resign":
        accSelect_support.loadPSM()
        accSelect.vp_start_gui()
    sys.stdout.flush()

def psone():
    if x == "unsign":
        accSelect_support.loadPSOne()
        accSelect.vp_start_gui()

    elif x == "sign":
        sign_support.loadPSOne()
        sign.vp_start_gui()
    elif x == "resign":
        accSelect_support.loadPSOne()
        accSelect.vp_start_gui()
    sys.stdout.flush()


def psp():
    if x == "unsign":
        accSelect_support.loadPSP()
        accSelect.vp_start_gui()

    elif x == "sign":
        sign_support.loadPSP()
        sign.vp_start_gui()
    elif x == "resign":
        accSelect_support.loadPSP()
        accSelect.vp_start_gui()
    sys.stdout.flush()


def psv():
    if x == "unsign":
        accSelect_support.loadPSV()
        accSelect.vp_start_gui()

    elif x == "sign":
        sign_support.loadPSV()
        sign.vp_start_gui()

    elif x == "resign":
        accSelect_support.loadPSV()
        accSelect.vp_start_gui()
    sys.stdout.flush()




def system():
    if x == "unsign":
        accSelect_support.loadSYS()
        accSelect.vp_start_gui()

    elif x == "sign":
        sign_support.loadSYS()
        sign.vp_start_gui()

    elif x == "resign":
        accSelect_support.loadSYS()
        accSelect.vp_start_gui()
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
    import backupType
    backupType.vp_start_gui()


