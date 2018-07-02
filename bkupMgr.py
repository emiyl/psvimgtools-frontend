
import sys

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

import bkupMgr_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    top = Backup_Mannager (root)
    bkupMgr_support.init(root, top)
    root.mainloop()

w = None
def create_Backup_Mannager(root, *args, **kwargs): ##*manager
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Backup_Mannager (w)
    bkupMgr_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Backup_Mannager():
    global w
    w.destroy()
    w = None


class Backup_Mannager:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("170x180+588+287")
        top.title("Backup Mannager")
        top.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.06, rely=0.0, relheight=0.96
                , relwidth=0.88)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Backup Manager''')
        self.Labelframe1.configure(width=150)

        self.unsign = Button(self.Labelframe1)
        self.unsign.place(relx=0.07, rely=0.12, height=26, width=127)
        self.unsign.configure(activebackground="#d9d9d9")
        self.unsign.configure(command=bkupMgr_support.unsign)
        self.unsign.configure(text='''Unsign & Extract''')

        self.sign = Button(self.Labelframe1)
        self.sign.place(relx=0.07, rely=0.29, height=26, width=127)
        self.sign.configure(activebackground="#d9d9d9")
        self.sign.configure(command=bkupMgr_support.sign)
        self.sign.configure(text='''Sign & Pack''')

        self.reSign = Button(self.Labelframe1)
        self.reSign.place(relx=0.07, rely=0.46, height=26, width=127)
        self.reSign.configure(activebackground="#d9d9d9")
        self.reSign.configure(command=bkupMgr_support.reSign)
        self.reSign.configure(text='''Quick Re-Sign''')

        self.cmaDir = Button(self.Labelframe1)
        self.cmaDir.place(relx=0.07, rely=0.73, height=26, width=127)
        self.cmaDir.configure(activebackground="#d9d9d9")
        self.cmaDir.configure(command=bkupMgr_support.cmaDir)
        self.cmaDir.configure(text='''CMA DIR''')

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.07, rely=0.63, height=14, width=56)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor=W)
        self.Label1.configure(justify=LEFT)
        self.Label1.configure(text='''Options:''')






if __name__ == '__main__':
    vp_start_gui()



