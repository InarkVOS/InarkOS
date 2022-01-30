from programs import *
from programs import __all__
from programs import pkgm
from programs import tutr
from programs import execute
from programs import animate
from programs import clear
from programs import version
from programs import echo
from programs import programmanager
from programs import ls
from colorama import Fore, Back
import os


def check(cmd):
    if cmd.lower().startswith("dir") or cmd.lower().startswith("ls"):
        ls.listdirectory(cmd[3:])
    elif cmd.lower().startswith("./"):
        programmanager.run(cmd[2:])
    elif cmd.lower().startswith("echo "):
        echo.echo(cmd)
    elif cmd.lower().startswith("help"):
        help.help()
    elif cmd.lower().startswith("version"):
        version.version()
    elif cmd.lower().startswith("clear") or cmd.lower().startswith("cls"):
        clear.clearConsole()
    elif cmd.lower().startswith("animate "):
        animate.animate(cmd)
    elif cmd.lower().startswith("exit"):
        exit.rl()
    elif cmd.lower().startswith("pkgm downloadrepo"):
        pkgm.downloadrepo()
    elif cmd.lower().startswith("pkgm install "):
        pkgm.install(cmd.split(" ")[2])
    elif cmd.lower().startswith("tutr "):
        tutr.tutr(cmd)
    elif cmd.lower().startswith("exec "):
        execute.exec(cmd)
    elif cmd.lower().startswith("pkgm uninstall "):
        print(os.listdir())
        if cmd.split(' ')[2].replace('\n', '') in os.listdir('pkgprograms'):
            print(f"Uninstalling package" + cmd.split(" ")[2] + "...")
            os.system("del pkgprograms\\" + cmd.split(" ")[2] + ".py")
        else:
            print("package " + cmd.split(' ')[2] + f" is not installed but can be installed with {Fore.CYAN}pkgm install {Fore.YELLOW}" + cmd.split(' ')[2] + f"{Fore.WHITE}")
    elif cmd.lower().startswith("pkgm list"):
        file = open("programs/pkgnames.txt", "r").readlines()
        for i in range(len(file)):
            installed = "Not Installed"
            if file[i].replace("\n", "").split(" ")[2]+".py" in os.listdir("pkgprograms"):
                installed = f"{Fore.GREEN}Installed{Fore.WHITE}"
            else:
                installed = f"{Fore.RED}Not Installed{Fore.WHITE}"
            print(f"{Fore.GREEN}Command {i+1}. {Fore.YELLOW}" + file[i].replace("\n", "").split(" ")[2] + f"{Fore.WHITE} (" + installed + ")")
    elif cmd.lower().startswith("pkgm run"):
        if cmd.split(" ")[2]+".py" in os.listdir("pkgprograms"):
            os.system("python pkgprograms/" + cmd.split(" ")[2] + ".py")
        else:
            file = open("programs/pkgnames.txt", "r").readlines()
            for i in range(len(file)):
                if file[i].replace("\n", "").split(" ")[2] == cmd.split(" ")[2]:
                    print(f"Command not found but can be installed with: {Fore.CYAN}pkgm install {Fore.YELLOW}" + file[i].split(" ")[0] + f"{Fore.WHITE}")
    else:
        print("Command not found run help for list of commands")
