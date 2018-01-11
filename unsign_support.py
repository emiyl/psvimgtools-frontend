
import os
import subprocess
import sys
from sys import *
import tkFileDialog
import tkMessageBox
from tkFileDialog import askopenfiles
import shutil
import accSelect
import accSelect_support
import backupType
import backupType_support
from shutil import *

import pfs
import sfoParser

if sys.platform.__contains__('linux'):

    def openFolder(path):
        os.system('xdg-open "' + path + '"')


if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):

    def openFolder(path):
        os.system('start "' + path + '"')


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

def getLoad():
    return load

def getResign():
    return resign




def goUnsign(cmaBackup, CMA=defs.getCmaDir(),cmbackup=False,load="",account="",resign=False):
    if cmbackup == True:
            title=sfoParser.main(CMA + '/' + load + '/' + defs.getAid(account) + '/' + cmaBackup + '/sce_sys/param.sfo')
            try:
                location = tkFileDialog.asksaveasfilename(title='Select location',filetypes=[('Unsigned CMA Backup File', '*.cmbackup')],initialfile = title)
            except:
                location = tkFileDialog.asksaveasfilename(title='Select location',filetypes=[('Unsigned CMA Backup File', '*.cmbackup')],initialfile=cmaBackup)
            try:
                print 'location: '+location
            except TypeError:
                tkMessageBox.showerror(title="Error 302",message="ERROR: You did not select a location to create the .cmbackup!")
                import sys
                sys.exit()


    print "Checking if allready extracted backup exists..."
    if os.path.exists(CMA + '/EXTRACTED/' + load + '/' + cmaBackup):
        print 'Backup Found! Removing...'
        shutil.rmtree(CMA + '/EXTRACTED/' + load + '/' + cmaBackup)
        print 'Extracting backup..'
    else:
        print 'Nope! Extracting backup..'
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
            am = 3
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
            foldParams = ['app']
            am = 0
        while am != -1:
            if sys.platform.__contains__('linux') or sys.platform.__contains__('darwin'):
                print 'Executing: ./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '"'
                os.system('./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '"')
                print 'Executing: ./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"'
                os.system('./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"')
                am -= 1
            if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
                print 'Executing: psvimg-extract.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg ' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am]
                os.system('psvimg-extract.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '"')
                print 'Executing: psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"'
                os.system('psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + foldParams[am] + '/' + foldParams[am] + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/' + foldParams[am] + '.psvmd-dec"')
                am -= 1

        if not os.path.exists(CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/sce_sys'):
            print 'Copying Folder: ' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/sce_sys' + ' To: ' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/sce_sys'
            shutil.copytree(CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/sce_sys', CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '/sce_sys')
    elif load == 'SYSTEM':
        if sys.platform.__contains__('linux') or sys.platform.__contains__('darwin'):
            print 'Executing: ./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"'
            os.system('./psvimg-extract -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"')
            print 'Executing: ./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"'
            os.system('./psvmd-decrypt -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"')
        if sys.platform.__contains__('win') and not sys.platform.__contains__("darwin"):
            print 'Executing: psvimg-extract.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"'
            os.system('psvimg-extract.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvimg" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '"')
            print 'Executing: psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"'
            os.system('psvmd-decrypt.exe -K ' + cmaKey + ' "' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvmd" "' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvmd-dec"')
        print 'Copying File: ' + CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvinf' + ' To: ' + CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvinf'
        if os.path.exists(CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvinf'):
            shutil.copy(CMA + '/' + load + '/' + cmaAID + '/' + cmaBackup + '/' + cmaBackup + '.psvinf', CMA + '/EXTRACTED/' + load + '/' + cmaBackup + '.psvinf')
    if resign == False and cmbackup == False:
        tkMessageBox.showinfo(title='Extract', message='Extraction Complete!')
        if pfs.isKeyKnown(cmaBackup):
            if tkMessageBox.askyesno(title="PFS",message="The PFS Key for this application is known\nWould you like to decrypt PFS as well?"):
                pfs.decrypt(cmaBackup)
                tkMessageBox.showinfo(title="PFS",message="PFS Decrypted for " +cmaBackup)
        import unsign
        unsign.vp_start_gui()
    elif resign == True:
        loaad = load
        accSelect_support.resignVars(cmaBackup, load)
        backupType_support.action('resign2')
        accSelect.vp_start_gui()
    elif cmbackup == True:
        print 'Creating .cmbackup'
        print 'Writing load.txt'
        loadtext = open(CMA + '/EXTRACTED/'+load+'/'+cmaBackup+'/load.txt', 'w')
        loadtext.write(load)
        loadtext.close()
        print 'Writing TitleID.txt'
        loadtext = open(CMA + '/EXTRACTED/'+load+'/'+cmaBackup+'/TitleID.txt', 'w')
        loadtext.write(cmaBackup)
        loadtext.close()
        print 'Checking for savedata..'
        if os.path.exists(CMA + '/EXTRACTED/'+load+'/'+cmaBackup+'/savedata'):
            savedata = tkMessageBox.askyesno(title="Savedata",message="This Backup Contains Savedata, Would you like to pack that into the .CMBACKUP File?\nSavedata could potentailly contain personal infomation!!")
            if savedata == False:
                shutil.rmtree(CMA + '/EXTRACTED/'+load+'/'+cmaBackup+'/savedata')
                os.remove(CMA + '/EXTRACTED/'+load+'/'+cmaBackup+'/savedata.psvmd-dec')
        print 'Writing .cmbackup file..'
        defs.zip(src=CMA + '/EXTRACTED/'+load+'/'+cmaBackup,dst=location)
        print "Removing: "+ CMA + '/EXTRACTED/' + load + '/' + cmaBackup
        shutil.rmtree(CMA + '/EXTRACTED/' + load + '/' + cmaBackup)
        print "Done! CMBackup Created!"
        tkMessageBox.showinfo(title='CMBACKUP', message='.cmbackup Created.')
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
