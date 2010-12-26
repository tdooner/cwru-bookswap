pyeBay
Python Module for eBay
Version 0.1.4
18. November 2004
http://developer.ebay.com
developer-relations@ebay.com
============================

About this Module
-----------------
pyeBay is a Python module for eBay. It wraps eBay's XML-over-HTTPS API, making it simple to incorporate the eBay marketplace into your Python application.

This release currently encapsulates the following eBay functionality:

 - GeteBayOfficialTime
 - GetSearchResults
 - GetUser
 - GetCategories
 - AddItem
 - GetSellerList (new in this release)
 - GetFinanceOffers (new in this release)
 - ValidateTestUserRegistration (new in this release)
 - REST Token retrieval (similar to the token tool at http://developer.ebay.com/tokentool/ with the benefit of not invalidating existing tokens when you create a REST token; see GetRestToken.py for the code)

See the enclosed demo scripts (GetTimeTest.py, SearchTest.py, etc.) for an example of how to use this module.


Licensing
---------
This module is licensed under the MIT license, a BSD-style open source license. See the enclosed file LICENSE.TXT for details.


Using pyeBay
------------
This module uses the eBay API. To use the eBay API, you must first sign up for the eBay Developers Program. (It's free.) Do so here:

  http://developer.ebay.com/join/

After you've signed up, you'll receive a set of developer keys. You'll need to copy your developer keys into the appropriate locations in the eBay.ini file that accompanies this distribution. Then you'll need to create a test account on sandbox.ebay.com. Then, you must generate a single-use authentication token from the tool located here:

  http://developer.ebay.com/tokentool/

This module wraps eBay's API, which uses XML over HTTPS POST. See complete information about developing eBay applications using eBay's XML API here:

  http://developer.ebay.com/xml/
  
To test seller functionality (such as AddItem) in the sandbox, you must bless the sandbox user account with a call to the ValidateTestUserRegistration API. You must do this once (and only once) per sandbox account. The script Validate.py performs this step for you; see the comments in that script for details.

 
Contributing
------------
There are approximately seventy eBay API calls in total. We'd like to see Python class wrappers for all of them. The calls on the to-do list are listed in the comment block at the top of eBay.py; the complete list of all available API calls is here:

  http://developer.ebay.com/DevZone/docs/API_Doc/index.asp

If there's an API call you need for which there isn't a wrapper, feel free to create it and send it to us. We'll include it in a future release.

At some point, some sort of Tkinter or wxPython UI would probably be interesting as well, but for now we'll get the class wrappers out of the way and make the pretty stuff happen later.

Questions, comments, patches, etc., may be sent to the eBay evangelism team at developer-relations@ebay.com.