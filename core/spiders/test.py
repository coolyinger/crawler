from scrapy.spider import BaseSpider
from core.items import CoreItem

import sys

class TestSpider(BaseSpider):
    name = "test"
    allowed_domains = ['baidu.com']

    market = sys.stdin.readline ().strip ()
    start_urls = eval (sys.stdin.readline ().strip ())
    category_general = sys.stdin.readline ().strip ()
    rule = sys.stdin.readline ().strip ()
    sys.stdin.flush ()

    print 'market = ', market
    print 'links = ', links
    print 'category = ', category_general
    print 'rule = ', rule

    def parse(self, response):
        print "A response from %s just arrived!" % response.url
