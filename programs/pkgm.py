import os
import requests


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
