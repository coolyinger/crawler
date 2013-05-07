#!/bin/env python
#-*- coding:utf-8 -*-

import pymongo
from pymongo.connection import Connection

import conf
from mongoUtil import mongoUtil

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

        self.reset_starturls ()

    def reset_starturls (self):
        self.starturls.update_items ({}, {"locked_by_host":""})


def test ():
    crawl = Crawler ()
    crawl.start ()

if __name__ == "__main__":
    test ()
