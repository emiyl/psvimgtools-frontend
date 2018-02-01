import os
import binascii

trpFile = "C:\Users\Matthew\Documents\PSVTROPHYISGOOD\data\decrypted\TRPTRANS.DAT"

trpData = open(trpFile, "rb").read()


def getAccountId():
    return binascii.hexlify(trpData[0x120:0x120+0x8])

def makeCmaAid(aid):
    cmaAid = [aid[i:i + 2] for i in range(0, len(aid), 2)]
    cmaAid.reverse()
    return str(cmaAid)
def getNumberOfUnlockedTrophies():
    return int(str(binascii.hexlify(trpData[0x187:0x187+0x1])),16)

def getNpCommId():
    return trpData[0x170:0x170 + 0x0C]

def getNpCommSign():
    return binascii.hexlify(trpData[0x19C:0x19C + 0x94])

def findDataZone(v):
        begin = 0x2B7
        end = begin + 0xAC
        a = 0
        while a != v:
            begin += 0xAC +0x04
            end = begin + 0xAC
            a += 1
        return {"begin":begin,"end":end}

def getTrophyDataBlock(v):
    begin = findDataZone(v)["begin"]
    end = findDataZone(v)["end"]
    return binascii.hexlify(trpData[begin:end])

a = 0
while a != getNumberOfUnlockedTrophies():
    b = getTrophyDataBlock(a)[132:]
    b = b[:7*2]
    b = int(b,16)
    #b = str(b)[:11]
    print int(b)
    a += 1
