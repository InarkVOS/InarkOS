import os
import getpass
import hashlib
os.system('cls')
print("If you wanna use g* packages do pip install pyqt5")
print("Done...")

if 'MainDrive' in os.listdir('.'):
    if os.name == 'nt':
        os.system('powershell -c "rm MainDrive"')
    else:
        os.system('rm MainDrive -rf')

os.mkdir('MainDrive/')
os.mkdir('MainDrive/Users/')

if len(os.listdir('MainDrive/Users')) > 0:
    os.system(f'{python} bootscreen.py')
else:
    username = input("Username: ")
    password = getpass.getpass("Password (No echo): ")
    encp = password.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    os.mkdir(f'MainDrive/Users/{username}')
    if not os.path.exists('ubin'):
        os.mkdir('ubin/')
    usrdir = open(f"MainDrive/Users/{username}/usrdir", "w").write(username)
    pswdir = open(f"MainDrive/Users/{username}/pswdir", "w").write(hash)
