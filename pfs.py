import csv
import os
import requests
import ConfigParser

import sys

import defs

nps_games = "https://nopaystation.com/csv/PSV_GAMES.csv"
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
    with open(defs.getWorkingDir()+"/keydb.ini","wb") as configfile:
        configParser.write(configfile)

def isKeyKnown(titleid):
    configParser = ConfigParser.RawConfigParser()
    configParser.read(defs.getWorkingDir()+"/keydb.ini")
    try:
        if configParser.has_option("zrif",titleid):
            return True
        if configParser.has_option("klicense",titleid):
            return True
        else:
            return False
    except:
        return False

def getKey(titleid):
    print "Looking up key for "+titleid
    configParser = ConfigParser.RawConfigParser()
    configParser.read(defs.getWorkingDir()+"/keydb.ini")
    try:
        print("Checking zRIF..")
        key = configParser.get("zrif",titleid)
        print "Key found in zRIF"
        return key
    except ConfigParser.NoOptionError:
        print "Key not found in zRIF"
    try:
        print("Checking klicense..")
        key = configParser.get("klicense",titleid)
        print("Key found in klicense")
        return key
    except:
        print "Key not found in klicense"

    print "Key is not found in the key database."
    return 404
"""
def decryptSavedata(titleid):
    CMADir = defs.getCmaDir()
    if os.path.exists(CMADir+'/EXTRACTED/APP/'+titleid+'/savedata/ux0_temp_game_'+titleid+'_savedata_'+titleid):
        if sys.platform.__contains__("linux" or "darwin"):
            cmd = defs.getWorkingDir()+'/psvpfsparser --title_id_src="'+CMADir+'/EXTRACTED/APP/'+titleid+'/savedata/ux0_temp_game_'+titleid+'_savedata_'+titleid+'" --title_id_dst="'+CMADir+'/EXTRACTED/DPFS/SAVEDATA/'+titleid+'" --f00d_url=cma.henkaku.xyz'
        elif sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
            cmd = defs.getWorkingDir() + '\\psvpfsparser.exe --title_id_src="' + CMADir + '\\EXTRACTED\\APP\\' + titleid + '\\savedata\\ux0_temp_game_' + titleid + '_savedata_' + titleid + '" --title_id_dst="' + CMADir + '\\EXTRACTED\\DPFS\\SAVEDATA\\' + titleid + '" --f00d_url=cma.henkaku.xyz'
        print "Executing: "+cmd
        os.system(cmd)"""

def decrypt(titleid):
    print("Preparing to PFS decrypt "+titleid)
    rifkey = getKey(titleid)
    CMADir = defs.getCmaDir()
    if rifkey == 404:
        return 404
    if defs.getKeyType(rifkey) == "zrif":
        keyType = "--zRIF="
    else:
        keyType = "--klicensee="
    if os.path.exists(CMADir+'/EXTRACTED/APP/'+titleid+'/app/ux0_temp_game_'+titleid+'_app_'+titleid):
        if sys.platform.__contains__("linux" or "darwin"):
            cmd = defs.getWorkingDir()+'/psvpfsparser --title_id_src="'+CMADir+'/EXTRACTED/APP/'+titleid+'/app/ux0_temp_game_'+titleid+'_app_'+titleid+'" --title_id_dst="'+CMADir+'/EXTRACTED/DPFS/APP/'+titleid+'" '+str(keyType)+str(rifkey)+' --f00d_url=cma.henkaku.xyz'
        elif sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
            cmd = defs.getWorkingDir() + '\\psvpfsparser.exe --title_id_src="' + CMADir + '\\EXTRACTED\\APP\\' + titleid + '\\app\\ux0_temp_game_' + titleid + '_app_' + titleid + '" --title_id_dst="' + CMADir + '\\EXTRACTED\\DPFS\\APP\\' + titleid + '" ' + str(keyType) + str(rifkey) + ' --f00d_url=cma.henkaku.xyz'
        print "Executing: "+cmd
        os.system(cmd)
    if os.path.exists(CMADir+'/EXTRACTED/APP/'+titleid+'/patch/ux0_temp_game_'+titleid+'_patch_'+titleid):
        if sys.platform.__contains__("linux" or "darwin"):
            cmd = defs.getWorkingDir()+'/psvpfsparser --title_id_src="'+CMADir+'/EXTRACTED/APP/'+titleid+'/patch/ux0_temp_game_'+titleid+'_patch_'+titleid+'" --title_id_dst="'+CMADir+'/EXTRACTED/DPFS/PATCH/'+titleid+'" '+str(keyType)+str(rifkey)+' --f00d_url=cma.henkaku.xyz'
        elif sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
            cmd = defs.getWorkingDir() + '\\psvpfsparser.exe --title_id_src="' + CMADir + '\\EXTRACTED\\APP\\' + titleid + '\\patch\\ux0_temp_game_' + titleid + '_patch_' + titleid + '" --title_id_dst="' + CMADir + '\\EXTRACTED\\DPFS\\PATCH\\' + titleid + '" ' + str(keyType) + str(rifkey) + ' --f00d_url=cma.henkaku.xyz'
        print "Executing: "+cmd
        os.system(cmd)
    """if os.path.exists(CMADir+'/EXTRACTED/APP/'+titleid+'/savedata/ux0_temp_game_'+titleid+'_savedata_'+titleid):
        if sys.platform.__contains__("linux" or "darwin"):
            cmd = defs.getWorkingDir()+'/psvpfsparser --title_id_src="'+CMADir+'/EXTRACTED/APP/'+titleid+'/savedata/ux0_temp_game_'+titleid+'_savedata_'+titleid+'" --title_id_dst="'+CMADir+'/EXTRACTED/DPFS/SAVEDATA/'+titleid+'" --f00d_url=cma.henkaku.xyz'
        elif sys.platform.__contains__("win") and not sys.platform.__contains__("darwin"):
            cmd = defs.getWorkingDir() + '\\psvpfsparser.exe --title_id_src="' + CMADir + '\\EXTRACTED\\APP\\' + titleid + '\\savedata\\ux0_temp_game_' + titleid + '_savedata_' + titleid + '" --title_id_dst="' + CMADir + '\\EXTRACTED\\DPFS\\SAVEDATA\\' + titleid + '" --f00d_url=cma.henkaku.xyz'
        print "Executing: "+cmd
        os.system(cmd)"""
