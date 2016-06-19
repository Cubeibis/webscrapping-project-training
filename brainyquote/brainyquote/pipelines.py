# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo, logging

class BrainyquotePipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
	collection_name = 'brainy_quote'

	def __init__(self, mongo_uri, mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db  = mongo_db
	## End __init__

	@classmethod
	def from_crawler(cls, crawler):
	    return cls(
	        mongo_uri=crawler.settings.get('MONGO_URI'),
	        mongo_db=crawler.settings.get('MONGO_DATABASE')
	    )
	## End from_crawler

	def open_spider(self, spider):		
		self.client     = pymongo.MongoClient(self.mongo_uri)				
		self.db         = self.client[self.mongo_db]		
		self.collection = self.db[self.collection_name]
		self.collection.create_index([("author_name", 1), ("quote", 1)])
	## End open_spider

	def close_spider(self, spider):
	    self.client.close()
	## End close_spider

	def process_item(self, item, spider):
	    logging.warning('** Mongo to insert {}'.format(dict(item)))

	    #We need to convert the item into dict format and insert into the database
	    dict_item = dict(item) 
	    verify_item = self.collection.find_one({'author_name': dict_item['author_name'], 'quote': dict_item['quote']})

	    if verify_item is None:
	    	self.collection.insert_one(dict_item)
	    
	    return item
	## End process_item
## End MongoPipeline