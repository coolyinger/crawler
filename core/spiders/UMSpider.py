from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from core.items import CoreItem
from scrapy import linkextractor


import os
import logging
import sys
import pprint

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../../market')
sys.path.append(working_dir)

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../../src')
sys.path.append(working_dir)

import config_factory
import log, conf

class UmspiderSpider(CrawlSpider):
    name = 'UMSpider'

    log.setup_logging ("xlcrawler", False)
#    market = sys.stdin.readline ().strip ()
#    start_urls = eval (sys.stdin.readline ())
#    category_general = sys.stdin.readline ().strip ()
#    rule = sys.stdin.readline ().strip ()
#    sys.stdin.flush ()
#
#    marketConfig = config_factory.get_market_config (market)
#    if not marketConfig:
#        logging.error ("no market (%s)" % market)
#        sys.exit (1)
#
#    allowed_domains = []
#    allowed_domains.append (marketConfig.domain)
#
#    DEPTH_LIMIT = 1
#    DEPTH_PRIORITY = 1
#    SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
#    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
#
#    deny_ext = linkextractor.IGNORED_EXTENSIONS
#    deny_ext.append ('apk')
#
#    rules = (
#        Rule(SgmlLinkExtractor(allow = rule, deny_extensions = deny_ext),
#             callback='parse_item', follow=True),
#    )

    def parse_item(self, response):
        logging.debug ("parse url: %s" % response.url)
        item = CoreItem ()
        item["market"] = self.market
        item["url"] = response.url
        item["category_general"] = self.category_general
        item = self.marketConfig.parse (response, item)

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

    def make_requests_from_url (self, url):
        logging.debug ("crawling starturl: %s" % url)
        return super (UmspiderSpider, self).make_requests_from_url (url)
