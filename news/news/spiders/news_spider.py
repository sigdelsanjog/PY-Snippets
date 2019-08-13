# -*- coding: utf-8 -*-
import scrapy


class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']//span[@class='text']/text()").extract()
        yield {'quotes': quotes}
