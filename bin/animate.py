import time
def animate(cmd):
    text = cmd.split('animate ', 1)[-1] + '\n'
    for ltr in text:
        print(ltr, end='')
        time.sleep(0.05)