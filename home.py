from commandhandler import check
import curses as c


def mainwindow(win):
    c.endwin()
    print("Please know that this is a beta build.")
    while True:
        option = input("-> ")
        check(option)
