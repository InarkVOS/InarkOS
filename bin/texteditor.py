import npyscreen
import os
import sys
w, h = os.get_terminal_size()
try:
	usr  = sys.argv[sys.argv.index('--user')+1]
	try:
		file = sys.argv[sys.argv.index('--file')+1]
	except:
		file = ''

	class TextEditor(npyscreen.NPSApp):
		def __init__(self, usr):
			self.usr = usr
		def main(self):
			F		= npyscreen.Form(name = "InarkOS Text Editor",)
			maintext = F.add(npyscreen.MultiLineEdit, value = '', max_height=h-7, rely=1)
			try:
				maintext.value = open(f'MainDrive/{file}', 'r').read()
			except:
				pass
			try:
				maintext.value = open(f'{file}', 'r').read()
			except:
				pass
			fname	= F.add(npyscreen.TitleText, name = "Filename:", rely=h-3)
			fname.value = file
			a		= 0
			F.edit()
			if fname.value.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('"', '').replace('>', '').replace('<', '').replace('|', '') != '':
				try:
					open(f'{fname.value}', 'w').write(maintext.value)
				except:
					os.system(f'echo. > {fname.value}')
					open(f'{fname.value}', 'w').write(maintext.value)

	if '--run' in sys.argv:
		try:
			App = TextEditor(usr)
			App.run()
			App = ''
		except AttributeError:
			print('There is a bug that you can only run the text editor once i dont know how to fix it. :P')
except:
	pass
