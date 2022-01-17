import os
import requests
def downloadrepo():
    url = "https://pastebin.com/raw/sh4BtXGB"
    filecontent = requests.get(url)
    open('repo','wb').write(filecontent.content)
def install(package_name):
    repofile = open('repo')
    readedfile = repofile.read()
    nameofpkg = readedfile.split('=', 1)[-2]
    linkofpkg = readedfile.split('=', 1)[-1]
    print(nameofpkg, linkofpkg)
    filecontent = requests.get(linkofpkg)
    open('./programs/' + nameofpkg + '.py', 'wb').write(filecontent.content)