import os

def custom_listdir(fdir):
	folders = ['pswdir', 'usrdir']
	try:
		ls = os.listdir(fdir)
	except:
		return 'Folder does not exist.'
	for i in range(len(folders)):
		try:
			ls.remove(folders[i])
			for j in range(len(ls)):
				if ls[j][0] == '.':
					ls.remove(ls[j])
		except:
			pass
	if ls == []:
		return 'Folder is empty.'
	for i in range(len(ls)):
		if os.path.isdir(fdir + '/' + ls[i]):
			ls[i] = 'FOLDER: ' + ls[i]
		if os.path.isfile(fdir + '/' + ls[i]):
			ls[i] = 'FILE:   ' + ls[i]
	return ls

def listdirectory(fdir, usr):
	if usr == 'NOUSR':
		print('Please login to a user account.')
	else:
		if fdir == '':
			files = custom_listdir(f'MainDrive/Users/{usr}')
			if files == 'Folder is empty.':
				print(files)
			elif files == 'Folder does not exist.':
				print(files)
			else:
				print('\n'.join(custom_listdir(f'MainDrive/Users/{usr}')))
		else:
			files = custom_listdir(f'MainDrive/Users/{usr}/{fdir}')
			if files == 'Folder is empty.':
				print(files)
			elif files == 'Folder does not exist.':
				print('Folder does not exist.')
			else:
				print('\n'.join(files))
