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

    market = "AnzhItem"
    start_urls = [
            "http://www.anzhi.com/soft_814844.html",
            "http://anzhi.com/soft_743451.html",
            ]

    log.setup_logging ("test", "1.0")

    marketConfig = config_factory.get_market_config (market)
    allowed_domains = []
    allowed_domains.append (marketConfig.domain)

    def parse (self, response):
        logging.debug ("parse url: %s" % response.url)
        item = CoreItem ()
        item["market"] = self.market
        self.marketConfig.parse (response, item)
        print '\n===================================================\n'
        for k, v in item.items ():
            if k == "related_app":
                print k
                for rela in v:
                    print "%-20s : %s" % ("", rela.encode ("utf-8"))
                continue
            if isinstance (v, unicode):
                print "%-20s : %s" % (k, v.encode ("utf-8"))
            elif isinstance (v, list):
                print "%-20s : %s" % (k, pprint.pformat (v, indent = 20))
            else:
                print "%-20s : %s" % (k, v)
        return item

