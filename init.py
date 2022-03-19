import os, platform
from os.path import exists
import hashlib
import sys

python = "python3"
if platform.system() == "Windows": python = "python"

if '--bcomp' in sys.argv:
    try:
        if '--nologin' in sys.argv:
            username = sys.argv[sys.argv.index('--username')+1]
            password = sys.argv[sys.argv.index('--password')+1]
            if username not in os.listdir('MainDrive/Users'):
                print('Username is incorrect')
            else:
                password_f = open(f'MainDrive/Users/{username}/pswdir', 'r').read()
                username_f = open(f'MainDrive/Users/{username}/usrdir', 'r').read()
                encp = password.encode()
                d = hashlib.sha256(encp)
                hash = d.hexdigest()
                if hash == password_f and username == username_f:
                    import home
                    home.mainwindow(username)
        else:
            if exists('MainDrive/Users/'):
                print("Found file redirecting")
                os.system(f"{python} login.py")
            else:
                print("File not found redirecting")
                os.system(f"{python} setup.py")
    except Exception as e:
        data = open('sys_settings.cfg').readlines()
        for i in range(len(data)):
            if data[i].split('=')[0] == 'showerrors':
                if data[i].split('=')[1] == 'True':
                    print(e)
else:
    os.system(f"{python} bootscreen.py")
