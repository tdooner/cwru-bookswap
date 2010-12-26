'''
DEPENDENCIES:
	libxml2dom (http://www.boddie.org.uk/python/libxml2dom.html)


'''


import urllib, re
import libxml2dom

NUMBER_VENUES = 2 # Number of sites to show from BookScouter for an item.

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
	g = urllib.urlopen("http://m.bookscouter.com/prices.php?isbn="+isbn)
	html = libxml2dom.parseString(g.read(), html=1)
	venues = {}
	tablecells = html.getElementsByTagName("td")
	for n in xrange(0,NUMBER_VENUES*2,2):
		name = tablecells[n].textContent
		price  = tablecells[n+1].xpath(".//a")[0].textContent
		print("   " + name + " offers " + str(price))
