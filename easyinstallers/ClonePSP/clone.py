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

import clone_support

def vp_start_gui(acc=0,bkup=0,cma=0):
    global account
    global oldtitleid
    global CMA
    account = acc
    oldtitleid = bkup
    CMA = cma
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        import defs
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    top = Clone_Bubble (root)
    clone_support.init(root, top)
    root.mainloop()

w = None
def create_Clone_Bubble(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Clone_Bubble (w)
    clone_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Clone_Bubble():
    global w
    w.destroy()
    w = None


class Clone_Bubble:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {DejaVu Sans Mono} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("225x189+511+189")
        top.title("Clone Bubble")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.04, rely=0.05, height=18, width=206)
        self.Label1.configure(text='''Enter New TitleID''')
        self.Label1.configure(width=206)

        self.Message1 = Message(top)
        self.Message1.place(relx=0.0, rely=0.37, relheight=0.32, relwidth=0.99)
        self.Message1.configure(text='''Must be 9 characters
A-Z & 0-9 Only, ALL Capitals
ex: PSVIM0001''')
        self.Message1.configure(width=223)

        self.titleid = Entry(top)
        self.titleid.place(relx=0.04, rely=0.21, relheight=0.13, relwidth=0.92)
        self.titleid.configure(background="white")
        self.titleid.configure(font=font10)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.04, rely=0.74, height=26, width=88)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=lambda: clone_support.set(self.titleid.get(),oldtitleid,account))
        self.Button1.configure(text='''Set TitleID''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.44, rely=0.74, height=26, width=117)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(command=lambda: clone_support.random(oldtitleid,account))
        self.Button2.configure(text='''Random TitleID''')
        self.Button2.configure(width=117)

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event):
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.post(event.x_root, event.y_root)

    @staticmethod
    def popup3(event):
        Popupmenu3 = Menu(root, tearoff=0)
        Popupmenu3.configure(activebackground="#f9f9f9")
        Popupmenu3.post(event.x_root, event.y_root)

    @staticmethod
    def popup4(event):
        Popupmenu4 = Menu(root, tearoff=0)
        Popupmenu4.configure(activebackground="#f9f9f9")
        Popupmenu4.post(event.x_root, event.y_root)

    @staticmethod
    def popup5(event):
        Popupmenu5 = Menu(root, tearoff=0)
        Popupmenu5.configure(activebackground="#f9f9f9")
        Popupmenu5.post(event.x_root, event.y_root)

    @staticmethod
    def popup6(event):
        Popupmenu6 = Menu(root, tearoff=0)
        Popupmenu6.configure(activebackground="#f9f9f9")
        Popupmenu6.post(event.x_root, event.y_root)

    @staticmethod
    def popup7(event):
        Popupmenu7 = Menu(root, tearoff=0)
        Popupmenu7.configure(activebackground="#f9f9f9")
        Popupmenu7.post(event.x_root, event.y_root)

    @staticmethod
    def popup8(event):
        Popupmenu8 = Menu(root, tearoff=0)
        Popupmenu8.configure(activebackground="#f9f9f9")
        Popupmenu8.post(event.x_root, event.y_root)

    @staticmethod
    def popup9(event):
        Popupmenu9 = Menu(root, tearoff=0)
        Popupmenu9.configure(activebackground="#f9f9f9")
        Popupmenu9.post(event.x_root, event.y_root)

    @staticmethod
    def popup10(event):
        Popupmenu10 = Menu(root, tearoff=0)
        Popupmenu10.configure(activebackground="#f9f9f9")
        Popupmenu10.post(event.x_root, event.y_root)

    @staticmethod
    def popup11(event):
        Popupmenu11 = Menu(root, tearoff=0)
        Popupmenu11.configure(activebackground="#f9f9f9")
        Popupmenu11.post(event.x_root, event.y_root)

    @staticmethod
    def popup12(event):
        Popupmenu12 = Menu(root, tearoff=0)
        Popupmenu12.configure(activebackground="#f9f9f9")
        Popupmenu12.post(event.x_root, event.y_root)

    @staticmethod
    def popup13(event):
        Popupmenu13 = Menu(root, tearoff=0)
        Popupmenu13.configure(activebackground="#f9f9f9")
        Popupmenu13.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()



