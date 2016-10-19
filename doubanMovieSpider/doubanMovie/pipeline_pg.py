# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import uuid
from datetime import datetime

from scrapy import log
from twisted.enterprise import adbapi
import psycopg2

import settings


class PostgresqlPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['POSTGRESQL_HOST'],
            user=settings['POSTGRESQL_USER'],
            password=settings['POSTGRESQL_PASSWD'],
            database=settings['POSTGRESQL_DBNAME'],
            port=settings['POSTGRESQL_PORT']
            # cursorclass=psycopg2.extensions.cursor
        )
        dbpool = adbapi.ConnectionPool('psycopg2', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute(
            "select subject_id from public.movie where subject_id = %s",
            (item['subject_id'],))
        result = tx.fetchone()
        # log.msg(result,level=log.DEBUG)
        if result:
            log.msg("Item already stored in db:%s" % item, level=log.DEBUG)
        else:
            sql = ("INSERT INTO public.movie("
                   "uuid, update_time, subject_id, name, year, cover_url, "
                   "directors, writers, actors, genres, countries, languages, "
                   "release_date, running_time, alias, imdb_link, rating, "
                   "rating_num, summary, tags)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
                   " %s, %s, %s, %s, %s, %s, %s);")
            tx.execute(sql,
                       (str(uuid.uuid1()),
                        datetime.now(),
                        item['subject_id'].strip(),
                        item['name'][0].strip() if len(item['name']) > 0 else None,
                        item['year'][0] if len(item['year']) > 0 else None,
                        item['cover_url'][0] if len(item['cover_url']) > 0 else None,
                        map(lambda x: x.strip(), item['directors'][0].split('/')) if len(item['directors']) > 0 else None,
                        map(lambda x: x.strip(), item['writers'][0].split('/')) if len(item['writers']) > 0 else None,
                        map(lambda x: x.strip(), item['actors'][0].split('/')) if len(item['actors']) > 0 else None,
                        map(lambda x: x.strip(), item['genres'].split('/')),
                        map(lambda x: x.strip(), item['countries'][0].split('/')) if len(item['countries']) > 0 else None,
                        map(lambda x: x.strip(), item['languages'][0].split('/')) if len(item['languages']) > 0 else None,
                        item['release_date'][0].strip() if len(item['release_date']) > 0 else None,
                        int(item['running_time'][0]) if len(item['running_time']) > 0 else None,
                        map(lambda x: x.strip(), item['alias'][0].split('/')) if len(item['alias']) > 0 else None,
                        item['imdb_link'][0].strip() if len(item['imdb_link']) > 0 else None,
                        item['rating'][0] if len(item['rating']) > 0 else None,
                        item['rating_num'][0] if len(item['rating_num']) > 0 else None,
                        item['summary'][0].strip(' \t\n\r') if len(item['summary']) > 0 else None,
                        map(lambda x: x.strip(), item['tags']) if item['tags'] else None))
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
