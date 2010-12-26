from eBay import Item
theItem = Item()
theItem.Session.Initialize()
theItem.Add()
print "Added as ID # " + theItem.ID
print "View online at:"
print theItem.URL