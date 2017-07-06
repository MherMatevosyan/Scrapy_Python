# -*- coding: utf-8 -*-
import scrapy


class PstackSpider(scrapy.Spider):
    name = 'pstack'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions/tagged/python?page=1&sort=votes&pagesize=15',
    'http://stackoverflow.com/questions/tagged/python?page=2&sort=votes&pagesize=15',
    'http://stackoverflow.com/questions/tagged/python?page=3&sort=votes&pagesize=15']

    def parse(self, response):
        for i in response.css('div.summary'):
        	yield {
        	'question': i.css('h3 a::text').extract_first(),
        	'link': i.css('h3 a::attr(href)').extract_first()
        	}
