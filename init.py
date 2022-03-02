import os
from os.path import exists
import sys

if '--bcomp' in sys.argv:
    try:
        if '--nologin' in sys.argv:
            from home import *
            mainwindow()
    except:
        pass
    if os.path.exists('MainDrive/Users/'):
        print("Found file redirecting")
        os.system("python3 login.py")
    else:
        print("File not found redirecting")
        os.system("python3 setup.py")
else:
    os.system("python3 bootscreen.py")
