
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

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    top = PSVImgTools (root)
    main_support.init(root, top)
    root.mainloop()



w = None
def create_PSVImgTools(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = PSVImgTools (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_PSVImgTools():
    global w
    w.destroy()
    w = None


class PSVImgTools:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("170x180+570+315")
        top.title("PSVImgTools")
        top.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.06, rely=0.0, relheight=0.94
                , relwidth=0.88)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''PSVImgTools''')
        self.Labelframe1.configure(width=150)

        self.Button1 = Button(self.Labelframe1)
        self.Button1.place(relx=0.07, rely=0.12, height=26, width=127)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=main_support.esyInstall)
        self.Button1.configure(text='''Easy Installers''')

        self.Button2 = Button(self.Labelframe1)
        self.Button2.place(relx=0.07, rely=0.29, height=26, width=127)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(command=main_support.bkupMgr)
        self.Button2.configure(text='''Backup Manager''')


        self.Button3 = Button(self.Labelframe1)
        self.Button3.place(relx=0.07, rely=0.47, height=26, width=127)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(command=main_support.accMan)
        self.Button3.configure(text='''Account Manager''')

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.07, rely=0.65, height=48, width=126)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''PSVIMGTOOLS By:
Molecule/Yifanlu
Gui By: SilicaAndPina''')






if __name__ == '__main__':
    vp_start_gui()



