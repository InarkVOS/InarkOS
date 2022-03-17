import os, platform
from os.path import exists
import sys

python = "python3"
if platform.system() == "Windows": python = "python"

if '--bcomp' in sys.argv:
    try:
        if '--nologin' in sys.argv:
            import home
            home.mainwindow('NOUSR')
        else:
            if exists('MainDrive/Users/'):
                print("Found file redirecting")
                os.system(f"{python} login.py")
            else:
                print("File not found redirecting")
                os.system(f"{python} setup.py")
    except:
        pass
else:
    os.system(f"{python} bootscreen.py")
