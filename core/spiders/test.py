from scrapy.spider import BaseSpider

class TestSpider(BaseSpider):
    name = "test"
    allowed_domains = ["appchina.com"]
    start_urls = (
            'http://www.appchina.com/app/com.moji.mjweather/',
        )

    def parse(self, response):
        filename = response.url.split ('/')[-2]

        open (filename, "wb").write (response.body)
        pass 
