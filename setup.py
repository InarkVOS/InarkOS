import os
from os.path import exists
import getpass
import hashlib
print("Please wait until we install the dependencies...")
os.system("pip3 install requests psutil colorama termcolor py-cpuinfo")
if os.name == 'nt':
    os.system('pip install windows-curses')
else:
    os.system('pip install curses')
os.mkdir("pkgprograms")
print("If you wanna use g* packages do pip install pyqt5")
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
