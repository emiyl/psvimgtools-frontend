
import fnmatch
import os
import tkMessageBox
import tkSimpleDialog

import pfs
import sfoParser
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

import sign_support
def pfdecrypt(titleid):
    if pfs.isKeyKnown(titleid):
        if tkMessageBox.askyesno(title="PFS",message="Decrypt PFS For "+titleid+"?"):
            pfs.decrypt(titleid)
            tkMessageBox.showinfo(title="PFS",message="PFS Decrypted For "+titleid)
    elif os.path.exists(defs.getCmaDir()+"/EXTRACTED/APP/"+titleid+"/savedata"):
            pfs.decryptSavedata(titleid)
            tkMessageBox.showinfo(title="PFS",message="Savedata was decrypted, game files where NOT decrypted (PFS Key Is Unknown)")
    if not pfs.isKeyKnown(titleid):
        newKey = tkSimpleDialog.askstring(title="PFS",prompt="PFS Decryption Key Is Unknown For "+titleid+".\nIf You Have The Key In Either KLicensee Or zRIF Format\nEnter It Below:")
        if newKey != "":
            pfs.addKey(titleid,newKey)
            tkMessageBox.showinfo(title="Added Key For: "+titleid+" To The Key Database.")
            pfs.decrypt(titleid)
            tkMessageBox.showinfo(title="PFS", message="PFS Decrypted For " + titleid)
def vp_start_gui():
    """Starting point when module is the main routine."""
    global root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    sign_support.set_Tk_var()
    top = Sign_Backup(root)
    sign_support.init(root, top)
    root.mainloop()


def close_window(root):
    root.destroy()


def isOpen():
    if 'normal' == root.state():
        return True
    else:
        return False


w = None

def create_Sign_Backup(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global rt
    global w
    rt = root
    w = Toplevel(root)
    sign_support.set_Tk_var()
    top = Sign_Backup(w)
    sign_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Sign_Backup():
    global w
    w.destroy()
    w = None


class Sign_Backup:

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
        top.geometry('750x500+183+54')
        top.title('Sign Backup')
        top.configure(highlightcolor='black')
        cmadir = open('cmadir.txt', 'r')
        CMA = cmadir.read()
        self.Button2 = Button(top)
        self.Button2.place(relx=0.13, rely=0.94, height=26, width=107)
        self.Button2.configure(activebackground='#d9d9d9')
        if sign_support.getLoad() != "SYSTEM":
            self.Button2.configure(command=lambda : sign_support.delBkup(defs.getTitleID(self.backupList.get(ACTIVE))))
        elif sign_support.getLoad() == "SYSTEM":
            self.Button2.configure(command=lambda: sign_support.delBkup(self.backupList.get(ACTIVE)))
        self.Button2.configure(text='Delete Backup')
        self.Button2.configure(width=107)
        self.Button3 = Button(top)
        self.Button3.place(relx=0.87, rely=0.94, height=26, width=87)
        self.Button3.configure(activebackground='#d9d9d9')
        if sign_support.getLoad() != "SYSTEM":
            self.Button3.configure(command=lambda : sign_support.sign(defs.getTitleID(self.backupList.get(ACTIVE))))
        elif sign_support.getLoad() == "SYSTEM":
            self.Button3.configure(command=lambda: sign_support.sign(self.backupList.get(ACTIVE)))
        self.Button3.configure(text='Sign & Pack')
        self.Button3.configure(width=87)
        a = 0
        self.backupList = ScrolledListBox(top)
        self.backupList.place(relx=0.01, rely=0.02, relheight=0.91, relwidth=0.97)
        self.backupList.configure(background='white')
        self.backupList.configure(font=font10)
        self.backupList.configure(highlightcolor='#d9d9d9')
        self.backupList.configure(selectbackground='#c4c4c4')
        self.backupList.configure(width=10)
        print 'Looking For Backups In: ' + CMA + '/EXTRACTED/' + sign_support.getLoad()
        for root, dir, files in defs.walklevel(CMA + '/EXTRACTED/' + sign_support.getLoad(),0):
            for items in fnmatch.filter(dir, '*'):
                a += 1
                if sign_support.getLoad() != 'SYSTEM' and defs.isApp(CMA + '/EXTRACTED/' + sign_support.getLoad() + '/' + items):
                    title = sfoParser.main(CMA + '/EXTRACTED/' + sign_support.getLoad() + '/' + items + '/sce_sys/param.sfo')
                    if pfs.isKeyKnown(items):
                        self.backupList.insert(a, title + ' [PFS] (' + items + ')')
                    else:
                        self.backupList.insert(a, title + ' (' + items + ')')
                elif sign_support.getLoad() == 'SYSTEM' and defs.isBackup(CMA + '/EXTRACTED/' + sign_support.getLoad() + '/' + items):
                    self.backupList.insert(a, items)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.01, rely=0.94, height=26, width=87)
        self.Button4.configure(activebackground='#d9d9d9')
        if sign_support.getLoad() != "SYSTEM":
            self.Button4.configure(command=lambda : sign_support.expBkup(defs.getTitleID(self.backupList.get(ACTIVE))))
        elif sign_support.getLoad() == 'SYSTEM':
            self.Button4.configure(command=lambda: sign_support.expBkup(self.backupList.get(ACTIVE)))
        self.Button4.configure(text='Edit Backup')
        self.Button4.configure(width=87)

        self.Button9 = Button(top)
        self.Button9.place(relx=0.28, rely=0.94, height=26, width=115)
        self.Button9.configure(activebackground='#d9d9d9')
        self.Button9.configure(command=sign_support.cmbackup)
        self.Button9.configure(text='Install .cmbackup')
        self.Button9.configure(width=107)

        if sign_support.getLoad() == "APP":
            self.pfsDecryptButton = Button(top)
            self.pfsDecryptButton.place(relx=0.75, rely=0.94, height=26, width=87)
            self.pfsDecryptButton.configure(activebackground='#d9d9d9')
            self.pfsDecryptButton.configure(command=lambda: pfdecrypt(defs.getTitleID(self.backupList.get(ACTIVE))))
            self.pfsDecryptButton.configure(text='PFS Decrypt')
            self.pfsDecryptButton.configure(width=87)


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
