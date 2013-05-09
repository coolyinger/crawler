from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from core.items import CoreItem

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
    market = sys.stdin.readline ().strip ()
    start_urls = eval (sys.stdin.readline ())
    category_general = sys.stdin.readline ().strip ()
    rule = sys.stdin.readline ().strip ()
    sys.stdin.flush ()

    marketConfig = config_factory.get_market_config (market)
    if not marketConfig:
        logging.error ("no market (%s)" % market)
        sys.exit (1)

    allowed_domains = []
    allowed_domains.append (marketConfig.domain)

    DEPTH_LIMIT = 1
    DEPTH_PRIORITY = 1
    SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

    rules = (
        Rule(SgmlLinkExtractor(allow = rule), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        logging.debug ("parse url: %s" % response.url)
        item = CoreItem ()
        item["market"] = self.market
        item["category_general"] = self.category_general
        item = self.marketConfig.parse (response, item)

        logging.debug ('\n============================================\n')
        for k, v in item.items ():
            if k == "related_app":
                print k
                for rela in v:
                    log_str = "%-20s : %s" % ("", rela.encode ("utf-8"))
                    logging.debug (log_str)
                continue
            if isinstance (v, unicode):
                log_str = "%-20s : %s" % (k, v.encode ("utf-8"))
                logging.debug (log_str)
            elif isinstance (v, list):
                log_str = "%-20s : %s" % (k, pprint.pformat (v, indent = 20))
                logging.debug (log_str)
            else:
                log_str = "%-20s : %s" % (k, v)
                logging.debug (log_str)
        return item

    def make_requests_from_url (self, url):
        logging.debug ("crawling starturl: %s" % url)
        return super (UmspiderSpider, self).make_requests_from_url (url)
