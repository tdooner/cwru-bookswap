from eBay import SellerList
theList = SellerList()
theList.Get('jmcmanus')
print theList.Xml.toprettyxml()