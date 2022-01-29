import os
from os.path import exists
import getpass
import hashlib
print("Please wait until we install the dependencies...")
os.system("pip3 install --user requests")
print("Done...")
if exists('pswdir') | exists('usrdir'):
    print("We detected an invalid file (storage) please run init.py again")
    exit(0)
username = input("Username: ")
password = getpass.getpass("Password (No echo): ")
encp = password.encode()
d = hashlib.sha256(encp)
hash = d.hexdigest()
usrdir = open("usrdir","w").write(username)
pswdir = open("pswdir","w").write(hash)
