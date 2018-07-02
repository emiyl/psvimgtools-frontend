

import sys
import webbrowser
import tkMessageBox

from os.path import expanduser

from account import *

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
import defs




def auto():
    defs.autoAccount()
    import account
    account.close_window(root)
    defs.showMessage(title="Account Reigstered.",message="Account Registered")
    import accMgr
    accMgr.vp_start_gui()
    sys.stdout.flush()


def addaccount(aid, acc):
    if aid == "" and acc != "" and acc.find(',') == -1:
        defs.showMessage(title="Error 001", message="Please enter your AID.")

    if acc == "" and aid != "" and aid.find(',') == -1:
        defs.showMessage(title="Error 002", message="Please enter Your Account Name")

    if acc == "" and aid == "":
        defs.showMessage(title="Error 003", message="Please enter Your Account Name And your AID.")

    if len(aid) == 16:
        if acc != "" and aid != "" and acc.find(',') == -1:

            text_file = open("accounts/" +acc, "w+")
            text_file.write(aid)
            text_file.close()

            import urllib
            urllib.urlretrieve("http://cma.henkaku.xyz/?aid=" + aid, "tempKey.html")
            text_file = open("keys/"+acc,"w+")
            text_file.write(defs.getKey())
            text_file.close()

            import account
            account.close_window(root)
            defs.showMessage(title="Thank You!", message="Account: " + acc + " [" + aid + "] Was Registered.")
            import accMgr
            accMgr.vp_start_gui()

    sys.stdout.flush()


def question():
    defs.showMessage(title="CMA Key",message="Your AID is the name of the random numbers and letters folder your CMA backups are stored in.")
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
    import account

    account.vp_start_gui()



