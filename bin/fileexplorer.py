import os
if os.name == 'nt':
	from msvcrt import *
else:
	from curtsies import Input
	def getch():
		with Input(keynames='curses') as input_generator:
			for e in input_generator:
				if e == '\n':
					return 'ENTER'
				else:
					return e.replace('KEY_', '')
import sys
w, h = os.get_terminal_size()
selidx = 0
done = 0
paths = ['MainDrive']
customs = ['>back<', '>quit<', '>delete<', '>rename<', '>make file<', '>make folder<']
selected = []

def update(path):
	files = os.listdir(path)
	os.system('cls')
	if len(paths) != 1:
		files.append('>back<')
	files.append('>quit<')
	files.append('>make file<')
	files.append('>make folder<')
	if len(selected) != 0:
		files.append('>delete<')
	if len(selected) == 1:
		files.append('>rename<')
	for i in range(len(files)):
		if i == selidx:
			print('* ', end='')
		elif files[i] in selected:
			print('# ', end='')
		else:
			print('  ', end='')
		print(files[i])
	return len(files), files

if '--run' in sys.argv:
	try:
		usr = sys.argv[sys.argv.index('--user')+1]
		path = 'MainDrive/'
		if os.name == 'nt':
			while not done:
				length, items = update(paths[-1])
				key = ord(getch())
				if key == 224:
					keyc = ord(getch())
					if keyc == 80:
						if selidx != length-1:
							selidx += 1
					if keyc == 72:
						if selidx != 0:
							selidx -= 1
				if key == 13 and items[selidx] == '>quit<':
					os.system('cls')
					done = 1
				if key == 32 and items[selidx] not in customs:
					if items[selidx] in selected:selected.remove(items[selidx])
					else:selected.append(items[selidx])
				elif key == 13:
					if items[selidx] not in customs and os.path.isdir(paths[-1] + '/' + items[selidx]):
						paths.append(paths[-1] + '/' + items[selidx])
						selidx = 0
					if items[selidx] == '>back<':
						del paths[-1]
						selidx = 0
					if items[selidx] not in customs and os.path.isfile(paths[-1] + '/' + items[selidx]):
						os.system(f'python3 bin/texteditor.py --run --user {usr} --file ' + paths[-1] + '/' + items[selidx])
					if items[selidx] == '>delete<':
						for i in range(len(items)):
							if items[i] in selected:
								idx = selected.index(items[i])
								if os.name == 'nt':
									thing = paths[-1].replace('/', '\\')
									if os.path.isdir(f'{thing}\\{selected[idx]}'):
										os.system(f'rmdir {thing}\\{selected[idx]}')
									else:
										os.system(f'del /f {thing}\\{selected[idx]}')
								selected.remove(items[i])
						selidx = 0
					if len(selected) == 1 and '>rename<' in items and items[selidx] == '>rename<':
						newname = input(f'Enter the new file name for {selected[0]}: ')
						thing = os.getcwd().replace('\\', '/')
						thinga = paths[-1].replace('\\', '/')
						os.chdir(paths[-1])
						os.system(f'rename {selected[0]} {newname}')
						for i in range(len(paths[-1].split('/'))):
							os.chdir('..')
						selected.remove(selected[0])
						selidx = 0
					if items[selidx] == '>make file<':
						os.chdir(paths[-1])
						fname = input('Enter the file name: ')
						open(fname, 'w').write('')
						for i in range(len(paths[-1].split('/'))):
							os.chdir('..')
					if items[selidx] == '>make folder<':
						os.chdir(paths[-1])
						fname = input('Enter the folder name: ')
						os.mkdir(fname)
						for i in range(len(paths[-1].split('/'))):
							os.chdir('..')
		else:
			while not done:
				length, items = update(paths[-1])
				key = getch()
				if key == 'DOWN':
					if selidx != length-1:
						selidx += 1
				if key == 'UP':
					if selidx != 0:
						selidx -= 1
				if key == 'ENTER':
					if items[selidx] == '>quit<':
						os.system('clear')
						done = 1
					if items[selidx] != '>back<' and os.path.isdir(paths[-1] + '/' + items[selidx]):
						paths.append(paths[-1] + '/' + items[selidx])
						selidx = 0
					if items[selidx] == '>back<':
						del paths[-1]
						selidx = 0
					if items[selidx] != '>back<' and os.path.isfile(paths[-1] + '/' + items[selidx]):
						os.system(f'python3 bin/texteditor.py --run --user {usr} --file ' + paths[-1] + '/' + items[selidx])
	except:
		pass