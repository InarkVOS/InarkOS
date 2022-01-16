import os
from os.path import exists
import getpass
import bcrypt
print("Please wait until we install the dependencies...")
os.system("pip3 install --user psutil")
os.system("pip3 install --user gputil")
os.system("pip3 install --user tabulate")
print("Done...")
if exists('pswdir') | exists('usrdir'):
    print("We detected an invalid file (storage) please run init.py again")
    exit(0)
username = input("Username: ")
password = getpass.getpass("Password (No echo): ")
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)
usrdir = open("usrdir","w")
pswdir = open("pswdir","w")
usrdir.write(username)
pswdir.write(hashed)
