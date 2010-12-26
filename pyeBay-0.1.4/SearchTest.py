from eBay import Search
theSearch = Search()
theSearch.Get('shoes')
print theSearch.Xml.toprettyxml()