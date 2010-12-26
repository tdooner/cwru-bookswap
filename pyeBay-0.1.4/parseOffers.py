from xml.dom.minidom import parse, parseString
xd = parse('offers.xml')
# print xd.toprettyxml()

offers = xd.getElementsByTagName('FinanceOffer')

for e in offers:
    print "Seller terms:"
    print str(e.getElementsByTagName('SellerTerms')[0].childNodes[1].nodeValue)
    print "Buyer terms:"
    print str(e.getElementsByTagName('BuyerTerms')[0].childNodes[1].nodeValue)
    print "-------------------------------------"