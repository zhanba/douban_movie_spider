# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from doubanMovie.items import DoubanMovieItem

class ALLMoiveSpider(CrawlSpider):
    name="doubanAllMovie"
    allowed_domains=["movie.douban.com"]
    tag_url = r"https://movie.douban.com/tag/"
    start_urls = [tag_url + str(x) for x in range(1880, 2016)]
    rules=[
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/\d+?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')),callback="parse_item"),
    ]

    def parse_item(self,response):
        sel=Selector(response)
        item=DoubanMovieItem()
        item['subject_id'] = response.url.split("/")[-2]
        item['name']=sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['cover_url']=sel.xpath('//*[@id="mainpic"]/a/img/@src').extract()
        item['directors']=sel.xpath('//*[@id="info"]/span[1]/span[2]').xpath('string(.)').extract()
        item['writers']=sel.xpath('//*[@id="info"]/span[2]/span[2]').xpath('string(.)').extract()
        item['actors']=sel.xpath('//*[@id="info"]/span[3]/span[2]').xpath('string(.)').extract()
        genre_list = sel.xpath('//*[@id="info"]/*[@property="v:genre"]/text()').extract()
        item['genres']='/'.join(genre_list)
        item['countries']=sel.xpath(u'//*[@id="info"]/*[text()="制片国家/地区:"]/following-sibling::text()[1]').extract()
        item['languages']=sel.xpath(u'//*[@id="info"]/*[text()="语言:"]/following-sibling::text()[1]').extract()
        item['release_date']=sel.xpath('//*[@id="info"]/*[@property="v:initialReleaseDate"]/@content').extract()
        item['running_time']=sel.xpath('//*[@id="info"]/*[@property="v:runtime"]/@content').extract()
        item['alias']=sel.xpath(u'//*[@id="info"]/*[text()="又名:"]/following-sibling::text()[1]').extract()
        item['imdb_link']=sel.xpath(u'//*[@id="info"]/*[text()="IMDb链接:"]/following-sibling::a[1]/text()').extract()
        item['rating']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item['rating_num']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract()
        item['summary']=sel.xpath('//*[@id="link-report"]/span[1]').xpath('string(.)').extract()
        item['tags']= sel.xpath('//*[@class="tags-body"]/*[text()]/text()').extract()
        return item
