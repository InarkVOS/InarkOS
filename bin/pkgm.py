import os
import requests
from rich import print
def writeURL(fname, url):
    open(fname + '.py', 'w').write(requests.get(url).text)



def install(cmd):
    done = False
    for i in range(len(cmd.split(' ')[2:])):
        f = open('bin/pkgnames.txt', 'r').readlines()
        for j in range(len(f)):
            if f[j].split(' ')[0] == cmd.split(' ')[2+i]:
                writeURL('ubin/' + cmd.split(' ')[2+i], f[j].split(' ')[1])
                done = True
    if done == False:
        print('Package not found.')



def list():
    file = open("bin/pkgnames.txt", "r").readlines()
    for i in range(len(file)):
        installed = "Not Installed"
        if file[i].replace("\n", "").split(" ")[2]+".py" in os.listdir("ubin"):
            installed = f"[green]Installed[/green]"
        else:
            installed = f"[red]Not Installed[/red]"
        print(f"[green]Command {i+1}. [/green]" + file[i].replace("\n", "").split(" ")[2] + f" (" + installed + ")")
def run(cmd):
    if cmd[0] == '.':
        cmd = cmd[2:]
        if cmd+'.py' in os.listdir('ubin'):
            os.system("python ubin/" + cmd + '.py')
        else:
            file = open('bin/pkgnames.txt', 'r').readlines()
            for i in range(len(file)):
                if file[i].replace('\n', '').split(' ')[2] == cmd:
                    print(f'Command not found but can be installed with: [cyan]pkgm install[/cyan][yellow]' + file[i].split(' ')[0] + f'[/yellow]')
    else:
        if cmd.split(' ')[2]+'.py' in os.listdir('ubin'):
            os.system("python ubin/" + cmd.split(' ')[2] + '.py')
        else:
            file = open('bin/pkgnames.txt', 'r').readlines()
            for i in range(len(file)):
                if file[i].replace('\n', '').split(' ')[2] == cmd.split(' ')[2]:
                    print(f'Command not found but can be installed with: [cyan]pkgm install [/cyan][yellow]' + file[i].split(' ')[0] + f'[/yellow]')

def uninstall(cmd):
    for i in range(len(cmd.split(' ')[2:])):
        if cmd.split(' ')[2+i]+'.py' in os.listdir('ubin'):
            os.remove('ubin/' + cmd.split(' ')[2+i] + '.py')
        else:
            f = open('bin/pkgnames.txt', 'r').readlines()
            for j in range(len(f)):
                if cmd.split(' ')[2+i] == f[j].split(' ')[0]:
                    print('Package ' + cmd.split(' ')[2+i] + f' not found but can be installed with [cyan]pkgm install [/cyan][yellow]' + cmd.split(' ')[2+i] + f'[/yellow]')
                    break
                else:
                    print('Package not found.')
                    break
