from analyse import *
import pandas as pd
def pretty_print(dictionaries): #pretty-printing
	"""
	:param dictionaries - dictionaries with results
	:type dictionaries - list of dict
	"""
	print('RESULTS'.center(70,' '))
	print(''.center(120,'_'))
	print('filename'.center(20,' ')+'|'+
		'vector size,bytes'.center(18,' ')+'|'+
		'Sample mean'.center(15,' ')+'|'+
		'Sample variance'.center(20,' ')+'|'+
		'chi_exp'.center(15,' ')+'|'+
		'chi_theor, a=0.95'.center(20,' ')+'|'+
		'Hypothesis assumed?'.center(20,' ')+'|')
	for d in dictionaries:
		print(d['filename'].center(20)+'|'+
			d['size'].center(18)+'|'+
			d['mean'].center(15)+'|'+
			d['var'].center(20)+'|'+
			d['exp'].center(15)+'|'+
			d['theor95'].center(20)+'|'+
			(d['assumed']).center(20)+'|')
	print(''.center(120,'_'))
dicts=[]
for i in range(1,11):
	formatter1='./jpgs/{}.jpg'
	formatter2='./cfb/{}.jpg.enc'
	formatter3='./zips/{}.zip'
	filename1=formatter1.format(str(i))
	filename2=formatter2.format(str(i))
	filename3=formatter3.format(str(i))
	for j in range(1,4):
		dicts.append(do_stuff(filename1,j))
		dicts.append(do_stuff(filename2,j))
		dicts.append(do_stuff(filename3,j))
pretty_print(dicts)
