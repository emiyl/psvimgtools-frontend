import Tkinter
import json
import ConfigParser
import sys
import tkMessageBox
import urllib
import webbrowser
if sys.platform == "darwin":
    import bplistlib
from os.path import expanduser

import requests


global latestVersion

def doesStringContain(contain,string):
    valid = set(contain)
    return set(string).issubset(valid)


def showMessage(title,message):
    window = Tkinter.Tk()
    window.wm_withdraw()
    tkMessageBox.showinfo(title=title, message=message)
    window.destroy()

def downloadWithProgressBar(link, file_name):
    with open(file_name, "wb") as f:
            print "Downloading %s" % file_name
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                    sys.stdout.flush()

def checkForUpdate(currentVersion):
    try:
        urllib.urlretrieve('https://api.github.com/repos/SilicaAndPina/psvimgtools-frontend/releases/latest', 'tmp.json')
    except: ##EXCEPT NETWORK ERROR -- THX GAMERSREBIRTHDL
        print "Could Not Connect, Skipping Update Check."
    if os.path.exists('tmp.json'):
        with open('tmp.json') as data_file:
            data = json.load(data_file)
            global latestVersion
            latestVersion = data["tag_name"]
            data_file.close()
        os.remove("tmp.json")
        print 'Latest Version Is: ' + latestVersion
        print 'Current Version Is: ' + currentVersion
        if currentVersion != latestVersion:
            print "An Update Is Available!"
            window = Tkinter.Tk()
            window.wm_withdraw()
            update = tkMessageBox.askyesno(title="Update?",message="An Update Is Avalible! \nVersion "+latestVersion+" Would you like to update?")
            window.destroy()
            if update:
                if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
                    if get64Bit():
                        downloadWithProgressBar("https://github.com/SilicaAndPina/psvimgtools-frontend/releases/download/"+latestVersion+"/psvimgtools-frontend-win64-setup.exe","install.exe")
                        os.system("start install.exe")
                        sys.exit()
                    else:
                        downloadWithProgressBar("https://github.com/SilicaAndPina/psvimgtools-frontend/releases/download/"+latestVersion+"/psvimgtools-frontend-win32-setup.exe","install.exe")
                        os.system("start install.exe")
                        sys.exit()
                else:
                    webbrowser.open_new_tab("https://github.com/SilicaAndPina/psvimgtools-frontend/releases/latest")
                sys.exit()
        else:
            print "No Updates Available."




def get64Bit():
    return sys.maxsize > 2 ** 32

if sys.platform.__contains__('linux'):

    def openFolder(path):
        os.system('xdg-open "' + path + '"')


if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):

    def openFolder(path):
        os.system('start "" "'+ path + '"')

def getHomeDir():
    from os.path import expanduser
    home = expanduser("~")
    return home

def getCmaDir():
    if os.path.exists("cmadir.txt"):
        text = text_file = open(getWorkingDir()+'/cmadir.txt', 'r')
        a = text.read()
        text_file.close()
        return a


def getKey():
    import os
    html_file = open(getWorkingDir()+'/tempKey.html')
    line = html_file.read()
    line = line.splitlines()[16]
    line = line[25:]
    html_file.close()
    os.remove(getWorkingDir()+'/tempKey.html')
    return line

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

def isPlugin(path):
    import os
    if os.path.exists(getWorkingDir() + '/easyinstallers/' + path + '/main.py'):
        return True


def getWorkingDir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))




def getAid(account):
    aid = open(getWorkingDir()+'/accounts/' + account, 'r')
    CmaAID = aid.read()
    return CmaAID


def getStoredKey(account):
    key = open(getWorkingDir()+'/keys/' + account, 'r')
    CmaKey = key.read()
    return CmaKey


def isBackup(dir):
    if os.path.isfile(dir + '.psvinf'):
        return True


def isEncryptedApp(dir):
    if os.path.isfile(dir + '/sce_sys/param.sfo'):
        return True


def isApp(dir):
    if os.path.isfile(dir + '/sce_sys/param.sfo'):
        return True

def getKeyType(key):
    if len(key) == 32:
        return "klicense"
    else:
        return "zrif"

def autoCMA():
    if sys.platform.__contains__('darwin'):
        home = expanduser('~')
        if os.path.exists(home + '/Library/Preferences/com.codestation.qcma.plist'):
            cmaFile = bplistlib.readPlist(home + '/Library/Preferences/com.codestation.qcma.plist')
            text_file = open('cmadir.txt', 'w+')
            text_file.write(cmaFile['appsPath'])
            text_file.close()
            print 'CMA Dir: ' + cmaFile['appsPath']
        else:
            print "Cannot find CMADir..."
            showMessage(title="CMADIR", message="Could not find the CMA Backups Directory.")
            import cmaDir
            cmaDir.vp_start_gui()
    if sys.platform.__contains__('linux'):
        home = expanduser('~')
        if os.path.exists(home + '/.config/codestation/qcma.conf'):
            configParser = ConfigParser.RawConfigParser()
            configFilePath = home + '/.config/codestation/qcma.conf'
            configParser.read(configFilePath)
            line = configParser.get('General', 'appsPath')
            text_file = open('cmadir.txt', 'w+')
            text_file.write(line)
            text_file.close()
            print 'CMA Dir: ' + line
        else:
            print "Cannot find CMADir..."
            showMessage(title="CMADIR", message="Could not find the CMA Backups Directory.")
            import cmaDir
            cmaDir.vp_start_gui()

    if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
        import _winreg
        try:
            global CMAFOLDER
            qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'Software\\codestation\\qcma')
            path = _winreg.QueryValueEx(qcma, 'appsPath')
            CMAFOLDER = path[0]
            _winreg.CloseKey(qcma)
        except:
            print("QCMA Is Not Installed.")
            print "Checking Default Location "+getHomeDir()+"\Documents\PS Vita"
            if os.path.exists("Checking Default Location "+getHomeDir()+"\Documents\PS Vita"):
                print "Directory Found! Setting As CMA APPS DIR "
                CMAFOLDER = getHomeDir()+"\My Documents\PS Vita"
            elif os.path.exists("Checking Default Location "+getHomeDir()+"\My Documents\PS Vita"):
                print "Directory Found! Setting As CMA Apps DIR"
                CMAFOLDER = getHomeDir()+"\My Documents\PS Vita"
                print "Legacy OS Detected, Documents Folder Is Called 'My Documents' PSVIMGTOOLS may not work correctly!"
            else:
                print "Folder not found checking for SONY CMA..."
                try:
                    cma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Sony Corporation\\Content Manager Assistant\\Settings')
                    path = _winreg.QueryValueEx(cma, 'ApplicationHomePath')
                    CMAFOLDER = path[0]
                    _winreg.CloseKey(cma)
                    print "---------------------WARNING---------------------"
                    print "SONY CMA IS NOT FULLY SUPPORTED, \nAND IT ALSO REQUIRES THE LATEST FIRMWARE"
                    print "I HIGHLY RECOMMEND USING QCMA INSTEAD!"
                except:
                    print "Checking for DEVKITCMA"
                    try:
                        cma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,'SOFTWARE\\SCE\\PSP2\\Services\\Content Manager Assistant for PlayStation(R)Vita DevKit\\Settings')
                        path = _winreg.QueryValueEx(cma, 'ApplicationHomePath')
                        CMAFOLDER = path[0]
                        _winreg.CloseKey(cma)
                        print "---------------------WARNING---------------------"
                        print "DEVKITCMA IS NOT FULLY SUPPORTED,"
                        print "I HIGHLY RECOMMEND USING QCMA INSTEAD!"
                    except:
                        print "Cannot find CMADir..."
                        showMessage(title="CMADIR", message="Could not find the CMA Backups Directory.")
                        import cmaDir
                        cmaDir.vp_start_gui()



        print 'CMA Dir: ' + CMAFOLDER
        text_file = open(getWorkingDir()+'/cmadir.txt', 'w+')
        text_file.write(CMAFOLDER)
        text_file.close()




def autoAccount():
    if sys.platform.__contains__('darwin'):
        home = expanduser('~')
        if os.path.exists(home + '/Library/Preferences/com.codestation.qcma.plist'):
            cmaFile = bplistlib.readPlist(home + '/Library/Preferences/com.codestation.qcma.plist')
            aid = cmaFile['lastAccountId']
            print 'AID: ' + aid
        else:
            print "No Account Found!"
            showMessage(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()

    if sys.platform.__contains__('linux'):
        home = expanduser('~')
        configParser = ConfigParser.RawConfigParser()
        configFilePath = home + '/.config/codestation/qcma.conf'
        configParser.read(configFilePath)
        if configParser.has_option("General",'lastAccountId'):
            aid = configParser.get('General', 'lastAccountId')
            print 'AID: ' + aid
        else:
            print "No Account Found!"
            showMessage(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()


    if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
        import _winreg
        try:
            qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'Software\\codestation\\qcma')
            aid = _winreg.QueryValueEx(qcma, 'lastAccountId')
        except:
            print "No Account Found!"
            showMessage(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()
        aid = aid[0]
        print 'AID: ' + aid
        _winreg.CloseKey(qcma)
    if sys.platform.__contains__('darwin'):
        home = expanduser('~')
        if os.path.exists(home + '/Library/Preferences/com.codestation.qcma.plist'):
            cmaFile = bplistlib.readPlist(home + '/Library/Preferences/com.codestation.qcma.plist')
            acc = cmaFile['lastAccountId']
            print 'Account Name: ' + acc
        else:
            print "No Account Found!"
            showMessage(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()
    if sys.platform.__contains__('linux'):
        home = expanduser('~')
        configParser = ConfigParser.RawConfigParser()
        configFilePath = home + '/.config/codestation/qcma.conf'
        configParser.read(configFilePath)
        if configParser.has_option("General", 'lastOnlineId'):
            acc = configParser.get('General', 'lastOnlineId')
            print 'Account Name: ' + acc
        else:
            print "No Account Found!"
            showMessage(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()
    if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
        import _winreg
        qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'Software\\codestation\\qcma')
        try:
            acc = _winreg.QueryValueEx(qcma, 'lastOnlineId')
            acc = acc[0]
        except:
            print "No Account Found!"
            showMessage(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()
        print 'Account Name: ' + acc
        _winreg.CloseKey(qcma)
    import urllib
    try:
        print 'Downloading Key From: ' + 'http://cma.henkaku.xyz/?aid=' + aid
        urllib.urlretrieve('http://cma.henkaku.xyz/?aid=' + aid, 'tempKey.html')
    except:
        print "Failed to connect to: "+'http://cma.henkaku.xyz/?aid=' + aid
        print "Trying henkaku.me.."
        try:
            print 'Downloading Key From: ' + 'http://cma.henkaku.me/?aid=' + aid
            urllib.urlretrieve('http://cma.henkaku.me/?aid=' + aid, 'tempKey.html')
        except:
            print "Failed to connect to: "+'http://cma.henkaku.me/?aid=' + aid
            print "Could Not Connect, Cannot find CMA Key!"
            window = Tkinter.Tk()
            window.wm_withdraw()
            tkMessageBox.showerror(title="Connection Error.",message="Failed to connect to: \nhttp://cma.henkaku.xyz\nThus your CMA Key could not be determined,\nPSVIMGTOOLS will not work without your CMA Key, \nPlease check your connection and try again.")
            window.destroy()
            sys.exit()

    key = getKey()
    print 'CMA Key: ' + key
    text_file = open(getWorkingDir()+'/keys/' + acc, 'w+')
    text_file.write(key)
    text_file.close()
    text_file = open(getWorkingDir()+'/accounts/' + acc, 'w+')
    text_file.write(aid)
    text_file.close()


def getTitleID(backup):
    output = backup[backup.find('(') + 1:]
    output = output[:-1]
    return output

import os
import zipfile

def executePy(file):
    print "Running file: "+ file
    pyFile = open(file)
    pyData = pyFile.read()
    pyFile.close()
    exec(pyData)


def zip(src, dst):
    zf = zipfile.ZipFile("%s" % (dst), "w", zipfile.ZIP_DEFLATED,allowZip64 = True)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'Writing %s To CMBackup' % (os.path.join(dirname, filename))
            zf.write(absname, arcname)
            print 'Removing '+os.path.join(dirname, filename)
            os.remove(os.path.join(dirname, filename))
    zf.close()

def extractZip(src,dst):
    zf = zipfile.ZipFile(src)
    zf.extractall(path=dst)
    zf.close()


import fnmatch
import os

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

import accSelect_support
def returnAccount(acc):
    global account
    account = acc
    close_window(root=root)

def get_account():
    vp_start_gui()
    return account

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    if sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
        import defs
        root.iconbitmap(bitmap=defs.getWorkingDir()+'\icon.ico')
    top = Account_Selector (root)
    accSelect_support.init(root, top)
    root.mainloop()
def close_window(root):
    root.destroy()
w = None
def create_Account_Selector(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Account_Selector (w)
    accSelect_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Account_Selector():
    global w
    w.destroy()
    w = None


class Account_Selector:
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

        top.geometry("310x453+398+30")
        top.title("Account Selector")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.03, rely=0.02, height=18, width=120)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Account Selector''')
        a=0
        self.accountList = ScrolledListBox(top)
        self.accountList.place(relx=0.03, rely=0.07, relheight=0.85
                , relwidth=0.92)
        self.accountList.configure(background="white")
        self.accountList.configure(font=font10)
        self.accountList.configure(highlightcolor="#d9d9d9")
        self.accountList.configure(selectbackground="#c4c4c4")
        self.accountList.configure(width=10)
        for root, dir, files in os.walk("accounts"):
            for items in fnmatch.filter(files, "*"):
                a += 1
                self.accountList.insert(a, items)
        self.Button1 = Button(top)
        self.Button1.place(relx=0.58, rely=0.93, height=26, width=117)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=lambda: returnAccount(self.accountList.get(ACTIVE)))
        self.Button1.configure(text='''Choose Account''')





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


