import csv
import os
import requests
import ConfigParser

import sys

import defs

nps_games = "https://docs.google.com/spreadsheets/d/18PTwQP7mlwZH1smpycHsxbEwpJnT8IwFP7YZWQT7ZSs/export?format=csv&id=18PTwQP7mlwZH1smpycHsxbEwpJnT8IwFP7YZWQT7ZSs&gid=1180017671"
def updateKeyDatabase():
    print "Updating: "+defs.getWorkingDir()+"/keydb.ini"
    configParser = ConfigParser.RawConfigParser()
    configParser.read(defs.getWorkingDir()+"/keydb.ini")
    try:
        configParser.add_section("zrif")
        configParser.add_section("klicense")
    except:
        ""
    try:
        open("temp.csv","wb").write(requests.get(nps_games).text.encode("utf-8"))
        with open('temp.csv', 'rb') as csvfile:
            keydb = csv.DictReader(csvfile)
            for row in keydb:
                try:
                    if row['zRIF'] == "MISSING" or row['zRIF'] == "NOT REQUIRED" or row['zRIF'] == "Probably not required":
                        ""
                    else:
                        configParser.set(defs.getKeyType(row['zRIF']),row['Title ID'].upper(),row['zRIF'])
                except ConfigParser.Error:
                    print("Failed to add key for "+row['Title ID'])

        with open(defs.getWorkingDir()+"/keydb.ini","wb") as configfile:
            configParser.write(configfile)
        os.remove("temp.csv")
    except requests.exceptions.ConnectionError:
        print "Unable To Connect To Server.."

def addKey(titleid,key):
    configParser = ConfigParser.RawConfigParser()
    configParser.read(defs.getWorkingDir()+"/keydb.ini")
    try:
        configParser.set(defs.getKeyType(key),titleid,key)
    except:
        print("Failed to add key for "+titleid)
    with open(defs.getWorkingDir()+"/keydb.ini") as configfile:
        configParser.write(configfile)

def getKey(titleid):
    print "Looking up key for "+titleid
    configParser = ConfigParser.RawConfigParser()
    configParser.read(defs.getWorkingDir()+"/keydb.ini")
    try:
        print("Checking zRIF..")
        key = configParser.get("zrif",titleid).upper()
        print "Key found in zRIF"
        return key
    except ConfigParser.NoOptionError:
        print "Key not found in zRIF"
    try:
        print("Checking klicense..")
        key = configParser.get("klicense",titleid).upper()
        print("Key found in klicense")
        return key
    except:
        print "key not found in klicense"

    print "Key is not found in the key database."
    return 404

def decrypt(titleid):
    print("Preparing to PFS decrypt "+titleid)
    rifkey = getKey(titleid)
    CMADir = defs.getCmaDir()
    if defs.getKeyType(rifkey) == "zrif":
        keyType = "--zRIF="
    else:
        keyType = "--klicensee="
    if rifkey == 404:
        return 404
    if sys.platform.__contains__("linux"):
        #cmd = defs.getWorkingDir()+'/psvpfsparser --title_id_src="'+CMADir+'/EXTRACTED/APP/'+titleid+'/app/ux0_temp_game_'+titleid+'_app_'+titleid+'" --title_id_dst="'+CMADir+'/EXTRACTED/DPFS/'+titleid+'" '+str(keyType)+str(rifkey)+' --f00d_url=cma.henkaku.xyz'
        cmd = '/home/silicaandpina/psvita/GIT/psvpfstools/cmake/output/Release/psvpfsparser --title_id_src="'+CMADir+'/EXTRACTED/APP/'+titleid+'/app/ux0_temp_game_'+titleid+'_app_'+titleid+'" --title_id_dst="'+CMADir+'/EXTRACTED/DPFS/'+titleid+'" '+str(keyType)+str(rifkey)+' --f00d_url=cma.henkaku.xyz'
        print "Executing: "+cmd
        #cmd = "./psvpfsparser --tile_id_src="+titleid
        os.system(cmd)
decrypt("PCSF00123")
