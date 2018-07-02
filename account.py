
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

import account_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        import defs
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    top = Add_Account(root)
    account_support.init(root, top)
    root.mainloop()
    root.resizable(0, 0)

def close_window(root):
    root.destroy()


w = None


def create_Add_Account(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Add_Account(w)
    account_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Add_Account():
    global w
    w.destroy()
    w = None


class Add_Account:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'

        top.geometry("400x200+469+264")
        top.title("Add Account")
        top.configure(highlightcolor="black")

        self.accName = Entry(top)
        self.accName.place(relx=0.35, rely=0.3, relheight=0.11, relwidth=0.44)
        self.accName.configure(background="white")
        self.accName.configure(font="TkFixedFont")
        self.accName.configure(selectbackground="#c4c4c4")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.25, rely=0.1, height=38, width=176)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Add Account''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.03, rely=0.3, height=18, width=126)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Account Name:''')

        self.key = Entry(top)
        self.key.place(relx=0.35, rely=0.5, relheight=0.11, relwidth=0.44)
        self.key.configure(background="white")
        self.key.configure(font="TkFixedFont")
        self.key.configure(selectbackground="#c4c4c4")

        self.Label3 = Label(top)
        self.Label3.place(relx=0.15, rely=0.5, height=21, width=76)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''AID:''')

        self.add = Button(top)
        self.add.place(relx=0.53, rely=0.7, height=26, width=107)
        self.add.configure(activebackground="#d9d9d9")
        self.add.configure(command=lambda: account_support.addaccount(self.key.get(), self.accName.get()))
        self.add.configure(text='''Add Account''')

        self.helpButton = Button(top)
        self.helpButton.place(relx=0.8, rely=0.5, height=16, width=17)
        self.helpButton.configure(activebackground="#d9d9d9")
        self.helpButton.configure(command=account_support.question)
        self.helpButton.configure(text='''?''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.35, rely=0.7, height=26, width=54)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=account_support.auto)
        self.Button1.configure(text='''Auto''')


if __name__ == '__main__':
    vp_start_gui()



