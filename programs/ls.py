import os

def listdirectory(fdir):
	print(str(os.system(f"dir {fdir}"))[0])
