from home import *
from genericpath import isfile
import os
from os.path import exists
import getpass
import hashlib
import time

if exists('pswdir') | exists('usrdir'):
    print("Found all files booting")
else:
    print("We detected an invalid file (storage) please run init.py again")
    exit(0)
username = input("Username: ")
password = getpass.getpass("Password (No echo): ")
encp = password.encode()
d = hashlib.sha256(encp)
hash = d.hexdigest()
pswdir = open('pswdir', 'r')
usrdir = open('usrdir', 'r')
readusr = usrdir.read()
readpsw = pswdir.read()
if readusr != username:
    print("Invalid username")
    exit(0)
else:
    if readpsw != hash:
        print("Invalid password")
        exit(0)
    else:
        print("Password and username matches")
# Open home
mainwindow()
