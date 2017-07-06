# -*- coding: utf-8 -*-
import scrapy
import json


class DirectorsSpider(scrapy.Spider):
    name = 'directors'
    allowed_domains = ['imdb.com']
    start_urls = []

    #################################################################################################
    ### To generate the json needed you need to run the spider "top_movie" then change the directory
    ### of the json file in this spider. I copied the json file to this spider's directory.
    ### If you don't want a new json file you can simply put # a line below and remove the other one.
    #################################################################################################

    with open ('C:\Data_scraping\imdb_top\imdb_top_movies.json') as f:
    #with open('imdb_top_movies.json') as f:
    	r=f.read()
    	d=json.loads(r)
    	for i in range(10): # change the range to get desired number of top movies
    		start_urls.append(d[i]['link'])

    def parse(self, response):
        yield{
        "movie": response.css('div.title_wrapper h1::text').extract_first(),
        "director": response.css('div.credit_summary_item span.itemprop::text').extract_first()
        }
