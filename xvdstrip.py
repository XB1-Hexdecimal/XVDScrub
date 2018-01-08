import sys

if len(sys.argv) > 1:
    xvdpath = sys.argv[1]
    fh = open(sys.argv[1], "r+b")
    fh.seek(0x896)
    zerobytes = "00000000000000".encode()
    zerobytes2 = "X000000-000".encode()
    fh.write(zerobytes)
    fh.seek(0x8CC)
    fh.write(zerobytes2)
    fh.close()
    print("Identifiable info was overwritten. ")
else:
    print("Please pass a path to a XVD/UWA.")
    print("xvdstrip.py pathtoxvd")
