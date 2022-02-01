import getpass
import hashlib
import os

def mkusr():
    username = input("Username: ")
    password = getpass.getpass("Password (No echo): ")
    encp = password.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    try:
        os.mkdir(f'MainDrive/Users/{username}')
    except:
        pass
    pswdir = open(f'MainDrive/Users/{username}/pswdir', 'w').write(hash)
    usrdir = open(f'MainDrive/Users/{username}/usrdir', 'w').write(username)
