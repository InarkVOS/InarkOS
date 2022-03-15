from colorama import Fore
import random
import os
x, y = os.get_terminal_size()
import time

print(Fore.GREEN, end='')

while 1:
	for j in range(os.get_terminal_size()[1]):
		print(' '.join([random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']) for i in range(os.get_terminal_size()[0]//2+1)]), end='\r')
		time.sleep(0.01)

print(Fore.WHITE, end='')