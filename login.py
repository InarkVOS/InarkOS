from genericpath  import isfile
from os.path      import exists
import curses     as c
import cursesutil as cu
import home
import os
import getpass
import hashlib
import time

def run(win):

    if exists('pswdir') | exists('usrdir'):
        win.addstr("Found all files booting")
        cu.incy(win)
    else:
        win.addstr("We detected an invalid file (storage) please run init.py again")
        cu.incy(win)
        exit(0)
    username = cu.getinp(win, "Username: ")
    cu.incy(win)
    password = cu.getinp(win, "Password (No Echo): ", True)
    encp = password.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    pswdir = open('pswdir', 'r')
    usrdir = open('usrdir', 'r')
    readusr = usrdir.read()
    readpsw = pswdir.read()
    if readusr != username:
        win.addstr("Invalid username")
        cu.incy(win)
        exit(0)
    else:
        if readpsw != hash:
            win.addstr("Invalid password")
            cu.incy(win)
            exit(0)
        else:
            win.addstr("Password and username matches")
            home.mainwindow(win)
            cu.incy(win)
