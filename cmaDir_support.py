
import os
import sys
import tkFileDialog
import tkMessageBox

from os.path import expanduser

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


def auto():
    import cmaDir
    defs.autoCMA()
    path = defs.getCmaDir()
    cmaDir.close_window(root)
    tkMessageBox.showinfo(title="Cma Directory", message="Detected: [" + path + "]!")





    sys.stdout.flush()

def submit(DIR):
    import cmaDir
    text_file = open("cmadir.txt", "w+")
    text_file.write(DIR)
    text_file.close()
    cmaDir.close_window(root)
    sys.stdout.flush()

def browse():
    import cmaDir
    text_file = open("cmadir.txt", "w+")
    text_file.write(tkFileDialog.askdirectory(title="CMA Directory"))
    text_file.close()
    cmaDir.close_window(root)
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
    import cmaDir
    cmaDir.vp_start_gui()


