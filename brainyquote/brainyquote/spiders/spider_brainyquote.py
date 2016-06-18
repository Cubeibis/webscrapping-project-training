# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from brainyquote.items import BrainyquoteItem
from scrapy.shell import inspect_response

class SpiderBrainyquoteSpider(CrawlSpider):
    name            = 'spider_brainyquote'
    allowed_domains = ['brainyquote.com']
    start_url       = 'http://www.brainyquote.com'
    # start_urls      = ['http://www.brainyquote.com']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        return [scrapy.Request(url=self.start_url, callback=self.first_quotes)]
    ## End start_requests

    def first_quotes(self, response):        
        inspect_response(response, self)
        for individual_author in response.xpath($x('//div[contains(@class, "bq_s")]//div[contains(@class, "bq_fl")]//div[contains(@class ,"bqLn")]'))
        author_name = individual_author.xpath('./a/text()').extract_first()
        author_link = individual_author.xpath('./a/@href').extract_first()
        self.logger.info('INFORMATION: {}'.format(author_name))

    ## End first_quotes

    def parse_item(self, response):        
        i = BrainyquoteItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
