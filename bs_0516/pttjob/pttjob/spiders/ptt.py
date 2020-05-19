# -*- coding: utf-8 -*-
import scrapy


class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/']

    def parse(self, response):
        pass
