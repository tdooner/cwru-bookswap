from eBay import User
theUser = User()
theUser.ID = "jmcmanus"
theUser.Get()
print theUser.Feedback
theUser.Dispose()