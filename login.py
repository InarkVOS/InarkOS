from home import *
from genericpath import isfile
import os
from os.path import exists
import getpass
import hashlib
import time

if os.listdir('MainDrive/Users') == []:
    print('No users have been created please run init.py')
    exit()
else:
    username = input("Username: ")
    password = getpass.getpass("Password (No echo): ")
    encp = password.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    pswdir = open(f'MainDrive/Users/{username}/pswdir', 'r')
    usrdir = open(f'MainDrive/Users/{username}/usrdir', 'r')
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
            mainwindow()
