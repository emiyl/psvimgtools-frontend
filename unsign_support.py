
import os
import subprocess
import sys
import tkFileDialog
import tkMessageBox
from tkFileDialog import askopenfiles
import shutil
import accSelect
import accSelect_support
import backupType
import backupType_support
if sys.platform.__contains__('linux'):

    def openFolder(path):
        os.system('xdg-open "' + path + '"')


elif sys.platform.__contains__('win'):

    def openFolder(path):
        os.system('explorer.exe "' + path + '"')


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

def pushVars(acc, lad, resi):
    global load
    global account
    global resign
    account = acc
    load = lad
    resign = resi


def getResign():
    return resign


def getLoad():
    return load


def browse():
    import unsign
    unsign.close_window(root)
    filename = tkFileDialog.askopenfilename(title='Select file', filetypes=[('All Backup Files', '*.psvimg , *.psvmd'), ('Psvita Image Files', '*.psvimg'), ('PSVita MetaData Files', '*.psvmd')])
    key = open('keys/' + account, 'r')
    cmaKey = key.read()
    aid = open('accounts/' + account, 'r')
    cmaAID = aid.read()
    if filename.endswith('.psvimg'):
        tkMessageBox.showinfo(title='File Selection', message='File ' + filename + ' Selected, Please Specifiy An Output Directory')
        outputFolder = tkFileDialog.askdirectory(title='Output Folder')
        if sys.platform.__contains__('linux'):
            print 'Executing: ./psvimg-extract -K ' + cmaKey + ' "' + filename + '" "' + outputFolder + '"'
            os.system('./psvimg-extract -K ' + cmaKey + ' "' + filename + '" "' + outputFolder + '"')
        elif sys.platform.__contains__('win'):
            print 'Executing: psvimg-extract.exe -K ' + cmaKey + ' "' + filename + '" "' + outputFolder + '"'
            os.system('psvimg-extract.exe -K ' + cmaKey + ' "' + filename + '" "' + outputFolder + '"')
        tkMessageBox.showinfo(title='File Selection', message='Extraction Complete!')
        openFolder(outputFolder)
    elif filename.endswith('.psvmd'):
        tkMessageBox.showinfo(title='File Selection', message='File ' + filename + ' Selected, Please Specifiy Where To Save The Decrypted Output')
        outputFile = tkFileDialog.asksaveasfilename(title='Save As')
        if sys.platform.__contains__('linux'):
            print 'Executing: ./psvmd-decrypt -K ' + cmaKey + ' "' + filename + '" "' + outputFile + '"'
            os.system('./psvmd-decrypt -K ' + cmaKey + ' "' + filename + '" "' + outputFile + '"')
        elif sys.platform.__contains__('win'):
            print 'Executing: psvmd-decrypt.exe -K ' + cmaKey + ' "' + filename + '" "' + outputFile + '"'
            os.system('psvmd-decrypt.exe -K ' + cmaKey + ' "' + filename + '" "' + outputFile + '"')
        tkMessageBox.showinfo(title='File Selection', message='Extraction Complete!')
        openFolder(outputFile + '/..')


def goUnsign(cmaBackup, CMA):
    global am
    global foldParams
    import unsign
    unsign.close_window(root)
    key = open('keys/' + account, 'r')
    cmaKey = key.read()
    aid = open('accounts/' + account, 'r')
    cmaAID = aid.read()
    import sys
    if load != 'SYSTEM':
        if load == 'PGAME':
            foldParams = ['game', 'license']
            am = 1
        elif load == 'APP':
            foldParams = ['app',
             'patch',
             'addcont',
             'appmeta',
             'license',
             'savedata']
            am = 5
        elif load == 'PSGAME':
            foldParams = ['game', 'license']
            am = 1
        elif load == 'PSM':
            foldParams = ['game',
             'license',
             'patch',
             'savedata']
            am = 4
        if not os.path.exists(CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/'):
            os.makedirs(CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/')
        while am != -1:
            if os.path.exists(CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/'):
                if not os.path.exists(CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am]):
                    os.makedirs(CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am])
            am -= 1

        if load == 'PGAME':
            foldParams = ['game', 'license']
            am = 1
        elif load == 'APP':
            foldParams = ['app',
             'patch',
             'addcont',
             'appmeta',
             'license',
             'savedata']
            am = 5
        elif load == 'PSGAME':
            foldParams = ['game', 'license']
            am = 1
        elif load == 'PSM':
            foldParams = ['game', 'license']
            am = 1
        while am != -1:
            if sys.platform.__contains__('linux'):
                print 'Executing: ./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '"'
                os.system('./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '"')
                print 'Executing: ./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"'
                os.system('./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"')
                am -= 1
            elif sys.platform.__contains__('win'):
                print 'Executing: psvimg.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg ' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am]
                os.system('psvimg-extract.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '"')
                print 'Executing: psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"'
                os.system('psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"')
                am -= 1

        if not os.path.exists(CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/sce_sys'):
            print 'Copying Folder: ' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/sce_sys' + ' To: ' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/sce_sys'
            shutil.copytree(CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/sce_sys', CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/sce_sys')
    elif load == 'SYSTEM':
        if sys.platform.__contains__('linux'):
            print 'Executing: ./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"'
            os.system('./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"')
            print 'Executing: ./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"'
            os.system('./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"')
        elif sys.platform.__contains__('win'):
            print 'Executing: psvimg-extract.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"'
            os.system('psvimg-extract.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"')
            print 'Executing: psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"'
            os.system('psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"')
        print 'Copying File: ' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvinf' + ' To: ' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvinf'
        if os.path.exists(CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvinf'):
            shutil.copy(CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvinf', CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvinf')
    if resign == False:
        tkMessageBox.showinfo(title='Extract', message='Extraction Complete!')
        print 'Opening Folder: ' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup
        openFolder(CMA + '/EXTRACTED/' + load + '/' + cmaBackup)
        import unsign
        unsign.vp_start_gui()
    elif resign == True:
        loaad = load
        accSelect_support.resignVars(cmaBackup, load)
        backupType_support.action('resign2')
        accSelect.vp_start_gui()
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global root
    global w
    global top_level
    w = gui
    top_level = top
    root = top


def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import unsign
    unsign.vp_start_gui()

def getAccount():
    return account
