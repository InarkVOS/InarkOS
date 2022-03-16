import time as t
import os

def clearline():
    print('\r' + ' '*80)
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
