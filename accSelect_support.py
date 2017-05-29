
import os
import shutil
import subprocess
import sys
import tkMessageBox
from subprocess import call
import accSelect
import backupType_support
import sign_support
import unsign
import unsign_support
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

def pushVars(bkup, ld):
    global load
    load = ld
    global backup
    backup = bkup

def resignVars(bku,lod):
    global loaad
    loaad = lod
    global bkupz
    bkupz = bku



def loadPSM():
    global load
    load = "PSM"

def loadPSP():
    global load
    load = "PGAME"


def loadPSOne():
    global load
    load = "PSGAME"


def loadPSV():
    global load
    load = "APP"


def loadSYS():
    global load
    load = "SYSTEM"
global account
def chooseAccount(account):
    if backupType_support.getImportType() == "unsign":
        accSelect.close_window(root)
        unsign_support.pushVars(account,load,False)
        unsign.vp_start_gui()
    elif backupType_support.getImportType() == "sign":
        sign_support.goSign(account,load,backup,False)
    if backupType_support.getImportType() == "resign":
        accSelect.close_window(root)
        unsign_support.pushVars(account,load,True)
        unsign.vp_start_gui()
    if backupType_support.getImportType() == "resign2":
        accSelect.close_window(root)
        sign_support.goSign(account, loaad, bkupz,True)
        tkMessageBox.showinfo(title="Resign", message="Re-Sign Complete! (Refresh QCMA)")



def getAccount():
    return account

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
    import accSelect
    accSelect.vp_start_gui()


