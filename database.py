from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import bottlenose
from xml.etree import ElementTree as etree
from StringIO import StringIO

def getMongoProducts():
	db = MongoClient('mongodb://sunny8751:gatechfinance@vandyhacksiv-shard-00-00-swivj.mongodb.net:27017,vandyhacksiv-shard-00-01-swivj.mongodb.net:27017,vandyhacksiv-shard-00-02-swivj.mongodb.net:27017/test?ssl=true&replicaSet=VandyHacksIV-shard-0&authSource=admin')['vandyhacks']
	products = db.products

	# newProduct = {
	# 	"name": "cookout",
	# 	"price": "4.94",
	# 	"unit": "tray"
	# }
	# print (products)
	# id = products.insert_one(newProduct).inserted_id
	# print("id is ", id)

	# for product in list(db.products.find()):
	# 	print(product)

def getAmazonProductInfo():
	# use Bottlenose to access Amazon Product Advertising API
	AWS_ACCESS_KEY_ID = 'AKIAJIOGJFBGV2UXRUAQ'
	AWS_SECRET_ACCESS_KEY = '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'
	AWS_ASSOCIATE_TAG = 'sunny8751-20'
	amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)

	# response = amazon.ItemSearch(Keywords="Kindle 3G", SearchIndex="All", ResponseGroup="Offers")
	# print(response)
	# responseXML = StringIO(response)
	# response = amazon.ItemLookup(ItemId="B007OZNUCE", ResponseGroup="Offers")
	# print(response)
	# for event, elem in etree.iterparse(responseXML, events=('start-ns',)):
	# 	print elem

	# root = etree.parse("other.xml").getroot()
	# print (root.tag)
	# for child in root:
	# 	print(child.tag, child.attrib)

	def getMap(root):
		if len(root) == 0:
			return root
		map = {}
		for child in root:
			tag = child.tag[child.tag.index('}') + 1:]
			map[tag] = getMap(child)
		return map

	#parse the xml into an ElementTree
	response = etree.parse("output.xml").getroot()
	#convert ElementTree into map
	response = getMap(response)
	print(response["Items"]["Item"])

# main code