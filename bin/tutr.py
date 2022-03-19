import os
from colorama import Fore

def tutr_read(fname):
    data = open('docs/commands.txt', 'r').readlines()
    for i in range(len(data)):
        if data[i].split(':')[0] == fname:
            print(data[i].split(':')[1][:-1])
            break
        elif data[i].split(' ')[0] == fname:
            print(data[i].split(':')[1][:-1])
            break
