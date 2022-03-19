import os
import requests
from rich import print as rprint
import numpy as np
from tqdm.auto import tqdm

def writeURL(fname, url):

    chunk_size = 1024

    r = requests.get(url, stream=True)

    total_size = int(r.headers.get('content-length', 0))

    with open(fname, 'wb') as f:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size/chunk_size, unit='KB'):
            f.write(data)

    print('Download Complete')



def install(cmd):
    done = False
    for i in range(len(cmd.split(' ')[2:])):
        f = open('bin/pkgnames.txt', 'r').readlines()
        for j in range(len(f)):
            if f[j].split(' ')[0] == cmd.split(' ')[2+i]:
                writeURL('ubin/' + cmd.split(' ')[2+i] + '.py', f[j].split(' ')[1])
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
        rprint(f"[green]Command {i+1}. [/green]" + file[i].replace("\n", "").split(" ")[2] + f" (" + installed + ")")

def run(cmd):
    if cmd[0:2] == './':
        found = False
        cmd = cmd[2:]
        if cmd+'.py' in os.listdir('ubin'):
            os.system("python3 ubin/" + cmd + '.py')
        else:
            file = open('bin/pkgnames.txt', 'r').readlines()
            for i in range(len(file)):
                if file[i].replace('\n', '').split(' ')[2] == cmd:
                    found = True
                    rprint(f'Package not found but can be installed with: [cyan]pkgm install[/cyan][yellow] ' + file[i].split(' ')[0] + f'[/yellow]')
            if found == False:
                print('Package not found.')

def uninstall(cmd):
    for i in range(len(cmd.split(' ')[2:])):
        if cmd.split(' ')[2+i]+'.py' in os.listdir('ubin'):
            os.remove('ubin/' + cmd.split(' ')[2+i] + '.py')
        else:
            f = open('bin/pkgnames.txt', 'r').readlines()
            for j in range(len(f)):
                if cmd.split(' ')[2+i] == f[j].split(' ')[0]:
                    rprint('Package ' + cmd.split(' ')[2+i] + f' not found but can be installed with [cyan]pkgm install [/cyan][yellow]' + cmd.split(' ')[2+i] + f'[/yellow]')
                    break
                else:
                    print('Package not found.')
                    break

def add_package(url, pname):
    try:
        res = requests.get(url, stream=True)
        print('NOTE: To add the package to the OS contact the OWNER/DEVS')
        data = open('pkgnames.txt', 'r').readlines()
        data.append('\n' + pname + ' ' + url + ' ' + pname)
        data = ''.join(data)
        open('pkgnames.txt', 'w').write(data)
        print('Added!')
    except requests.exceptions.MissingSchema:
        print('Invalid URL')
