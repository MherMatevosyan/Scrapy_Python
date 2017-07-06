# -*- coding: utf-8 -*-
import scrapy


class TopMovieSpider(scrapy.Spider):
    name = 'top_movie'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/chart/top/']

    def parse(self, response):
    	i=0
        for x in response.css('tr')[1:-2]:
        	yield{
        	'rank': x.css('td.titleColumn::text').re('[0-9]+')[0],
        	'title': x.css('td.titleColumn a::text').extract_first(),
        	'link': 'http://imdb.com'+str(x.css('td.titleColumn a::attr(href)').extract_first()),
        	'year': x.xpath('//td/span/text()').extract()[i],
        	'rating': x.css('td.ratingColumn.imdbRating strong::text').extract_first()
        	}
        	i+=1
        	
