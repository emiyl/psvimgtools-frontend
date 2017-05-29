
import os
import sys

import tkMessageBox
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
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global accounts
    accounts = StringVar()






def edAcc(edAcc):
    if edAcc == "":
        import accMgr
        accMgr.close_window(root)
        tkMessageBox.showinfo(title="Error 006", message="You have no accounts!")
        accMgr.vp_start_gui()
    import accMgr
    accMgr.close_window(root)
    os.remove("accounts/"+edAcc)
    os.remove("keys/"+edAcc)
    import account
    account.vp_start_gui()
    sys.stdout.flush()


def addAcc():
    import account
    import accMgr
    accMgr.close_window(root)
    account.vp_start_gui()
    sys.stdout.flush()

def rmAcc(rmAcc):
    if rmAcc == "":
        import accMgr
        accMgr.close_window(root)
        tkMessageBox.showinfo(title="Error 005", message="You have no accounts!")
        accMgr.vp_start_gui()
    import accMgr
    accMgr.close_window(root)
    os.remove("accounts/"+rmAcc)
    os.remove("keys/"+rmAcc)
    accMgr.vp_start_gui()
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
    import accMgr
    accMgr.vp_start_gui()





