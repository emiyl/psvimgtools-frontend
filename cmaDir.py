
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

import cmaDir_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        import defs
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    top = Cma_Directory (root)
    cmaDir_support.init(root, top)
    root.mainloop()
    root.resizable(0, 0)
def close_window(root):
    root.destroy()


w = None
def create_Cma_Directory(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Cma_Directory (w)
    cmaDir_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Cma_Directory():
    global w
    w.destroy()
    w = None


class Cma_Directory:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color,: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {DejaVu Sans Mono} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("350x100+652+125")
        top.title("Cma Directory")



        self.CmaDIR = Entry(top)
        self.CmaDIR.place(relx=0.2, rely=0.3, relheight=0.25, relwidth=0.73)
        self.CmaDIR.configure(background="white")
        self.CmaDIR.configure(font=font10)
        self.CmaDIR.configure(selectbackground="#c4c4c4")
        self.CmaDIR.configure(width=256)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.06, rely=0.1, height=18, width=136)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''QCMA Backups Folder:''')

        self.Button6 = Button(top)
        self.Button6.place(relx=0.74, rely=0.6, height=26, width=70)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(command=lambda: cmaDir_support.submit(self.CmaDIR.get()))
        self.Button6.configure(text='''Submit''')

        self.Button7 = Button(top)
        self.Button7.place(relx=0.57, rely=0.6, height=26, width=54)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(command=cmaDir_support.auto)
        self.Button7.configure(text='''Auto''')
        self.Button7.configure(width=54)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.06, rely=0.3, height=26, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=cmaDir_support.browse)
        self.Button1.configure(text='''Browse''')
        self.Button1.configure(width=67)






if __name__ == '__main__':
    vp_start_gui()



