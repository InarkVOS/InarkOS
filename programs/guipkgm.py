import curses as c
import os

selidx = 0
menu = []
f = open('programs/pkgnames.txt', 'r').readlines()
for i in range(len(f)):
    menu.append(f[i].split(' ')[0])

def drawMenu(win, menu):
    c.init_pair(1, c.COLOR_GREEN, c.COLOR_BLACK)
    c.init_pair(2, c.COLOR_RED, c.COLOR_BLACK)
    for i in range(len(menu)):
        if selidx == i:
            win.attron(c.A_REVERSE)
        else:
            win.attroff(c.A_REVERSE)
        if menu[i]+'.py' in os.listdir('pkgprograms'):
            win.addstr(i+1,0,menu[i])
            win.addstr(i+1,len(menu[i])," "*(20-len(menu[i]))+"(Installed)",c.color_pair(1))
        else:
            win.addstr(i+1,0,menu[i])
            win.addstr(i+1,len(menu[i])," "*(20-len(menu[i]))+"(Not Installed)",c.color_pair(2))


def refresh(win):
    win.attroff(c.A_REVERSE)
    win.clear()
    win.addstr(0,0,"Packages:")
    drawMenu(win, menu)

def run():
    global selidx
    win = c.initscr()
    c.start_color()
    c.noecho()
    c.curs_set(0)
    win.keypad(True)

    win.addstr(0,0,"Packges:")

    drawMenu(win, menu)

    while 1:
        refresh(win)
        key = win.getch()

        if key == c.KEY_DOWN and selidx != len(menu)-1:
            selidx += 1
            drawMenu(win, menu)
        if key == c.KEY_UP and selidx != 0:
            selidx -= 1
            drawMenu(win, menu)
        if chr(key) == '\n':
            c.endwin()
            return menu[selidx]


    win.getch()
