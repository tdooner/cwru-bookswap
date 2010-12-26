from eBay import Feedback
fb = Feedback()
fb.Get('tokemak')
# print fb.Xml.toprettyxml()
fb.Save('tokemak-feedback.xml')
print 'Feedback for ' + fb.UserID + ' saved.'