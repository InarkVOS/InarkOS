import os

def listdirectory(fdir):
	print(str(os.system(f"ls {fdir}"))[0])
listdirectory("~/Desktop")