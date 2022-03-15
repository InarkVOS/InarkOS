from curses import *
import random
import sys

def run():
	hexltrs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
	win = initscr()
	win.nodelay(1)
	a = False
	while 1:
		if a == True:
			endwin()
			break
		for y in range(win.getmaxyx()[0]):
			thing = ''
			key = win.getch()
			if key != -1:
				a = True
			if key == -1:
				for x in range(win.getmaxyx()[1]-1):
					thing += random.choice(hexltrs)
				win.addstr(y%win.getmaxyx()[0], 0, thing)
				win.refresh()
