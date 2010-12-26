import urllib, re

letterstosearch = ['+']
bookids = ['18405','12710'] # Eventually this will be an empty array

print("Pulling Bookswap Database")
'''
Commenting out for now because I want to minimize the pain on their server

for c in letterstosearch:
	f = urllib.urlopen("http://bookswap.case.edu/search.php?title="+c+"&sort=price&order=desc")
	bookids = re.findall('(?<=bookdata\.php\?bookid=)([0-9]*)', f.read())
	f.close()
'''

print("Found " + str(len(bookids)) + " results. Pulling data...")

for i in bookids:
	f = urllib.urlopen("http://bookswap.case.edu/bookdata.php?bookid="+i)
	html = f.read()
	price = re.search("(?<=Price:</font> \$)([0-9\.]*)", html).group(0)
	isbn = re.search("(?<=ISBN-10:</font> )[0-9]{10}", html).group(0)
	print("Found ISBN " + isbn + " at price " + price)
