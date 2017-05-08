import os
import shutil
import tkFileDialog
import tkMessageBox
import zipfile

import sys

import accSelect
import accSelect_support
import defs
import sign_support


def cmbackupextract(account,file=""):
    if file == "":
        cmfile = tkFileDialog.askopenfilename(title='Select cmbackup',filetypes=[('Unsigned CMA Backup Files', '*.cmbackup')])
    else:
        cmfile = file
    zf = zipfile.ZipFile(cmfile)
    try:
        zf.extract(member="load.txt", path="temp")
        zf.extract(member="TitleID.txt", path="temp")
    except KeyError:
        tkMessageBox.showerror(title="Error 094", message="Invalid .cmbackup!")
    zf.close()
    load = open('temp/load.txt', 'r')
    loadtype = load.read()
    load.close()
    backupfile = open('temp/TitleID.txt', 'r')
    CMABACKUP = backupfile.read()
    backupfile.close()
    os.remove("temp/load.txt")
    os.remove("temp/TitleID.txt")
    os.removedirs("temp")
    defs.extractZip(src=cmfile, dst=defs.getCmaDir() + '/EXTRACTED/' + loadtype + "/" + CMABACKUP)
    os.remove(defs.getCmaDir() + '/EXTRACTED/' + loadtype + "/" + CMABACKUP + "/" + "load.txt")
    os.remove(defs.getCmaDir() + '/EXTRACTED/' + loadtype + "/" + CMABACKUP + "/" + "TitleID.txt")
    if os.path.exists(defs.getCmaDir() + '/EXTRACTED/' + loadtype + "/" + CMABACKUP + '/savedata') == True:
        savedata = tkMessageBox.askyesno(title="Savedata",message="This .cmbackup contains savedata, would you like to use this savedata?\nYou may have problems with trophy eligiby if you do.")
        if savedata == False:
            shutil.rmtree(defs.getCmaDir() + '/EXTRACTED/' + loadtype + "/" + CMABACKUP + '/savedata')
            os.remove(defs.getCmaDir() + '/EXTRACTED/' + loadtype + "/" + CMABACKUP + '/savedata.psvmd-dec')
    sign_support.goSign(account,loadtype,CMABACKUP,True)
    tkMessageBox.showinfo(title="Done!",message="Done!, Backup Created.")
    if file != "":
        sys.exit()
