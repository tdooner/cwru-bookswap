import urllib, re

classes = ['EECS233']#,'EECS245','EECS281','EECS290','EECS301','EECS302','EECS304','EECS305','EECS309','EECS313','EECS314','EECS315','ENGR131','ENGR145','ENGR200','ENGR210','ENGR216','ENGR225','PHYS121','PHYS122','CHEM111','MATH121','MATH122','ECIV160']

for c in classes:
	f = urllib.urlopen("http://bookswap.case.edu/search.php?class="+c)
	books = re.findall('(?<=bookdata\.php\?bookid=)([0-9]*)', f.read())
	print(books)
	f.close()
