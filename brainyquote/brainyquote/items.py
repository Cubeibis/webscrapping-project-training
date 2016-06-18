# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BrainyquoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_name = scrapy.Field()
    quote = scrapy.Field()
    quote_image = scrappy.Field()
    amazon_source = scrapy.Field()
    categories = scrapy.Field
