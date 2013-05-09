from scrapy.spider import BaseSpider
from core.items import CoreItem

import os
from os import path
import sys
import logging
from core.items import CoreItem
import pprint

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../../market')
sys.path.append(working_dir)

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../../src')
sys.path.append(working_dir)

import config_factory
import log

class TestSpider(BaseSpider):
    name = "test"

    market = "HiApkItem"
    start_urls = [
            "http://apk.hiapk.com/html/2013/05/1445026.html",
            "http://apk.hiapk.com/html/2013/05/1434939.html",
            "http://cdn.market.hiapk.com/data/upload/2013/05_06/10/com.zdworks.android.zdclock_104048.apk",
            ]

    log.setup_logging ("test", False)

    marketConfig = config_factory.get_market_config (market)
    allowed_domains = []
    allowed_domains.append (marketConfig.domain)

    def parse (self, response):
        logging.debug ("parse url: %s" % response.url)
        item = CoreItem ()
        item["market"] = self.market
        self.marketConfig.parse (response, item)
        #print '\n===================================================\n'
        #for k, v in item.items ():
        #    if k == "related_app":
        #        print k
        #        for rela in v:
        #            print "%-20s : %s" % ("", rela.encode ("utf-8"))
        #        continue
        #    if isinstance (v, unicode):
        #        print "%-20s : %s" % (k, v.encode ("utf-8"))
        #    elif isinstance (v, list):
        #        print "%-20s : %s" % (k, pprint.pformat (v, indent = 20))
        #    else:
        #        print "%-20s : %s" % (k, v)
        return item

