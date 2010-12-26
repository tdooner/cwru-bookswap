'''
DEPENDENCIES:
	libxml2dom (http://www.boddie.org.uk/python/libxml2dom.html)


'''


import urllib, re
import libxml2dom
import sys, time

NUMBER_VENUES = 2 # Number of sites to show from BookScouter for an item.

letterstosearch = ['+']
bookids = []
ISBNcache = {} # Stores the lookups - {"isbn" => [["price_1", "name_1"], ["price_2", "name_2"]], "isbn2" => ...}

def getOffers(isbn):
	if isbn in ISBNcache:
		return ISBNcache[isbn]
	g = urllib.urlopen("http://m.bookscouter.com/prices.php?isbn="+isbn)
	html = libxml2dom.parseString(g.read(), html=1)
	venues = []
	tablecells = html.getElementsByTagName("td")
	for n in xrange(0,min(len(tablecells),NUMBER_VENUES*2),2):
		name = tablecells[n].textContent.replace(" ","_")
		price  = tablecells[n+1].xpath(".//a")[0].textContent
		venues.append([price, name])
	ISBNcache[isbn] = venues
	time.sleep(0.5) # Be nice to bookscouter
	return ISBNcache[isbn]

print("Pulling Bookswap Database")
for c in letterstosearch:
	f = urllib.urlopen("http://bookswap.case.edu/search.php?title="+c+"&sort=price&order=desc")
	bookids = re.findall('(?<=bookdata\.php\?bookid=)([0-9]*)', f.read())
	f.close()

print("Found " + str(len(bookids)) + " results. Pulling data...")

for i in bookids:
	f = urllib.urlopen("http://bookswap.case.edu/bookdata.php?bookid="+i)
	html = f.read()
	price = re.search("(?<=Price:</font> \$)([0-9\.]*)", html).group(0)
	isbn = re.search("(?<=ISBN-10:</font> )[0-9X]{10}", html)
	if isbn:
		isbn = isbn.group(0)
	else:
		sys.stderr.write("Error: No ISBN Found for " + i)
		continue
	print(isbn + " " + price), # This comma trick is the stupidest thing ever.
	values = getOffers(isbn)
	for n in values:
		print(n[0] + " " + n[1]),
	print("")
