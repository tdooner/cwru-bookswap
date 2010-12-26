from eBay import Categories
cats = Categories()
cats.Get()
cats.Save('categories.xml')
cats.Dispose()
