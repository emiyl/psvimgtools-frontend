import sys
import tkMessageBox
import cmaDir_support
import defs
import main


import os
import fnmatch


if not os.path.exists("accounts"):
    os.makedirs("accounts")
if not os.path.exists("keys"):
    os.makedirs("keys")

a = 0

print "Setting Up Plugins."
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
elif sys.platform.__contains__("win"):
    print "Test OK!, sys.platform: " + sys.platform
    print("Starting GUI")
    main.vp_start_gui()
else:
    tkMessageBox.showinfo(title="Error 009", message="Your OS Is Not Supported!")
    quit()

sys.exit()

