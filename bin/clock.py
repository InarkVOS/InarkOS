from datetime import datetime
import os

numbers = [
'''████████  ████  ████  ████████''', # 0
'''    ██    ██    ██    ██    ██''', # 1
'''██████    ██████████    ██████''', # 2
'''██████    ████████    ████████''', # 3
'''██  ████  ████████    ██    ██''', # 4
'''████████    ██████    ████████''', # 5
'''████████    ████████  ████████''', # 6
'''██████    ██    ██    ██    ██''', # 7
'''████████  ██████████  ████████''', # 8
'''████████  ████████    ████████''', # 9
'''        ██          ██        ''', # :
]

currt = datetime.now()

def displayNumbers(number):
    customs = [[':', '10']]
    for y in range(5):
        for i in range(len(number)):
            idx = i
            for n in range(len(customs)):
                if customs[n][0] == number[i]:
                    idx = customs[n][1]
            for x in range(6):
                if type(idx) == int:
                    print(numbers[int(number[idx])][(y*6)+x], end='')
                else:
                    print(numbers[int(customs[0][1])][(y*6)+x], end='')
                if x == 5:
                    print('  ', end='')
        print()
    print('\n(WIP)')

def a(k, h, o):return h*(o-len(k))+k

prevtime = str(a(str(currt.second), '0', 2))
currtime = str(a(str(currt.second), '0', 2))

while 1:
    currt = datetime.now()
    if prevtime != currtime:
        os.system('cls')
        hrs  = str(a(str(currt.hour), '0', 2))
        mins = str(a(str(currt.minute), '0', 2))
        secs = str(a(str(currt.second), '0', 2))
        displayNumbers(f'{hrs}:{mins}:{secs}')
        prevtime = currtime
    currtime = str(a(str(currt.second), '0', 2))