import os
import platform
import subprocess
import ConfigParser
import sys

from os.path import expanduser


def getCmaDir():
    text = text_file = open("cmadir.txt", "r")
    a = text.read()
    text_file.close()
    return a


def getKey():
    import os
    html_file = open("tempKey.html")
    line = html_file.read()
    line = line.splitlines()[16]
    line = line[25:]
    html_file.close()
    os.remove("tempKey.html")
    return line

def isPlugin(path):
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dir_path+"/easyinstallers/"+path+"/main.py"):
        return True

def getWorkingDir():
    return os.path.dirname(os.path.realpath(__file__))

def getAid(account):
    aid = open("accounts/" + account, 'r')
    CmaAID = aid.read()
    return CmaAID

def getStoredKey(account):
    key = open("keys/" + account, 'r')
    CmaKey = key.read()
    return CmaKey

def isBackup(dir):
    if os.path.isfile(dir+".psvinf"):

        return True

def isEncryptedApp(dir):
    if os.path.isfile(dir+"/license/license.psvmd"):
        return True

def isApp(dir):
    if os.path.isfile(dir+"/license.psvmd-dec"):
        return True

def autoCMA():
    if sys.platform.__contains__("linux"):
        home = expanduser("~")
        configParser = ConfigParser.RawConfigParser()
        configFilePath = home+"/.config/codestation/qcma.conf"
        configParser.read(configFilePath)
        line = configParser.get('General', 'appsPath')

        text_file = open("cmadir.txt", "w+")
        text_file.write(line)
        text_file.close()
        print "CMA Dir: " + line

    if sys.platform.__contains__("win"):
        import _winreg
        qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\codestation\qcma")
        path = _winreg.QueryValueEx(qcma, "appsPath")
        print "CMA Dir: " + path[0]
        text_file = open("cmadir.txt", "w+")
        text_file.write(path[0])
        text_file.close()
        _winreg.CloseKey(qcma)


def autoAccount():

    ##GET AID FROM QCMA CONFIG
    if sys.platform.__contains__("linux"):
        home = expanduser("~")
        configParser = ConfigParser.RawConfigParser()
        configFilePath = home+"/.config/codestation/qcma.conf"
        configParser.read(configFilePath)
        aid = configParser.get('General', 'lastAccountId')
        print "AID: " + aid
    if sys.platform.__contains__("win"):
        import _winreg
        qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\codestation\qcma")
        aid = _winreg.QueryValueEx(qcma, "lastAccountId")
        aid = aid[0]
        print "AID: " + aid
        _winreg.CloseKey(qcma)
    ##GET ACCOUNT NAME FROM QCMA CONFIG
    if sys.platform.__contains__("linux"):
        home = expanduser("~")
        configParser = ConfigParser.RawConfigParser()
        configFilePath = home+"/.config/codestation/qcma.conf"
        configParser.read(configFilePath)
        acc = configParser.get('General', 'lastOnlineId')

        print "Account Name: " + acc
    if sys.platform.__contains__("win"):
        import _winreg
        qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\codestation\qcma")
        acc = _winreg.QueryValueEx(qcma, "lastOnlineId")
        acc = acc[0]
        print "Account Name: " + acc
        _winreg.CloseKey(qcma)


    import urllib
    print "Downloading Key From: " + "http://cma.henkaku.xyz/?aid=" + aid
    urllib.urlretrieve("http://cma.henkaku.xyz/?aid=" + aid, "tempKey.html")
    key = getKey()
    print "CMA Key: "+ key

    text_file = open("keys/" + acc, "w+")
    text_file.write(key)
    text_file.close()

    text_file = open("accounts/" + acc, "w+")
    text_file.write(aid)
    text_file.close()
