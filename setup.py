import os
from os.path import exists
import getpass
import hashlib
print("Please wait until we install the dependencies...")
os.system("pip3 install requests psutil colorama termcolor py-cpuinfo")
if os.name == 'nt':
    os.system('pip install windows-curses')
print("If you wanna use g* packages do pip install pyqt5")
print("Done...")
if os.path.exists('MainDrive/Users'):
    pass
else:
    username = input("Username: ")
    password = getpass.getpass("Password (No echo): ")
    encp = password.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    os.mkdir('MainDrive/')
    os.mkdir('MainDrive/Users/')
    os.mkdir(f'MainDrive/Users/{username}')
    usrdir = open(f"MainDrive/Users/{username}/usrdir","w").write(username)
    pswdir = open(f"MainDrive/Users/{username}/pswdir","w").write(hash)
