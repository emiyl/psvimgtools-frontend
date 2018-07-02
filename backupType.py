
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

import backupType_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        import defs
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    top = Backup_Type (root)
    backupType_support.init(root, top)
    root.mainloop()
w = None
def create_Backup_Type(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Backup_Type (w)
    backupType_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Backup_Type():
    global w
    w.destroy()
    w = None


class Backup_Type:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("170x180+510+198")
        top.title("Backup Type")
        top.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.06, rely=0.0, relheight=0.97
                , relwidth=0.88)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Backup Type''')
        self.Labelframe1.configure(width=150)

        self.Button1 = Button(self.Labelframe1)
        self.Button1.place(relx=0.07, rely=0.29, height=26, width=127)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=backupType_support.psp)
        self.Button1.configure(text='''Playstation Portable''')

        self.Button2 = Button(self.Labelframe1)
        self.Button2.place(relx=0.07, rely=0.46, height=26, width=127)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(command=backupType_support.psm)
        self.Button2.configure(text='''Playstation Mobile''')

        self.Button3 = Button(self.Labelframe1)
        self.Button3.place(relx=0.07, rely=0.63, height=26, width=127)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(command=backupType_support.psone)
        self.Button3.configure(text='''Playstation One''')

        self.Button4 = Button(self.Labelframe1)
        self.Button4.place(relx=0.07, rely=0.11, height=26, width=127)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(command=backupType_support.psv)
        self.Button4.configure(text='''Playstation Vita''')

        self.Button5 = Button(self.Labelframe1)
        self.Button5.place(relx=0.07, rely=0.8, height=26, width=127)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(command=backupType_support.system)
        self.Button5.configure(text='''System Backup''')






if __name__ == '__main__':
    vp_start_gui()



