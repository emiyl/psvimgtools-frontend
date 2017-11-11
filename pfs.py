import csv
import os
import requests
import zlib
import base64
def ExtractKey(rif):
    zrif_dict = list(zlib.decompress(base64.b64decode(b"eNpjYBgFo2AU0AsYAIElGt8MRJiDCAsw3xhEmIAIU4N4AwNdRxcXZ3+/EJCAkW6Ac7C7ARwYgviuQAaIdoPSzlDaBUo7QmknIM3ACIZM78+u7kx3VWYEAGJ9HV0=")))
    print zrif_dict
    c = zlib.compressobj(level=9, wbits=10, memLevel=8, zdict=bytes(zrif_dict))
    zlib.compressobj(9)
    bin = c.decompress(rif)
    bin += c.flush()

    if len(bin) % 3 != 0:
      bin += b"\0" * (3 - len(bin) % 3)

    content = rif[0x10:0x40].rstrip(b"\0").decode("ascii")

    return(content, base64.b64encode(bin).decode("ascii"))




nps_games = "https://docs.google.com/spreadsheets/d/18PTwQP7mlwZH1smpycHsxbEwpJnT8IwFP7YZWQT7ZSs/export?format=csv&id=18PTwQP7mlwZH1smpycHsxbEwpJnT8IwFP7YZWQT7ZSs&gid=1180017671"
def updateKeyDatabase():
    if os.path.exists("keydb.ini"):
        os.remove("keydb.ini")
    database = open("keydb.ini","w+")
    database.write("[games]\n")
    open("temp.csv","wb").write(requests.get(nps_games).text.encode("utf-8"))
    with open('temp.csv', 'rb') as csvfile:
        keydb = csv.DictReader(csvfile)
        for row in keydb:
            if row['zRIF'] == "MISSING" or row['zRIF'] == "NOT REQUIRED" or row['zRIF'] == "Probably not required":
                """"""
            else:
                print ExtractKey(row['zRIF'])
                ##database.write(row['Title ID'] + "=" + row['zRIF'] + "\n")
    os.remove("temp.csv")

updateKeyDatabase()

