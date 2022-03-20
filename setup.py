import os
import getpass
import hashlib
os.system('cls')
print("Done...")

if 'MainDrive' in os.listdir('.'):
    os.rmdir("MainDrive")

os.mkdir('MainDrive/')
os.mkdir('MainDrive/Users/')

username = input("Username: ")
password = getpass.getpass("Password (No echo): ")
encp = password.encode()
d = hashlib.sha256(encp)
hash = d.hexdigest()
os.mkdir(f'MainDrive/Users/{username}')
if 'ubin' not in os.listdir('.'):
    os.mkdir('ubin')
usrdir = open(f"MainDrive/Users/{username}/usrdir", "w").write(username)
pswdir = open(f"MainDrive/Users/{username}/pswdir", "w").write(hash)
os.mkdir(f'MainDrive/Users/{username}/Desktop')
os.system(f'python3 bootscreen.py --noboot --nologin --username {username} --password {password}')