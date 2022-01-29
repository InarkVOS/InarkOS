import os
import requests


def downloadrepo():
    url = "https://pastebin.com/raw/sh4BtXGB"
    filecontent = requests.get(url)
    open('repo', 'wb').write(filecontent.content)


def install(package_name):
    f = open('programs/pkgnames.txt', 'r').readlines()
    for i in range(len(f)):
        if f[i].split(' ')[1] == package_name:
            name = f[i].split(': ')[0]
            f = open(
                f'pkgprograms/{name}', 'w').write(requests.get(package_name).text.strip())
        print(f[i].split(' ')[1])
