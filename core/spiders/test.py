from scrapy.spider import BaseSpider
from scrapy import linkextractor

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

    market = "NDuoaItem"
    start_urls = [
            "http://www.nduoa.com/package/detail/11852",
            "http://www.nduoa.com/package/detail/7847",
            "http://www.nduoa.com/package/detail/189581",
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

        log_str = "crawl a APP:\n"
        for k, v in item.items ():
            if k == "related_app":
                log_str += "%s:\n" % k
                for rela in v:
                    log_str += "%-20s : %s\n" % ("", rela.encode ("utf-8"))
                continue
            if isinstance (v, unicode):
                log_str += "%-20s : %s\n" % (k, v.encode ("utf-8"))
            elif isinstance (v, list):
                log_str += "%-20s : %s\n" % (k, pprint.pformat (v, indent = 20))
            else:
                log_str += "%-20s : %s\n" % (k, v)
        logging.debug (log_str)
        return item
