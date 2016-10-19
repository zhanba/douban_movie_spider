# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import uuid

from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request

import MySQLdb
import MySQLdb.cursors


class DoubanMoivePipeline(object):

    counter = 0

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            db='douban',
                                            user='webgiser',
                                            passwd='1234',
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=False
                                            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute(
            "select subject_id from movie where subject_id = %s", (item['subject_id'],))
        result = tx.fetchone()
        # log.msg(result,level=log.DEBUG)
        print "counter = " + str(DoubanMoivePipeline.counter) + "; subject_id = " + str(result)
        if result:
            log.msg("Item already stored in db:%s" % item, level=log.DEBUG)
        else:
            sql = ("INSERT INTO `movie` (`uuid`, `subject_id`, `name`, `year`, "
                   "`cover_url`, `directors`, `writers`, `actors`, `genres`, "
                   "`countries`, `languages`, `release_date`, `running_time`, "
                   "`alias`, `imdb_link`, `rating_num`, `rating_people`, "
                   "`summary`, `tags`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, "
                   "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
            tx.execute(sql,
                       (str(uuid.uuid1()), item['subject_id'], item['name'][0],
                        item['year'][0], item['cover_url'][
                            0], item['directors'][0],
                           item['writers'][0], item[
                               'actors'][0], item['genres'],
                           item['countries'][0], item['languages'][0],
                           item['release_date'][0], item['running_time'][0],
                           item['alias'][0], item['imdb_link'][
                               0], item['rating_num'][0],
                           item['rating_people'][0], item['summary'][0].strip(' \t\n\r'), item['tags']))
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)
            DoubanMoivePipeline.counter += 1

    def handle_error(self, e):
        log.err(e)
