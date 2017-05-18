import json
import os
import platform
import shutil
import subprocess
import ConfigParser
import sys
import tkMessageBox
import urllib
import webbrowser
from pprint import pprint

import bplistlib
from os.path import expanduser

import requests

global latestVersion

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
    except: ##EXCEPT NETWORK ERROR -- THX GAMERSREBIRTHD
        print "Could Not Connect, Skipping Update Check."
    if os.path.exists('tmp.json'):
        with open('tmp.json') as data_file:
            data = json.load(data_file)
            latestVersion = data["tag_name"]
            data_file.close()
        os.remove("tmp.json")
        print 'Latest Version Is: ' + latestVersion
        print 'Current Version Is: ' + currentVersion
        if currentVersion != latestVersion:
            print "An Update Is Available!"
            if tkMessageBox.askyesno(title="Update?",message="An Update Is Avalible! \nVersion "+latestVersion+" Would you like to update?"):
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


def getHomeDir():
    from os.path import expanduser
    home = expanduser("~")
    return home

def getCmaDir():
    text = text_file = open('cmadir.txt', 'r')
    a = text.read()
    text_file.close()
    return a


def getKey():
    import os
    html_file = open('tempKey.html')
    line = html_file.read()
    line = line.splitlines()[16]
    line = line[25:]
    html_file.close()
    os.remove('tempKey.html')
    return line


def isPlugin(path):
    import os
    if os.path.exists(getWorkingDir() + '/easyinstallers/' + path + '/main.py'):
        return True


def getWorkingDir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))




def getAid(account):
    aid = open('accounts/' + account, 'r')
    CmaAID = aid.read()
    return CmaAID


def getStoredKey(account):
    key = open('keys/' + account, 'r')
    CmaKey = key.read()
    return CmaKey


def isBackup(dir):
    if os.path.isfile(dir + '.psvinf'):
        return True


def isEncryptedApp(dir):
    if os.path.isfile(dir + '/license/license.psvmd'):
        return True


def isApp(dir):
    if os.path.isfile(dir + '/license.psvmd-dec'):
        return True


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
            tkMessageBox.showinfo(title="CMADIR", message="Could not find the CMA Backups Directory.")
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
            tkMessageBox.showinfo(title="CMADIR", message="Could not find the CMA Backups Directory.")
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
                        tkMessageBox.showinfo(title="CMADIR", message="Could not find the CMA Backups Directory.")
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
            tkMessageBox.showinfo(title='FAIL',message='Count not find account automatically.')
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
            tkMessageBox.showinfo(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()


    if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
        import _winreg
        try:
            qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'Software\\codestation\\qcma')
            aid = _winreg.QueryValueEx(qcma, 'lastAccountId')
        except:
            print "No Account Found!"
            tkMessageBox.showinfo(title='FAIL',message='Count not find account automatically.')
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
            tkMessageBox.showinfo(title='FAIL',message='Count not find account automatically.')
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
            tkMessageBox.showinfo(title='FAIL',message='Count not find account automatically.')
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
            tkMessageBox.showinfo(title='FAIL',message='Count not find account automatically.')
            import account
            account.vp_start_gui()
        print 'Account Name: ' + acc
        _winreg.CloseKey(qcma)
    import urllib
    print 'Downloading Key From: ' + 'http://cma.henkaku.xyz/?aid=' + aid
    urllib.urlretrieve('http://cma.henkaku.xyz/?aid=' + aid, 'tempKey.html')
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

def zip(src, dst):
    zf = zipfile.ZipFile("%s" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'Adding %s To %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()

def extractZip(src,dst):
    zf = zipfile.ZipFile(src)
    zf.extractall(path=dst)
    zf.close()

