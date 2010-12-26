# Validate.py
# -----------
# Blesses an eBay sandbox test account for selling
# activity. You must validate a test account before
# you can use it to perform seller activity (such as
# AddItem).
#
# Create a test user account on sandbox.ebay.com
# before using this.
#
# Usage:
#   python validate.py <userid>
#
import sys
from eBay import User
theUser = User()
theUser.ID = sys.argv[1]
theUser.Validate()
print theUser.Xml.toprettyxml()