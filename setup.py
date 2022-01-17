import os
from os.path import exists
import getpass
import hashlib
print("Please wait until we install the dependencies...")
os.sytem("pip3 install --user requests")
tof = input("Install optional dependencies? (Type no if using termux):  ")
if tof:
    os.system("pip3 install --user psutil")
    os.system("pip3 install --user gputil")
    os.system("pip3 install --user tabulate")
print("Done...")
if exists('pswdir') | exists('usrdir'):
    print("We detected an invalid file (storage) please run init.py again")
    exit(0)
username = input("Username: ")
password = getpass.getpass("Password (No echo): ")
encp = password.encode()
d = hashlib.sha256(encp)
hash = d.hexdigest()
usrdir = open("usrdir","w")
pswdir = open("pswdir","w")
usrdir.write(username)
pswdir.write(hash)
