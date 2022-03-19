import time as t
import os

def clearline():
    print('\r' + ' '*(os.get_terminal_size()[0]-1))
    return ''

def goup():
    print('\033[A')
    return ''

def system(cmd):
    if cmd == 'clear' or cmd == 'cls':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    else:
        os.system(cmd)

def progressbar(style, val, scl, end='\n'):
    if style == 0: # ██████░░░░░░
        if val%5 != 0:print('█'*(val//scl) + '░'*((100-val)//scl) + '░ ' + str(val) + '%', end=end)
        else:print('█'*(val//scl) + '░'*((100-val)//scl) + ' ' + str(val) + '%', end=end)