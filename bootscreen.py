import os
import platform
if 'MainDrive' not in os.listdir():
    python = "python3"
    pip = "pip3"
    if platform.system() == "Windows":
        python = "python"
        pip = "pip"

    print("Please wait until we install the dependencies...")

    os.system(f"{pip} install -r req.txt")
    os.system(f"{python} -m pip install -r req.txt")
    if os.name == 'nt':
        os.system(f"{pip}3 install -r req.txt")
        os.system(f"{python}3 -m pip install -r req.txt")
    if os.name == 'nt':
        os.system('pip install windows-curses')
        os.system('pip install msvcrt')
    else:
        os.system('pip install curtsies')
    os.system('cls')
from curses import *
from colorama import Fore
from colorama import init
import time
import random
import sys
import time as t

w, h = os.get_terminal_size()
targets = [
    "# /dev/sda5: recovering journal",
    "# /dev/sda5: clean, 306882&1277952 files, 2236576/5111040 blocks",
    "S -.mount",
    "S dev-hugepages.mount",
    "S dev-mqueue.mount",
    "S sys-kernel-debug.mount",
    "S sys-kernel-tracing.mount",
    "S blk-availability.service",
    "S kmod-static-nodes.service",
    "S systemd-journald.service",
    "S systemd-remount-fs.service",
    "S lvm2-monitor.service",
    "S ufw.service",
    "S systemd-udev-trigger.service",
    "S swapfile.swap",
    "S systemd-random-seed.service",
    "S keyboard-setup.service",
    "S systemd-sysusers.service",
    "S systemd-modules-load.service",
    "S sys-fs-fuse-connection.mount",
    "S sys-kernel-config.mount",
    "S systemd-tmpfiles-setup-dev.service",
    "S systemd-journal-flush.service",
    "S systemd-sysctl.service",
    "S systemd-udevd.service",
    "S systemd-fsckd.service",
    "S boot-efi.mount",
    "S finalrd.service",
    "O Finished Set console font and keymap",
    "S console-setup.service",
    "O Finished Tell Plymouth To Write Out Runtime Data.",
    "S systemd-tmpfiles-setup.service",
    "O Finished Create Volatile Files and Directories.",
    "# Starting Network Name Resuolution...",
    "# Starting Network Time Synchronization...",
    "# Starting Update UTHP about System Boot/Shutdown...",
    "S systemd-update-utmp.service",
    "O Finished Update UTHP abvout System Boot/Shutdown.",
    "O Finished Clean up any mess left by odns-up.",
    "O Started Network Time Synchronization.",
    "O Reached target System Time Set.",
    "O Reached target System Time Synchronized.",
    "S systemd-timesyncd.service",
    "# Starting Tell Plymouth To Write Out Runtime Data...",
    "# Starting Show Plymouth Boot Screen...",
    "O Finished Tell Plymouth To Write Out Runtime Data.",
    "O Started Show Plymouth Boot Screen.",
    "O Started Network Name Resolution.",
    "O Reached target Host and Network Name Lookups.",
    "S systemd-resolved.service",
    "S apparmor.service",
    "O Finished Load AppArmor profiles.",
    "O Reached target System Initialization.",
    "O Started ACPI Events Check.",
    "O Started Daily pkgm download activities.",
    "O Started Daily pkgm upgrade and clean activities.",
    "O Started Periodic ext4 Online Metadata Check for All Filesystems.",
    "O Started Discard unused blocks once a week.",
    "O Started Refresh fwupd metadata regularly.",
    "O Daily rotation of log files.",
    "O Daily man-db regeneration.",
    "O Started Message of the Day.",
    "O Started Daily Cleanup of Temporary Directories.",
    "O Reached target Paths.",
    "O Reached target Timers.",
    "O Listening on ACPID Listen Socket.",
    "O Listening on Avahi mDNS/DNS-SD Stack Activation Socket.",
    "O Listening on CUPS Scheduler.",
    "O Listening on D-Bus System Message Bus Socket.",
    "O Listening on UUID daemon activation socket.",
    "O Reached target Sockets.",
    "O Reached target Basic System.",
    "# Starting Accounts Service...",
    "O Started ACPI event daemon.",
    "# Starting Save/Restore Sound Card State...",
    "S anacron.service",
    "F Starting Save/Restore Sound Card State.",
    "O Started Regular background program processing daemon.",
    "S cron.service",
    "O Started CUPS Scheduler.",
    "S cups.service",
    "O Started D-Bus System Message Bus.",
    "S dbus.service",
    "# Starting Network Manager...",
    "O Started Save initial kernel messages after boot.",
    "S dmesg.service",
    "# Starting Remove Stale Online ext4 Metadata Check Snapshots...",
    "# Starting Detect the available GPUS and deal with any system changes...",
    "# Starting Record successful boot for GRUB...",
    "O Started irqbalance daemon.",
    "S irqbalance.service",
    "# Starting Initialize hardware monitoring sensors...",
    "O Started inarkos-system.service.",
    "S inarkos-system.service",
    "# Starting Dispatcher daemon for systemd-networkd...",
    "# Starting Raise network interfaces...",
    "# Starting Authorization Manager...",
    "# Starting System Logging Service...",
    "# Starting Login Service...",
    "# Starting InarkOS system adjustments...",
    "# Starting Disk Manager",
    "# Starting HPA supplicant...",
    "O Finished Remove Stale Online ext4 Metadata Check Snapshots.",
    "S alsa-restore.service",
    "O Finished Save/Restore Sound Card State.",
    "O Reached target Sound Card.",
    "S lm-sensors.service",
    "O Finished Initialize hardware monitoring sensors."
    "O Finished Record successful boot for GRUB.",
    "# Starting GRUB failed boot detection...",
    "S networking.service",
    "O Finished Raise network interfaces.",
    "O Finished GRUB failed boot detection...",
    "O Started System Logging Service.",
    "S rsyslog.service",
    "O Finished Detect the available GPUs and deal with any system changes.",
    "O Started Login Service.",
    "S systemd-logind.service",
    "O Started Avahi mDNS/DNS-SD Stack.",
    "S avahi-daemon.service",
    "O Started Make remote CUPS printers available locally.",
    "S cups-browsed.service",
    "O Started WPA supplicant.",
    "S wpa_supplicant.service",
    "O Started Authorization Manager.",
    "S polkit.service",
    "# Starting Modem Manager...",
    "S inarkos-system-adjustments.service",
    "O Finished InarkOS system adjustments.",
    "O Started Network Manager.",
    "O Reached target Network.",
    "S NetworkManager.service",
    "# Starting Network Manager Wait Online...",
    "# Starting Permit User Sessions...",
    "S systemd-user-sessions.service",
    "O Finished Permit User Sessions.",
    "# Starting Hold until boot process finishes up...",
    "# Starting Hostname Service...",
    "O Starting Hostname Service.",
    "S systemd-hostnamed.service",
    "O Started Disk Manager.",
    "S udisks2.service",
    "# Starting Network Manager Script Dispatcher Service...",
    "O Started Accounts Service.",
    "S accounts-daemon.service",
    "F Started Network Manager Script Dispatcher Service.",
    "S NetworkManager-dispatcher.service",
    "O Started Modem Manager.",
    "S ModemManager.service",
    "S NetworkManager-wait-online.service",
    "S hddtemp.service",
    "S kerneloops.service",
    "S networkd-dispatcher.service",
    "O Mounting /dev/sda1",
    "F Mounting /dev/sda2",
    "F Mounting /dev/sda3",
    "O Mounting /boot",
    "O Mounting /root",
    "O Starting InarkOS...",
    "S inarkos.service",
    "O Starting InarkOS.",
]

def fancyboot():
    for target in targets:
        _ = target.split(' ')[0]
        if _ == 'O': # Ok
            print(f'[  {Fore.GREEN}' + 'OK' + f'{Fore.WHITE}  ] ' + target[2:])
        elif _ == '#': # Blank
            print(' '*9 + str(target[2:]))
        elif _ == 'F': # Fail
            print(f'[{Fore.RED}' + 'FAILED' + f'{Fore.WHITE}] ' + target[2:])
        elif _ == 'S': # Service
            print(f'{Fore.WHITE}' + target[2:])
        time.sleep(random.uniform(0.005, 0.02))
    time.sleep(1.5)
    
clear_command = 'clear'
if os.name == 'nt':  # If Machine is running on Windows, use cls
    clear_command = 'cls'

if '--noboot' not in sys.argv:

    data = open('sys_settings.cfg', 'r').readlines()
    for i in range(len(data)):
        if data[i].split('=')[0] == 'boot-type':
            if data[i].split('=')[1].replace('\n', '') == '\'phase\'':
                os.system(clear_command)

                fancyboot()
                del targets
                def cprint(r, g, b, text):
                    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))

                a = 1
                v = 0

                for i in range(255):
                    os.system(clear_command)
                    if v%255 == 0:
                        if a == 1:
                            a = 0
                        else:
                            a = 1
                    if a == 1:
                        v -= 3
                    else:
                        v += 3
                    for i in range(h//2-3):
                        print()
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██╗███╗  ██╗ █████╗ ██████╗ ██╗  ██╗       █████╗  ██████╗')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║████╗ ██║██╔══██╗██╔══██╗██║ ██╔╝      ██╔══██╗██╔════╝')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║██╔██╗██║███████║██████╔╝█████═╝ █████╗██║  ██║╚█████╗ ')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║██║╚████║██╔══██║██╔══██╗██╔═██╗ ╚════╝██║  ██║ ╚═══██╗')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║██║ ╚███║██║  ██║██║  ██║██║ ╚██╗      ╚█████╔╝██████╔╝')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚════╝ ╚═════╝ ')
            elif data[i].split('=')[1].replace('\n', '') == '\'normal\'':
                init()

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
                    win.addstr(y + yoffset - 5 - offset, x - 27, "██╗███╗  ██╗ █████╗ ██████╗ ██╗  ██╗       █████╗  ██████╗")
                    win.addstr(y + yoffset - 4 - offset, x - 27, "██║████╗ ██║██╔══██╗██╔══██╗██║ ██╔╝      ██╔══██╗██╔════╝")
                    win.addstr(y + yoffset - 3 - offset, x - 27, "██║██╔██╗██║███████║██████╔╝█████═╝ █████╗██║  ██║╚█████╗ ")
                    win.addstr(y + yoffset - 2 - offset, x - 27, "██║██║╚████║██╔══██║██╔══██╗██╔═██╗ ╚════╝██║  ██║ ╚═══██╗")
                    win.addstr(y + yoffset - 1 - offset, x - 27, "██║██║ ╚███║██║  ██║██║  ██║██║ ╚██╗      ╚█████╔╝██████╔╝")
                    win.addstr(y + yoffset - 0 - offset, x - 27, "╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚════╝ ╚═════╝ ")

                    for i in range(scl + 1):
                        win.addstr(y + 8, x - round(scl / 2) - 2, "[" + "#" * i + "-" * (scl - i) + ']')
                        win.addstr(y + 10, x - round(scl / 2) - 2 + 6, "Booting...")
                        win.refresh()
                        time.sleep(0.07)

                    time.sleep(0.6)
                    win.attroff(color_pair(1))
                    endwin()
                except Exception as e:
                    print(e)
            elif data[i].split('=')[1].replace('\n', '') == '\'D-boot\'':
                os.system(clear_command)

                fancyboot()
                del targets
                def cprint(r, g, b, text):
                    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))

                on = [1, 0, 0, 0, 0, 0]

                v = 0

                for i in range(20):
                    os.system(clear_command)
                   
                    for j in range(h//2-3):
                        print()

                    v = i%6

                    cprint(0, 0, 255 if v == 0 else 150, ' '*((w//2)-(58//2)) + '██╗███╗  ██╗ █████╗ ██████╗ ██╗  ██╗       █████╗  ██████╗')
                    cprint(0, 0, 255 if v == 1 else 150, ' '*((w//2)-(58//2)) + '██║████╗ ██║██╔══██╗██╔══██╗██║ ██╔╝      ██╔══██╗██╔════╝')
                    cprint(0, 0, 255 if v == 2 else 150, ' '*((w//2)-(58//2)) + '██║██╔██╗██║███████║██████╔╝█████═╝ █████╗██║  ██║╚█████╗ ')
                    cprint(0, 0, 255 if v == 3 else 150, ' '*((w//2)-(58//2)) + '██║██║╚████║██╔══██║██╔══██╗██╔═██╗ ╚════╝██║  ██║ ╚═══██╗')
                    cprint(0, 0, 255 if v == 4 else 150, ' '*((w//2)-(58//2)) + '██║██║ ╚███║██║  ██║██║  ██║██║ ╚██╗      ╚█████╔╝██████╔╝')
                    cprint(0, 0, 255 if v == 5 else 150, ' '*((w//2)-(58//2)) + '╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚════╝ ╚═════╝ ')
                    t.sleep(0.5)

os.system(clear_command)

if '--nologin' in sys.argv:
    os.system(f"python3 init.py --bcomp {' '.join(sys.argv[1:])}")
else:
    os.system('python3 init.py --bcomp')
