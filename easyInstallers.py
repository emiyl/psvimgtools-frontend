
import fnmatch
import os
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

import easyInstallers_support

def vp_start_gui():
    """Starting point when module is the main routine."""
    global root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    easyInstallers_support.set_Tk_var()
    top = Easy_Installers(root)
    easyInstallers_support.init(root, top)
    root.mainloop()


def close_window(root):
    root.destroy()


w = None

def create_Easy_Installers(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global rt
    global w
    rt = root
    w = Toplevel(root)
    easyInstallers_support.set_Tk_var()
    top = Easy_Installers(w)
    easyInstallers_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Easy_Installers():
    global w
    w.destroy()
    w = None


class Easy_Installers:

    def __init__(self, top = None):
        """This class configures and populates the toplevel window.
        top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'
        font10 = '-family {DejaVu Sans Mono} -size 12 -weight normal -slant roman -underline 0 -overstrike 0'
        self.style = ttk.Style()
        if sys.platform == 'win32':
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])
        top.geometry('600x450+387+80')
        top.title('Easy Installers')
        top.configure(highlightcolor='black')
        self.Button3 = Button(top)
        self.Button3.place(relx=0.62, rely=0.91, height=26, width=217)
        self.Button3.configure(activebackground='#d9d9d9')
        self.Button3.configure(command=lambda : easyInstallers_support.install(self.backupList.get(ACTIVE)))
        self.Button3.configure(text='Install')
        a = 0
        self.backupList = ScrolledListBox(top)
        self.backupList.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.58)
        self.backupList.configure(background='white')
        self.backupList.configure(font=font10)
        self.backupList.configure(highlightcolor='#d9d9d9')
        self.backupList.configure(selectbackground='#c4c4c4')
        self.backupList.configure(width=10)
        for root, dir, files in defs.walklevel(defs.getWorkingDir()+'/easyinstallers',0):
            for items in fnmatch.filter(dir, '*'):
                a += 1
                if defs.isPlugin(items):
                    self.backupList.insert(a, items)



class AutoScroll(object):
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass

        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
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
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() + Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""

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
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)

    return wrapped


class ScrolledListBox(AutoScroll, Listbox):
    """A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


if __name__ == '__main__':
    vp_start_gui()

