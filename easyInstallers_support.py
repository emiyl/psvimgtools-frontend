import tkMessageBox
import defs
import os
import getopt
import sys
import urllib
import urllib2
import main
import pfs
import zipfile
import subprocess
import shutil
import easyinstallers.Whitelister.main as Whitelister
import easyinstallers.ARK.main as ARK
import easyinstallers.HiddenApps.main as HiddenApps
import easyinstallers.VitaShell.main as VitaShell
import easyinstallers.hencore.main as hencore
import easyinstallers.VHBL.main as VHBL
import easyinstallers.UriCaller.main as UriCaller
import easyinstallers.PSMRuntime.main as PSMRuntime
import easyinstallers.Skype.main as Skype
import easyinstallers.RemoveFeatured.main as RemoveFeatured
import easyinstallers.CmBackup.main as cmbackup
import easyinstallers.EmuBubble.main as emububble
import easyinstallers.ClonePSP.main as clonePSP
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

def set_Tk_var():
    global accounts
    accounts = StringVar()


def install(plugin):
    if plugin == 'ARK':
        if tkMessageBox.askyesno(title="3.65?",message="ARK WILL NOT WORK ON 3.65+\nDo you still want to continue?"):
                ARK.vp_start_gui()
    elif plugin == 'VHBL':
        VHBL.vp_start_gui()
    elif plugin == 'HiddenApps':
        HiddenApps.run()
    elif plugin == 'Whitelister':
        Whitelister.vp_start_gui()
    elif plugin == 'UriCaller':
        UriCaller.vp_start_gui()
    elif plugin == 'PSMRuntime':
        PSMRuntime.run()
    elif plugin == 'Skype':
        if tkMessageBox.askyesno(title="3.65?",message="SKYPE WILL NOT WORK ON 3.65+\nDo you still want to continue?"):
                Skype.run()
    elif plugin == 'RemoveFeatured':
        RemoveFeatured.vp_start_gui()
    elif plugin == 'CmBackup':
        cmbackup.vp_start_gui()
    elif plugin == 'EmuBubble':
        emububble.vp_start_gui()
    elif plugin == 'ClonePSP':
        clonePSP.vp_start_gui()
    elif plugin == 'VitaShell':
        VitaShell.run()
    elif plugin == 'hencore':
        if not os.path.exists("easyinstallers/hencore/PCSG90096/app"):
            if tkMessageBox.askyesno(title="Download h-encore?",message="h-encore is not downloaded\nIt will not work unless you download it\nDo you want to download h-encore?"):
                if os.path.exists("hencore"):
                    shutil.rmtree('hencore')
                if os.path.exists("easyinstallers/hencore/PCSG90096/app"):
                    shutil.rmtree('easyinstallers/hencore/PCSG90096/app')
                if os.path.exists("easyinstallers/hencore/PCSG90096/appmeta"):
                    shutil.rmtree('easyinstallers/hencore/PCSG90096/appmeta')
                if os.path.exists("easyinstallers/hencore/PCSG90096/license"):
                    shutil.rmtree('easyinstallers/hencore/PCSG90096/license')
                if os.path.exists("easyinstallers/hencore/PCSG90096/savedata"):
                    shutil.rmtree('easyinstallers/hencore/PCSG90096/savedata')
                if os.path.exists("easyinstallers/hencore/PCSG90096/sce_sys"):
                    shutil.rmtree('easyinstallers/hencore/PCSG90096/sce_sys')
                print 'Downloading bitter smile...\nThis may take a while.'
                os.makedirs("hencore")
                open("hencore/bittersmile.pkg", "wb").write(urllib2.urlopen("http://ares.dl.playstation.net/cdn/JP0741/PCSG90096_00/xGMrXOkORxWRyqzLMihZPqsXAbAXLzvAdJFqtPJLAZTgOcqJobxQAhLNbgiFydVlcmVOrpZKklOYxizQCRpiLfjeROuWivGXfwgkq.pkg").read())
                print 'Downloading pkg2zip...'
                open("hencore/pkg2zip_32bit.zip", "wb").write(urllib2.urlopen("https://github.com/mmozeiko/pkg2zip/releases/download/v1.8/pkg2zip_32bit.zip").read())
                print 'Unzipping pkg2zip...'
                zip_ref = zipfile.ZipFile("hencore/pkg2zip_32bit.zip", 'r')
                zip_ref.extractall("hencore")
                zip_ref.close()
                os.remove("hencore/pkg2zip_32bit.zip")
                print 'Downloading h-encore...'
                open("hencore/h-encore.zip", "wb").write(urllib2.urlopen("https://github.com/TheOfficialFloW/h-encore/releases/download/v1.0/h-encore.zip").read())
                print 'Unzipping h-encore...'
                zip_ref = zipfile.ZipFile("hencore/h-encore.zip", 'r')
                zip_ref.extractall("hencore")
                zip_ref.close()
                os.remove("hencore/h-encore.zip")
                print 'Decrypting pkg...'
                subprocess.call('hencore/pkg2zip -x hencore/bittersmile.pkg')
                print 'Copying game to h-encore folder...'
                source = "app/PCSG90096/"
                dest1 = "hencore/h-encore/app/ux0_temp_game_PCSG90096_app_PCSG90096/"
                files = os.listdir(source)
                for f in files:
                    shutil.move(source+f, dest1)
                shutil.rmtree('app')
                print 'Copying license...'
                shutil.copy2("hencore/h-encore/app/ux0_temp_game_PCSG90096_app_PCSG90096/sce_sys/package/temp.bin", "hencore/h-encore/license/ux0_temp_game_PCSG90096_license_app_PCSG90096")
                shutil.move("hencore/h-encore/license/ux0_temp_game_PCSG90096_license_app_PCSG90096/temp.bin", "hencore/h-encore/license/ux0_temp_game_PCSG90096_license_app_PCSG90096/6488b73b912a753a492e2714e9b38bc7.rif")
                print 'Finishing up...'
                if not os.path.exists("hencore/h-encore/sce_sys/"):
                    os.makedirs("hencore/h-encore/sce_sys/")
                source = "hencore/h-encore/PCSG90096/sce_sys/"
                dest1 = "hencore/h-encore/sce_sys/"
                files = os.listdir(source)
                for f in files:
                    shutil.move(source+f, dest1)
                os.rmdir("hencore/h-encore/PCSG90096/sce_sys")
                os.rmdir("hencore/h-encore/PCSG90096/")
                source = "hencore/h-encore/"
                dest1 = "easyinstallers/hencore/PCSG90096"
                files = os.listdir(source)
                for f in files:
                    shutil.move(source+f, dest1)
                shutil.rmtree('hencore')
                hencore.run()
        else:
            hencore.run()

    else:
        ### Load Custom EasyInstaller. ###
        defs.executePy(defs.getWorkingDir()+'/easyinstallers/'+plugin+'/main.py')

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
    import easyInstallers
    easyInstallers.vp_start_gui()
