# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider_helper import parse_movie_item, types, countries


class MoiveSpider(CrawlSpider):
    name = "movie"
    allowed_domains = ["movie.douban.com"]
    tag_url = u"https://movie.douban.com/tag/"
    # start_urls = [tag_url + str(x) for x in range(1880, 2016)] # parse by year
    tags = [i.decode('UTF-8') for i in types + countries]
    start_urls = [tag_url + x for x in tags] # parse by types and countries
    rules = [
        Rule(
            LinkExtractor(allow=(r'https://movie.douban.com/tag/\d+\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')),
             callback="parse_movie_item"),
    ]
