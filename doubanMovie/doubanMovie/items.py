# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class DoubanMovieItem(Item):
    subject_id = Field() # the douban subject id
    name = Field() # movie name
    year = Field() # year
    cover_url = Field() # img cover url
    directors = Field() # directors name and url
    writers = Field() # writers name and url
    actors = Field() # stars and url
    genres = Field() # genres
    countries = Field() # countries
    languages = Field() # langaues
    release_date = Field() # premiere date and country
    running_time = Field() # running time
    alias = Field() # alias
    imdb_link = Field() # imdb link
    rating = Field() # the movie rating
    rating_num = Field() # the people num that rating movie
    summary = Field() # summary
    tags = Field() # the most used tags for the movie

