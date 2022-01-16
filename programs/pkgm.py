import os
import requests
def downloadrepo():
    url = "https://pastebin.com/raw/sh4BtXGB"
    filecontent = requests.get(url)
    open('repo','wb').write(filecontent.content)
def install_package(package_name):
    repofile = open('repo')
