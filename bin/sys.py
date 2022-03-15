from pathlib import Path

class DisplayablePath (object ):
	display_filename_prefix_middle ='├──'
	f ='└──'
	b ='	'
	display_p_prefix_last ='│   '
	def __init__ (O0OO0O0000000000O ,OO0OOOO000O0O00OO ,OO0000000OO0O0O0O ,O0OO00O0O00OO0O0O ):
		O0OO0O0000000000O .l =Path (str (OO0OOOO000O0O00OO ))
		O0OO0O0000000000O .p =OO0000000OO0O0O0O 
		O0OO0O0000000000O .y =O0OO00O0O00OO0O0O 
		if O0OO0O0000000000O .p :O0OO0O0000000000O .o =O0OO0O0000000000O .p .o +1 
		else :O0OO0O0000000000O .o =0 
	@property 
	def displayname (OOO0O00OO0O0OOO00 ):
		if OOO0O00OO0O0OOO00 .l .is_dir ():return OOO0O00OO0O0OOO00 .l .name +'/'
		return OOO0O00OO0O0OOO00 .l .name 
	@classmethod 
	def make_tree (OOOOO0OOOO0OO0000 ,O000O000O00O00O0O ,p =None ,y =False ,u =None ):
		O000O000O00O00O0O =Path (str (O000O000O00O00O0O ))
		u =u or OOOOO0OOOO0OO0000 .r 
		OOO0OO00OOO0OOOOO =OOOOO0OOOO0OO0000 (O000O000O00O00O0O ,p ,y )
		yield OOO0OO00OOO0OOOOO 
		OOO0OOOOO0O0O0OOO =sorted (list (OOOO00000OO000O0O for OOOO00000OO000O0O in O000O000O00O00O0O .iterdir ()if u (OOOO00000OO000O0O )),key =lambda OOOOOO00O0O0O00O0 :str (OOOOOO00O0O0O00O0 ).lower ())
		O00O000OO000O0O0O =1 
		for OO00O00O0OOOOO00O in OOO0OOOOO0O0O0OOO :
			y =O00O000OO000O0O0O ==len (OOO0OOOOO0O0O0OOO )
			if OO00O00O0OOOOO00O .is_dir ():yield from OOOOO0OOOO0OO0000 .make_tree (OO00O00O0OOOOO00O ,p =OOO0OO00OOO0OOOOO ,y =y ,u =u )
			else :yield OOOOO0OOOO0OO0000 (OO00O00O0OOOOO00O ,OOO0OO00OOO0OOOOO ,y )
			O00O000OO000O0O0O +=1 
	@classmethod 
	def r (OOO0OO0O00O00OOO0 ,O0OOOO000OOOOO00O ):return True 
	@property 
	def displayname (OO0OO0O0O0000O00O ):
		if OO0OO0O0O0000O00O .l .is_dir ():return OO0OO0O0O0000O00O .l .name +'/'
		return OO0OO0O0O0000O00O .l .name 
	def displayable (O000OOOO00OO0O000 ):
		if O000OOOO00OO0O000 .p is None :return O000OOOO00OO0O000 .displayname 
		_O0O00OO0OO00000OO =(O000OOOO00OO0O000 .f if O000OOOO00OO0O000 .y else O000OOOO00OO0O000 .display_filename_prefix_middle )
		O0O00000OO0OOO0O0 =['{!s} {!s}'.format (_O0O00OO0OO00000OO ,O000OOOO00OO0O000 .displayname .replace ('/',''))]
		O00O0OOO0O00OO0OO =O000OOOO00OO0O000 .p 
		while O00O0OOO0O00OO0OO and O00O0OOO0O00OO0OO .p is not None :
			O0O00000OO0OOO0O0 .append (O000OOOO00OO0O000 .b if O00O0OOO0O00OO0OO .y else O000OOOO00OO0O000 .display_p_prefix_last )
			O00O0OOO0O00OO0OO =O00O0OOO0O00OO0OO .p 
		return ''.join (reversed (O0O00000OO0OOO0O0 ))

def tree(dir, usr):
	if usr != 'NOUSR':
		ls = DisplayablePath.make_tree(Path(f'../MainDrive/Users/survi/{dir}'.replace('\\\\', '').replace('..', '.')))
		for l in ls:
			print(l.displayable())