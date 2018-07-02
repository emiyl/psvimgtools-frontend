
import fnmatch
import os
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

import accMgr_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        import defs
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    accMgr_support.set_Tk_var()
    top = Account_Mannager (root)
    accMgr_support.init(root, top)
    root.mainloop()
    root.resizable(0, 0)

def close_window(root):
    root.destroy()

w = None
def create_Account_Mannager(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    accMgr_support.set_Tk_var()
    top = Account_Mannager (w)
    accMgr_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Account_Mannager(): ##Spelling error i know, but i dont know what would happen if anything would break if i changed
    global w
    w.destroy()
    w = None


class Account_Mannager:
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+520+158")
        top.title("Account Manager")
        top.configure(highlightcolor="black")



        self.Button2 = Button(top)
        self.Button2.place(relx=0.65, rely=0.82, height=26, width=207)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(command = lambda: accMgr_support.rmAcc(self.Scrolledlistbox1.get(ACTIVE)))
        self.Button2.configure(text='''Remove Account''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.65, rely=0.88, height=26, width=207)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(command=accMgr_support.addAcc)
        self.Button3.configure(text='''Add Account''')
        a=0
        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.02, rely=0.02, relheight=0.96
                , relwidth=0.61)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font=font10)
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(width=10)
        for root, dir, files in os.walk("accounts"):
            for items in fnmatch.filter(files, "*"):
                a += 1
                self.Scrolledlistbox1.insert(a, items)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.65, rely=0.76, height=26, width=207)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(command = lambda: accMgr_support.edAcc(self.Scrolledlistbox1.get(ACTIVE)))
        self.Button4.configure(text='''Edit Account''')





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



