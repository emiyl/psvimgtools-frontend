import getopt
import sys
import tkMessageBox
import urllib

import cmaDir_support
import defs
import easyinstallers.CmBackup.main as CMBACKUP
import main

# Requires BPlistLib -- https://github.com/tungol/bplistlib


import os
import fnmatch

import sign_support
version = "v0.4"
print "/--PSVIMGTOOLS-FRONTEND "+version+"--\ "
print '|  GUI BY SILICAANDPINA!        |'
print '|  CLI BY YIFANLU / MOLECULE    |'
print '\-------------------------------/'
opts, args = getopt.getopt(sys.argv[1:], 'x:y:')
try:
 if args[0] == "m":
        print "Running in MANUAL mode."
        print "In this mode you have to setup the application yourself."
        print "The only reason i added this mode is because people keep getting errors where\nthe application opens and then closes immediatley."
        print "So yea you just need to enter a few things: "
        PSNName = raw_input("What is your PSN Account Name? ")
        aid = raw_input("What is your AID/PSID? ")
        CmaDir = raw_input("Where is your QCMA Backups Directory? ")
        print "Downloading key.. - Make sure you are connected to the internet and have access to cma.henkaku.xyz!"
        urllib.urlretrieve('http://cma.henkaku.xyz/?aid=' + aid, 'tempKey.html')
        print "Key Downloaded."
        key = defs.getKey()
        print "Set 'key' to defs.getKey"
        text_file = open('keys/' + PSNName, 'w+')
        print "Opening text file keys/"+PSNName
        text_file.write(key)
        print "Writing " + key + " to file.."
        text_file.close()
        print "Closing text file.."
        text_file = open('accounts/' + PSNName, 'w+')
        print "Opening text file accounts/" + PSNName
        text_file.write(aid)
        print "Writing "+aid +" to file.."
        text_file.close()
        print "Closing text file."
        text_file = open('cmadir.txt', 'w+')
        print "Opening cmadir.txt"
        text_file.write(CmaDir)
        print "Writing "+CmaDir+" To File"
        text_file.close()
        print "Closing Text File."
        raw_input("All done! the application will now close.. just open it again and it SHOULD work..\nif it doesnt work. please just post an issue on github dont spam my comments\nAlso write more than just 'it doesnt work' thats.. not very usefull.")
        sys.exit()
except IndexError:
    ""

try:
    if args[0] == "s":
        print "Skipping Initial Check.."
        print "Problems may occur when doing this..."
        print "Running GUI.."
        main.vp_start_gui()
except IndexError:
    ""

try:
    if args[0] != "" and args[0] != "noUpdateCheck":
        print "Extracting CMBackup File"
        CMBACKUP.vp_start_gui(args[0])
except IndexError:
    ""

try:
    if args[0] == "noUpdateCheck":
        print "Skipping Update Check."
except IndexError:
    print "Checking for updates"
    defs.checkForUpdate(version)

if not os.path.exists("accounts"):
    os.makedirs("accounts")
if not os.path.exists("keys"):
    os.makedirs("keys")

a = 0

print "Setting Up EasyInstallers."
for root, dir, files in os.walk("*"):
    for items in fnmatch.filter(dir, "*"):
        sys.path.append(items)

print ("Checking CMADir.txt")
if not os.path.exists("cmadir.txt"):
    print "CMADir Doesnt Exist, Obtaining From QCMA!"
    defs.autoCMA()

else:
    print("CHECK OK")

print ("Checking Account List")
if os.listdir("accounts") == [] and os.listdir("keys") == []:
    print("No Accounts Found, Auto-Generating From QCMA!")
    defs.autoAccount()
else:
    print("CHECK OK")






CMA = defs.getCmaDir()


if sys.platform.__contains__("linux"):
    print("Making Psvimgtools Executable")
    print("Executing: chmod 777 psvimg-create")
    print("Executing: chmod 777 psvimg-extract")
    print("Executing: chmod 777 psvmd-decrypt")
    os.system("chmod 777 psvimg-create")
    os.system("chmod 777 psvimg-extract")
    os.system("chmod 777 psvmd-decrypt")



if CMA != "":
    print("Checking for "+CMA+"/EXTRACTED, /APP, /PGAME, /PSGAME, /PSM and /SYSTEM")
    if os.path.exists(CMA):
        if not os.path.exists(CMA+"/EXTRACTED"):
            print("/EXTRACTED Directory Does Not Exist, Creating!")
            os.makedirs(CMA+"/EXTRACTED")
        print "Checking for EXTRACTED/APP"
        if not os.path.exists(CMA + "/EXTRACTED/APP"):
            print ("/EXTRACTED/APP Directory Does Not Exist, Creating!")
            os.makedirs(CMA + "/EXTRACTED/APP")
        else:
            print("/EXTRACTED/APP Exists!")
        print "Checking for EXTRACTED/PGAME"
        if not os.path.exists(CMA + "/EXTRACTED/PGAME"):
            print ("/EXTRACTED/PGAME Directory Does Not Exist, Creating!")
            os.makedirs(CMA + "/EXTRACTED/PGAME")
        else:
            print("/EXTRACTED/PGAME Exists!")
        print "Checking for EXTRACTED/PSGAME"
        if not os.path.exists(CMA + "/EXTRACTED/PSGAME"):
            print ("/EXTRACTED/PSGAME Directory Does Not Exist, Creating!")
            os.makedirs(CMA + "/EXTRACTED/PSGAME")
        else:
            print("/EXTRACTED/PSGAME Exists!")
        print "Checking for EXTRACTED/PSM"
        if not os.path.exists(CMA + "/EXTRACTED/PSM"):
            print ("/EXTRACTED/PSM Directory Does Not Exist, Creating!")
            os.makedirs(CMA + "/EXTRACTED/PSM")
        else:
            print("/EXTRACTED/PSM Exists!")
        print "Checking for EXTRACTED/SYSTEM"
        if not os.path.exists(CMA + "/EXTRACTED/SYSTEM"):
            print ("/EXTRACTED/SYSTEM Directory Does Not Exist, Creating!")
            os.makedirs(CMA + "/EXTRACTED/SYSTEM")
        else:
            print("/EXTRACTED/SYSTEM Exists!")
    else:
        print(CMA + " Does Not Exist! Your CMA Dir Is Invalid?")
        print("Re-Generating CMADir...")
        defs.autoCMA()
        quit()
    print("Check OK All Required Files Where Found/Created")


print("Checking For 64-Bit")
is_64bits = sys.maxsize > 2**32

if is_64bits == 0:
    print("Running in 32-Bit mode.")
else:
    print("Test OK!")
print("Running OS Check")
if sys.platform.__contains__("linux"):
    print "Test OK!, sys.platform: "+sys.platform
    print("Starting GUI")
    main.vp_start_gui()
elif sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
    print "Test OK!, sys.platform: " + sys.platform
    print "Registering .cmbackup as a known filetype.."
    print "Executing: assoc .cmbackup=CmbackupFile"
    os.system("assoc .cmbackup=CmbackupFile")
    print 'Executing: ftype CmbackupFile="'+defs.getWorkingDir()+'"'
    os.system('ftype CmbackupFile="'+defs.getWorkingDir()+'"')
    print("Starting GUI")
    main.vp_start_gui()
elif sys.platform.__contains__("darwin"):
    print "Test OK!, sys.platform: " + sys.platform
    print "MacOS Is currently in BETA! Please report any bugs you may find."
    print("Starting GUI")
    main.vp_start_gui()
else:
    tkMessageBox.showinfo(title="Error 009", message="Your OS Is Not Supported!")
    quit()

sys.exit()

