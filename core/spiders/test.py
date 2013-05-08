from scrapy.spider import BaseSpider
from core.items import CoreItem

import os
from os import path
import sys
import logging

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../../src')
sys.path.append(working_dir)
import conf
import log

class TestSpider(BaseSpider):
    name = "test"

    log.setup_logging (conf.APP_NAME, False)
#
#    market = sys.stdin.readline ().strip ()
#    start_urls = eval (sys.stdin.readline ().strip ())
#    category_general = sys.stdin.readline ().strip ()
#    rule = sys.stdin.readline ().strip ()
#    sys.stdin.flush ()

    allowed_domains = ['hiapk.com']

    def parse(self, response):
        logging.debug (" ==== A response from %s just arrived!" % response.url)

    def make_requests_from_url (self, url):

        print '=============', url
        logging.debug ("crawling %s" % url)

        return super (TestSpider, self).make_requests_from_url (url)
