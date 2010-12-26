from eBay import FinanceOffers
theOffers = FinanceOffers()
theOffers.Get()
print theOffers.Xml.toprettyxml()
# print theOffers.Offers['6060842']
theOffers.Save('offers.xml')