# -*- coding: utf-8 -*-
import scrapy


class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['itcast.com']
    start_urls = ['http://www.itcast.com/']

    def parse(self, response):
        print response.body
