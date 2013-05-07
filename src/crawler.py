#!/bin/env python
#-*- coding:utf-8 -*-

import pymongo
from pymongo.connection import Connection

import conf
from mongoUtil import mongoUtil
from crawlerJob import crawlerJob

class Crawler (object):

    def __init__ (self, testmode = False):
        self.testmode = testmode
        self.starturls = mongoUtil (conf.DB, "starturl_test",
                                    conf.IP, conf.PORT)

    def start_test (self):
        """
            crawl few link to checking  whether XPATH need modify
        """
        print '=====test'

    def start (self):
        if self.testmode:
            self.start_test ()
            return

        if not conf.SLAVE:
            self.reset_starturls ()

        while 1:
            item = self.get_next_starturl ()
            if not item:
                break

            try:
                category_general = item["category_general"]
                links = map (lambda x: x.values()[0], item["links"])
                market = item["market"]
                rule = item["rule"]
            except KeyError:
                continue

            arglist = [market, links, category_general, rule]
            job = crawlerJob (arglist)
            job.start ()

    def reset_starturls (self):
        self.starturls.update_items ({}, {"locked_by_host":""})

    def get_next_starturl (self):
        item = self.starturls.find_and_modify (
                query = {"locked_by_host":"", "market": {"$in":conf.MARKETS}},
                update = {"$set": {"locked_by_host": conf.host},
                          "$inc": {"processed_count": 1}},
                sort = {"processed_count": 1},
                fields = ["market", "rule", "links", "category_general", "_id"])
        return item



def test ():
    crawl = Crawler ()
    crawl.start ()

if __name__ == "__main__":
    test ()
