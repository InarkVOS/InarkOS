from curses import *
from colorama import Fore
from colorama import init
import time
import os
init()
# Please not this is just fanciness. You can always skip bootscreen by --bcomp
targets = [
    'Reached target Encrypting Volumes.',
    'Listening on Process Core Dump Socket.',
    'Reached target Remote File Systems.',
    'Started Create list of required static device nodes.',
    'Started Apply Kernel Variables.',
    'Mounted Debug File System.',
    'Mounted Configuration File System.',
    'Mount POSIX Message Queue File System.',
    'Started Journal service.',
    'Started Remount Root and Kernel File Systems.',
    '# Starting udev Coldplug all Devices...',
    '# Starting Flush Journal to Persistent Storage...',
    '# Starting Create Static Device Nodes in /dev...',
    '# Starting Load/Save Random Seed...',
    'Started Load/Save Random Seed.',
    'Started udev Coldplug all Devices.',
    'Started Create Static Device Nodes in /dev.',
    '# Starting udev Kernel Device Manager...',
    'Reached target Local File Systems (Pre).',
    'Started Flush Journal to Persistent Storage.',
    'Started udev Kernel Device Manager.',
    'Found device Samsung_SSD_850_PRO_512GB SYSTEM.',
    '# Mounting /boot...',
]

for i in range(len(targets)):
    if targets[i].split(' ')[0] != '#':
        print(f'[  {Fore.GREEN}' + 'OK' + f'{Fore.WHITE}  ] ' + targets[i].replace('# ', ''))
        time.sleep(0.05)
time.sleep(0.2)
command = 'clear'
if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
os.system(command)
time.sleep(1)

win = initscr()
start_color()
curs_set(0)

y,x=win.getmaxyx()
y = int(y/2)
x = int(x/2)
scl = 20
offset = 3
yoffset = y-15


init_pair(1, 6, COLOR_BLACK)

win.attron(color_pair(1))
win.addstr(y+yoffset-5-offset,x-27,"██████╗  █████╗ ██████╗ ██╗  ██╗       █████╗  ██████╗")
win.addstr(y+yoffset-4-offset,x-27,"██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝      ██╔══██╗██╔════╝")
win.addstr(y+yoffset-3-offset,x-27,"██║  ██║███████║██████╔╝█████═╝ █████╗██║  ██║╚█████╗ ")
win.addstr(y+yoffset-2-offset,x-27,"██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════╝██║  ██║ ╚═══██╗")
win.addstr(y+yoffset-1-offset,x-27,"██████╔╝██║  ██║██║  ██║██║ ╚██╗      ╚█████╔╝██████╔╝")
win.addstr(y+yoffset-0-offset,x-27,"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚════╝ ╚═════╝ ")

for i in range(scl+1):
    win.addstr(y+8,x-int(scl/2)-2,"["+"#"*i+"-"*(scl-i)+']')
    win.addstr(y+10,x-int(scl/2)-2+6,"Booting...")
    win.refresh()
    time.sleep(0.1)

time.sleep(0.5)
win.attroff(color_pair(1))
endwin()
os.system("python init.py --bcomp")
