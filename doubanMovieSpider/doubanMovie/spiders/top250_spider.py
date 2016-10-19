# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from spider_helper import parse_movie_item

class MoiveSpider(CrawlSpider):
    name="movieTop250"
    allowed_domains=["movie.douban.com"]
    start_urls=["https://movie.douban.com/top250"]
    rules=[
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')),callback="parse_movie_item"),
    ]

    
