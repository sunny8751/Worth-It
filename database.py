from pymongo import MongoClient
import numpy as np
import bottlenose
from xml.etree import ElementTree as etree
import urllib

db = MongoClient('mongodb://sunny8751:gatechfinance@vandyhacksiv-shard-00-00-swivj.mongodb.net:27017,vandyhacksiv-shard-00-01-swivj.mongodb.net:27017,vandyhacksiv-shard-00-02-swivj.mongodb.net:27017/test?ssl=true&replicaSet=VandyHacksIV-shard-0&authSource=admin')['vandyhacks']

# use Bottlenose to access Amazon Product Advertising API
AWS_ACCESS_KEY_ID = 'AKIAJIOGJFBGV2UXRUAQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_ASSOCIATE_TAG = 'sunny8751-20'
amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)

def printMongoProducts():
	for product in list(db.products.find()):
		print(product)

def addMongoProduct(productName, productPrice, productUnit):
	products = db.products

	newProduct = {
		"name": productName, 
		"price": productPrice,
		"unit": productUnit
	}
	# print (products)
	id = products.insert_one(newProduct).inserted_id
	print("Added product ID:", id)

def getMongoPrice(productName):
	products = db.products.find({"name": productName})
	if products.count() == 0:
		# product not found
		return "0"
	# return product's price
	return products[0]["price"]

def getMongoUnit(productName):
	products = db.products.find({"name": productName})
	if products.count() == 0:
		# product not found
		return ""
	# return product's unit
	return products[0]["unit"]

def getMap(root):
		if len(root) == 0:
			return root
		map = {}
		for child in root:
			tag = child.tag[child.tag.index('}') + 1:]
			if tag not in map:
				#only update if it isn't in the map already
				map[tag] = getMap(child)
		return map

def getAmazonProductInfo(productName):
	response = None
	while response is None:
		try:
			response = amazon.ItemSearch(Keywords=productName, SearchIndex="All", ResponseGroup="Offers")
		except urllib.error.HTTPError:
			pass

	# print(response)
	# response = amazon.ItemLookup(ItemId="B007OZNUCE", ResponseGroup="Offers")
	# print(response)
	# for event, elem in etree.iterparse(responseXML, events=('start-ns',)):
	# 	print elem

	# root = etree.parse("other.xml").getroot()
	# print (root.tag)
	# for child in root:
	# 	print(child.tag, child.attrib)

	#parse the xml into an ElementTree
	response = etree.XML(response)
	#convert ElementTree into map
	response = getMap(response)
	price = response["Items"]["Item"]["OfferSummary"]["LowestNewPrice"]["Amount"].text

	itemId = response["Items"]["Item"]["ASIN"].text

	response = amazon.ItemLookup(ItemId=itemId)
	response = etree.XML(response)
	response = getMap(response)
	description = response["Items"]["Item"]["ItemAttributes"]["Title"].text

	return (description, price)


# main code
# print getMongoPrice("cookout")
# print getMongoUnit("cookout")
# getAmazonProductInfo("Kindle")
# print(getAmazonProductInfo("Ramen"))
print(printMongoProducts())






