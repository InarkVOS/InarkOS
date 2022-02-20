import os
import getpass
import hashlib
print("Please wait until we install the dependencies...")
os.system("pip3 install requests psutil colorama termcolor py-cpuinfo")
if os.name == 'nt':
    os.system('pip install windows-curses')
print("If you wanna use g* packages do pip install pyqt5")
print("Done...")
if os.path.exists('MainDrive/Users'):
    os.system('python3 bootscreen.py')
else:
    username = input("Username: ")
    password = getpass.getpass("Password (No echo): ")
    encp = password.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    os.mkdir('pkgprograms')
    os.mkdir('MainDrive/')
    os.mkdir('MainDrive/Users/')
    os.mkdir(f'MainDrive/Users/{username}')
    os.mkdir('ubin/')
    usrdir = open(f"MainDrive/Users/{username}/usrdir","w").write(username)
    pswdir = open(f"MainDrive/Users/{username}/pswdir","w").write(hash)
