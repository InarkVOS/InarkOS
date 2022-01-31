import os
import requests
from colorama import Fore, Style

def remove(package_name):
    print("Not working dont even try")
def install(package_name):
    try:
        print("Downloading...")
        f = open('programs/pkgnames.txt', 'r').readlines()
        for i in range(len(f)):
            f[i] = f[i].replace('\n', '')
            thing = f[i].split(' ')[0]
            if package_name == thing:
                name = f[i].split(' ')[2]
                txt = requests.get(f[i].split(' ')[1])
                f = open('pkgprograms/' + name + '.py', 'w').write(txt.text.strip())
    except:
        pass
def list():
    file = open("programs/pkgnames.txt", "r").readlines()
    for i in range(len(file)):
        installed = "Not Installed"
        if file[i].replace("\n", "").split(" ")[2]+".py" in os.listdir("pkgprograms"):
            installed = f"{Fore.GREEN}Installed{Fore.WHITE}"
        else:
            installed = f"{Fore.RED}Not Installed{Fore.WHITE}"
        print(f"{Fore.GREEN}Command {i+1}. {Fore.YELLOW}" + file[i].replace("\n", "").split(" ")[2] + f"{Fore.WHITE} (" + installed + ")")
def run(cmd):
    if cmd.split(' ')[2]+'.py' in os.listdir('pkgprograms'):
        os.system("python pkgprograms/" + cmd.split(' ')[2] + '.py')
    else:
        file = open('programs/pkgnames.txt', 'r').readlines()
        for i in range(len(file)):
            if file[i].replace('\n', '').split(' ')[2] == cmd.split(' ')[2]:
                print('Command not found but can be installed with: pkgm install ' + file[i].split(' ')[0])