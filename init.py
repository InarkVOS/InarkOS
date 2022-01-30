import curses as c
from   curses import wrapper
import os
from os.path import exists
import sys
import cursesutil as cu
from home import *
from login import run

def main(stdscr):
    stdscr.clear()
    try:
        if sys.argv[1] == '--nologin':
            mainwindow()
    except:
        pass
    if exists('pswdir') | exists('usrdir'):
        stdscr.addstr("Found file redirecting")
        cu.incy(stdscr)
        run(stdscr)
    else:
        stdscr.addstr("File not found redirecting")
        cu.incy(stdscr)
        os.system("python setup.py")

wrapper(main)
