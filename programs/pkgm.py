import os
import requests
from colorama import Fore, Back

def downloadrepo():
    url = "https://pastebin.com/raw/sh4BtXGB"
    filecontent = requests.get(url)
    open('repo', 'wb').write(filecontent.content)


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
