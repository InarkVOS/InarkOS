import os
import time
from os.path import exists
# sep = ''
# def split(word):
#     return list(word)
# word = "Loading DarkOS..."
# animation = split(word)
# alreadyprinted = [ ]
# for letter in animation:
#     clear()
#     print(sep.join(alreadyprinted) + letter)
#     alreadyprinted.append(letter)
#     time.sleep(0.3)
if exists('pswdir') | exists('usrdir'):
    print("Found file redirecting")
    os.system("python3 login.py")
else:
    print("Not found file redirecting")
    os.system("python3 setup.py")