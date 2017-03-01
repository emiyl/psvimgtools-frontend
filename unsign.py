
import fnmatch
import os
import sys
import defs
import sfoParser
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

import unsign_support

def vp_start_gui():
    """Starting point when module is the main routine."""
    global root
    root = Tk()
    top = Unsign_Backup(root)
    unsign_support.init(root, top)


def close_window(root):
    root.destroy()


w = None

def create_Unsign_Backup(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global rt
    global w
    rt = root
    w = Toplevel(root)
    top = Unsign_Backup(w)
    unsign_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Unsign_Backup():
    global w
    w.destroy()
    w = None


class Unsign_Backup:

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
        top.geometry('750x500+218+86')
        top.title('Unsign Backup')
        top.configure(highlightcolor='black')
        cmadir = open('cmadir.txt', 'r')
        CMA = cmadir.read()
        a = 0
        self.Label1 = Label(top)
        self.Label1.place(relx=0.02, rely=0.02, height=18, width=96)
        self.Label1.configure(text='What Backup?')
        self.Label1.configure(width=96)
        self.backupList = ScrolledListBox(top)
        self.backupList.place(relx=0.01, rely=0.06, relheight=0.87, relwidth=0.97)
        self.backupList.configure(background='white')
        self.backupList.configure(font=font10)
        self.backupList.configure(highlightcolor='#d9d9d9')
        self.backupList.configure(selectbackground='#c4c4c4')
        self.backupList.configure(width=10)
        print 'Looking For Backups In: ' + CMA + '/' + unsign_support.getLoad() + '/' + defs.getAid(unsign_support.getAccount())
        for root, dir, files in os.walk(CMA + '/' + unsign_support.getLoad() + '/' + defs.getAid(unsign_support.getAccount())):
            for items in fnmatch.filter(dir, '*'):
                a += 1
                if defs.isEncryptedApp(CMA + '/' + unsign_support.getLoad() + '/' + defs.getAid(unsign_support.getAccount()) + '/' + items):
                    title = sfoParser.main(CMA + '/' + unsign_support.getLoad() + '/' + defs.getAid(unsign_support.getAccount()) + '/' + items + '/sce_sys/param.sfo')
                    self.backupList.insert(a, title + ' (' + items + ')')
                elif unsign_support.getLoad() == 'SYSTEM' and defs.isBackup(CMA + '/' + unsign_support.getLoad() + '/' + defs.getAid(unsign_support.getAccount()) + '/' + items + '/' + items):
                    self.backupList.insert(a, items)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.83, rely=0.94, height=26, width=117)
        self.Button1.configure(activebackground='#d9d9d9')
        if unsign_support.getLoad() != "SYSTEM":
            self.Button1.configure(command=lambda : unsign_support.goUnsign(defs.getTitleID(self.backupList.get(ACTIVE)), CMA))
        else:
            self.Button1.configure(
                command=lambda: unsign_support.goUnsign(self.backupList.get(ACTIVE), CMA))
        self.Button1.configure(text='Unsign & Extract')
        if unsign_support.getResign() == False:
            self.Button2 = Button(top)
            self.Button2.place(relx=0.01, rely=0.94, height=26, width=77)
            self.Button2.configure(activebackground='#d9d9d9')
            self.Button2.configure(command=unsign_support.browse)
            self.Button2.configure(text='Browse')


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

