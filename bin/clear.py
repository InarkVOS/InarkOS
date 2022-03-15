import os
def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')