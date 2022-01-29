import os
from os.path import exists
import sys
try:
    if sys.argv[1] == '--nologin':
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
