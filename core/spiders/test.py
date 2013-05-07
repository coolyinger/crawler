from scrapy.spider import BaseSpider

class TestSpider(BaseSpider):
    name = "test"
    allowed_domains = ['baidu.com']
    start_urls = (
            'http://www.appchina.com/app/com.moji.mjweather/',
            'http://www.baidu.com/',
        )

    def parse(self, response):
        self.log ("A response from %s just arrived!" % response.url)
