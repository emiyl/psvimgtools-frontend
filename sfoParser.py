"""
    Python SFO Parser by: Chris Kreager a.k.a LanThief
    Date: January 17, 2006
"""



def str2hex(s, size=8):
    "String converter to hex"
    if (len(s) * size) <= 32:
        h = 0x0
    else:
        h = 0x0L
    for c in s:
        h = (h << size) | ord(c)
    return h


def hex2hexList(h, size=8, reverse=True):
    "hex converter to hex list"
    return hex2hexList_charList(h, size, reverse, False)


def hex2hexList_charList(h, size=8, reverse=True, ischr=True):
    "hex converter to either chr list or hex list"
    l = []
    if h == 0x0:
        if ischr:
            l.append(chr(h))
        else:
            l.append(h)
        return l
    while h:
        _h = (h & mask_bit(size))
        if ischr:
            horc = chr(_h)
        else:
            horc = _h
        l.append(horc)
        h = (h >> size)
    if reverse: l.reverse()
    return l


def str2hexList(s, size=8, reverse=True):
    "String converter to hex list"
    return hex2hexList(str2hex(s), size, reverse)


def mask_bit(size=8):
    if size > 32:
        return (0x1L << size) - (0x1)
    else:
        return (0x1 << size) - (0x1)


import sys

PsfMagic = "\0PSF"
PsfDefaultFile = "PARAM.SFO"


def le32(bits):
    bytes = str2hexList(bits)
    result = 0x0
    offset = 0
    for byte in bytes:
        result |= byte << offset
        offset += 8
    return result



def le16(bits):
    bytes = str2hexList(bits)
    if len(bytes) > 1:
        return (bytes[0] | bytes[1] << 8)
    return (bytes[0] | 0x0 << 8)


class PsfHdr:
    size = 20

    def __init__(self, bits):
        self.size = 20
        self.data = bits[:self.size]
        self.magic = str2hexList(bits[:4])
        self.rfu000 = str2hexList(bits[4:8])
        self.label_ptr = bits[8:12]
        self.data_ptr = bits[12:16]
        self.nsects = bits[16:20]

    def __len__(self):
        return self.size


class PsfSec:
    size = 16

    def __init__(self, bits):
        self.size = 16
        self.data = bits[:self.size]
        self.label_off = bits[:2]
        self.rfu001 = bits[2:3]
        self.data_type = str2hex(bits[3:4])  # string=2, integer=4, binary=0
        self.datafield_used = bits[4:8]
        self.datafield_size = bits[8:12]
        self.data_off = bits[12:16]

    def __len__(self):
        return self.size


psf = None


def main(filename):
    argc = len(sys.argv)
    argv = sys.argv
    global psf

    PsfFilename = (argv[1:2], PsfDefaultFile)[argc != 2]  # I use a slice [1:2] to avoid IndexError

    PsfFile = open(filename, 'rb')
    psf = PsfFile.read()
    PsfFile.close()

    if not psf.find(PsfMagic) == 0:
        print "This file is not a PSF file ! [PSF Magic == 0x%08X]\n" % str2hex(PsfMagic)

    psfheader = PsfHdr(psf)
    psfsections = PsfSec(psf[PsfHdr.size:])
    psflabels = psf[le32(psfheader.label_ptr):]
    psfdata = psf[le32(psfheader.data_ptr):]

    index = PsfHdr.size
    sect = psfsections

    for i in xrange(0, le32(psfheader.nsects)):
        le16(sect.label_off), le32(sect.data_off),
        le32(sect.datafield_size),
        le32(sect.datafield_used), sect.data_type,
        str2hex(sect.rfu001),
        if psflabels[le16(sect.label_off):].split('\x00')[0] == "TITLE":
            TITLE = psfdata[le32(sect.data_off):].split('\x00\x00')[0]
            if TITLE.__contains__("("):
                TITLE = TITLE.replace("(","[")
            if TITLE.__contains__(")"):
                TITLE = TITLE.replace(")","]")
            ##Found a bug where if it wouldnt dump the Gravity Rush Demo because it was called "Gravity Rush (DEMO)"
            ##Which conficts with the way i find titleid's
            print "Found: "+TITLE
            return TITLE
        index += PsfSec.size
        sect = PsfSec(psf[index:])



if __name__ == '__main__':
    import sys

#I modified the code a little bit so it would only give TITLE