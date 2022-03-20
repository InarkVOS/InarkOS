import os, platform
from os.path import exists
import hashlib
import sys

python = "python3"
if platform.system() == "Windows": python = "python"

if '--bcomp' in sys.argv:
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
        if '--username' not in sys.argv and '--password' not in sys.argv:
            import home
            home.mainwindow('NOUSR')
    else:
        if exists('MainDrive/Users/'):
            print("Found file redirecting")
            os.system(f"{python} login.py")
        else:
            print("File not found redirecting")
            os.system(f"{python} setup.py")
else:
    os.system(f"{python} bootscreen.py")
