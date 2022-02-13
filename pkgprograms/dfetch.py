#!python3

import os
import time
import getpass
import platform
import psutil, cpuinfo
from termcolor import colored
from colorama import init; init()

titleColor = "white"
infoColor = "white"
logoColor = "blue"

def uptime():
        """ Get the device uptime """
        delta = round(time.time() - psutil.boot_time())

        hours, remainder = divmod(int(delta), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        def includeS(text: str, num: int):
            return f"{num} {text}{'' if num == 1 else 's'}"

        d = includeS("day", days)
        h = includeS("hour", hours)
        m = includeS("minute", minutes)
        s = includeS("second", seconds)

        if days:
            output = f"{d}, {h}, {m} and {s}"
        elif hours:
            output = f"{h}, {m} and {s}"
        elif minutes:
            output = f"{m} and {s}"
        else:
            output = s
        return output


cpu_info = (cpuinfo.get_cpu_info())

username = getpass.getuser()
computername = platform.node()
fullname = username + "@" + computername
underscore_list = []
underscore_list.append(len(fullname) * "-")

hostcmd = "wmic csproduct get name"
hostcmd = os.popen(hostcmd).read().split()
hostcmd.remove('Name')

kcmd = "wmic os get Version"
kexeccmd = os.popen(kcmd).read().split()
kexeccmd.remove("Version")

cmd = "wmic path Win32_VideoController get CurrentVerticalResolution,CurrentHorizontalResolution"
size_tuple = tuple(map(int,os.popen(cmd).read().split()[-2::]))

def terminal():
    try:
        term = os.environ.get('TERM')
        return term
    except KeyError:
        return "Unknown"

exec_cmd = "wmic path win32_VideoController get name "
gpu_data = os.popen(exec_cmd).read().split()
gpu_data.remove("Name")

ram = psutil.virtual_memory()
tram = ram[0] / 1024 ** 2
aram = ram[4] / 1024 ** 2


print(colored(f"                                  ..,", f'{logoColor}'))
print(colored(f"                      ....,,:;+ccllll   ",f'{logoColor}') + colored(username, f'{titleColor}') + "@" + colored(computername, f'{titleColor}'))
print(colored(f"        ...,,+:;  cllllllllllllllllll   ", f'{logoColor}') + underscore_list[0])
print(colored(f"  ,cclllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("OS: ", f'{titleColor}') + platform.system() + f" {cpu_info['arch']}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("Host: ", f'{titleColor}') + ' '.join(hostcmd))
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("Kernel: ", f'{titleColor}') + " ".join(kexeccmd))
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("Uptime: ", f'{titleColor}') + f"{uptime()}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("Shell: ", f"{titleColor}") + f"Python {platform.python_version()}")
print(colored(f"                                        ") + colored("Resolution: ", f"{titleColor}") + f"{size_tuple[0]}x{size_tuple[1]}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("Terminal: ", f'{titleColor}') + f"{terminal()}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("CPU: ", f'{titleColor}') + f"{cpu_info['brand_raw']}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored("GPU: ", f'{titleColor}') + " ".join(gpu_data))
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}') + colored(f"RAM: ", f'{titleColor}') + f"{round(aram)} /  {round(tram)}MiB")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", f'{logoColor}'))
print(colored(f"  `'ccllllllllll  lllllllllllllllllll   ", f'{logoColor}'))
print(colored(f"           `'""*::  :ccllllllllllllllll ", f'{logoColor}'))
print(colored(f'                          ````''"*::cll ', f'{logoColor}'))
print(colored(f"                                   ``", f'{logoColor}'))