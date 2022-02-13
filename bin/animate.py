#import modules
import os
import time

def animate(cmd):
    argonly = cmd.split('animate ', 1)[-1]
    # set variables & functions
    sep = '' # Separator
    # Split the word into a list
    def split(word):
        return list(argonly)
    animation = split(argonly)
    alreadyprinted = [ ]
    # Clear console after each letter
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
    # Every item of list
    for letter in animation:
        clearConsole()
        print(sep.join(alreadyprinted) + letter)
        alreadyprinted.append(letter)
        time.sleep(0.3)