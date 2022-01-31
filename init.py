import os
from os.path import exists
import sys

if '--bcKvaMlxhBzeBVx' in sys.argv:
    try:
        if '--nologin' in sys.argv:
            from home import *
            mainwindow()
    except:
        pass
    if exists('pswdir') | exists('usrdir'):
        print("Found file redirecting")
        os.system("python login.py")
    else:
        print("Not found file redirecting")
        os.system("python setup.py")
else:
    os.system("python bootscreen.py")
