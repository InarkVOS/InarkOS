import os
import requests
from colorama import Fore, Style

def remove(package_name):
    print("Not working dont even try")

def writeURL(fname, url):
    open(fname + '.py', 'w').write(requests.get(url).text)



def install(cmd):
    done = False
    for i in range(len(cmd.split(' ')[2:])):
        f = open('programs/pkgnames.txt', 'r').readlines()
        for j in range(len(f)):
            if f[j].split(' ')[0] == cmd.split(' ')[2+i]:
                writeURL('pkgprograms/' + cmd.split(' ')[2+i], f[j].split(' ')[1])
                done = True
    if done == False:
        print('Package not found.')



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
                print(f'Command not found but can be installed with: {Fore.CYAN}pkgm install {Fore.YELLOW}' + file[i].split(' ')[0] + f'{Fore.WHITE}')

def uninstall(cmd):
    for i in range(len(cmd.split(' ')[2:])):
        if cmd.split(' ')[2+i]+'.py' in os.listdir('pkgprograms'):
            os.system('del pkgprograms\\' + cmd.split(' ')[2+i] + '.py')
        else:
            f = open('programs/pkgnames.txt', 'r').readlines()
            for j in range(len(f)):
                if cmd.split(' ')[2+i] == f[j].split(' ')[0]:
                    print('Package ' + cmd.split(' ')[2+i] + f' not found but can be installed with {Fore.CYAN}pkgm install {Fore.YELLOW}' + cmd.split(' ')[2+i] + f'{Fore.WHITE}')
                    break
                else:
                    print('Package not found.')
                    break
