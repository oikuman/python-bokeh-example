import re
import requests
import json
import pprint as pp

def search_birth(url):
	res = requests.get(url)
	j = res.text
	#{{Birth date|df=yes|1879|02|23}}

	p = re.compile(r'Birth date(.*)')
	m = re.search(p, j)
	if not m==None:
		s = m.group()

		p1 = re.compile(r'\d\d\d\d\|\d\d\|\d\d')
		m1 = re.search(p1, s)
		if not m1==None:
			s1 = m1.group()
			birth_list = s1.split('|')
			return birth_list
	
from birth_api_data import birth_data	

name_birth = dict()
name_month = dict()

for name in birth_data:
	url = birth_data[name]
	date = search_birth(url)
	if not date==None:
		year = int(date[0])
		month = int(date[1])
		day = int(date[2])
		print('{} {} {}'.format(year, month, day))
		name_birth[name] = str(year) + '-' + str(month) + '-' + str(day)
		name_month[name] = month

#save to file1
file = open('name_birth_data.py', 'w')
file.write('name_birth_data = ')
pp.pprint(name_birth, file)
file.close()

#save to file2
file = open('name_month_data.py', 'w')
file.write('name_month_data = ')
pp.pprint(name_month, file)
file.close()

		
