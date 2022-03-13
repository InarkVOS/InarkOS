from curses import *
from colorama import Fore
from colorama import init
import time
import os
import random
import sys

targets = [
    'O Create System Users.',
    'O Entropy Daemon based on the HAVEGE algorithm.',
    '# Starting Rule-based Manager for Device Events and Files.',
    'O Reached target Encrypting Volumes.',
    'O Listening on Process Core Dump Socket.',
    'O Reached target Remote File Systems.',
    'O Started Create list of required static device nodes.',
    'O Waiting for udev To Complete Device Initialization.',
    'O Monitoring of LVM2 mirrors, etc. using dmeventd or progress polling.',
    'O Started Apply Kernel Variables.',
    'O Mounted Debug File System.',
    'O Mounted Configuration File System.',
    'O Mount POSIX Message Queue File System.',
    'O Started Journal service.',
    'O Started Remount Root and Kernel File Systems.',
    '# Starting udev Coldplug all Devices...',
    '# Starting Flush Journal to Persistent Storage...',
    '# Starting Create Static Device Nodes in /dev...',
    '# Starting Load/Save Random Seed...',
    'O Started Load/Save Random Seed.',
    'O Started udev Coldplug all Devices.',
    'O Started Create Static Device Nodes in /dev.',
    '# Starting udev Kernel Device Manager...',
    'O Reached target Local File Systems (Pre).',
    'O Started Flush Journal to Persistent Storage.',
    'O Started udev Kernel Device Manager.',
    'O Found device Samsung_SSD_850_PRO_512GB SYSTEM.',
    '# Mounting /boot...',
]

def fancyboot():
    for target in targets:
        _ = target.split(' ')[0]
        if _ == 'O':
            print(f'[  {Fore.GREEN}' + 'OK' + f'{Fore.WHITE}  ] ' + target[2:])
        elif _ == '#':
            print(' '*9 + str(target[2:]))
        elif _ == 'F':
            print(f'[{Fore.RED}' + 'FAILED' + f'{Fore.WHITE}]' + target[2:])
        time.sleep(random.uniform(0.05, 0.07))
    time.sleep(0.07)
    
clear_command = 'clear'
if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'

if '--noboot' not in sys.argv:

    init()
    # Please not this is just fanciness. You can always skip bootscreen by --bcomp

    os.system(clear_command)

    fancyboot()

    try:
        win = initscr()
        start_color()
        curs_set(0)

        y, x = win.getmaxyx()
        y = y // 2
        x = x // 2
        scl = 20
        offset = 3
        yoffset = y - 15


        init_pair(1, COLOR_CYAN, COLOR_BLACK)

        win.attron(color_pair(1))
        win.addstr(y + yoffset - 5 - offset, x - 27, "██████╗  █████╗ ██████╗ ██╗  ██╗       █████╗  ██████╗")
        win.addstr(y + yoffset - 4 - offset, x - 27, "██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝      ██╔══██╗██╔════╝")
        win.addstr(y + yoffset - 3 - offset, x - 27, "██║  ██║███████║██████╔╝█████═╝ █████╗██║  ██║╚█████╗ ")
        win.addstr(y + yoffset - 2 - offset, x - 27, "██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════╝██║  ██║ ╚═══██╗")
        win.addstr(y + yoffset - 1 - offset, x - 27, "██████╔╝██║  ██║██║  ██║██║ ╚██╗      ╚█████╔╝██████╔╝")
        win.addstr(y + yoffset - 0 - offset, x - 27, "╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚════╝ ╚═════╝ ")

        for i in range(scl + 1):
            win.addstr(y + 8, x - round(scl / 2) - 2, "[" + "#" * i + "-" * (scl - i) + ']')
            win.addstr(y + 10, x - round(scl / 2) - 2 + 6, "Booting...")
            win.refresh()
            time.sleep(0.07)

        time.sleep(0.6)
        win.attroff(color_pair(1))
        endwin()
    except:
        pass

os.system(clear_command)

os.system("python3 init.py --bcomp")