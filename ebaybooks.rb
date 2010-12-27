require 'rubygems'
require 'ebay'
require './config.rb'


# Create the eBay client
ebay = Ebay::Api.new
#
# # Get the official eBay time
# response = ebay.get_ebay_official_time
#
# # Display the time to the user
# puts response.timestamp
response = ebay.get_item(:item_id => ARGV.first, :detail_level => "ItemReturnAttributes")
attribute_set = response.item.attribute_sets[0]
if attribute_set.attribute_set_id != 1392
	puts "Not a book!"
end
attributes = attribute_set.attributes

attributes.each do |j|
	if j.attribute_id == 63739:
		puts "ISBN-13: " + j.values[0].value_literal
	end
	if j.attribute_id == 25001:
		puts "ISBN-10: " + j.values[0].value_literal
	end
end
