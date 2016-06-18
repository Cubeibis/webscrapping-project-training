# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.shell import inspect_response

from brainyquote.items import BrainyquoteItem


class SpiderBrainyquoteSpider(CrawlSpider):
    name = 'spider_brainyquote'
    allowed_domains = ['brainyquote.com']
    start_url = ['http://www.brainyquote.com/']
    #start_urls = ['http://www.brainyquote.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_request(self):
        return[scrapy.Request(url=self.start_url,callback=self.first_quotes)]
    ## End of start requests

    def first_quotes(self,response):
        inspect_response(response, self)

    ## End of first quotes

    def parse_item(self, response):
        i = BrainyquoteItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
