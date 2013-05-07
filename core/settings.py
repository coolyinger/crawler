# Scrapy settings for umcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'core'

SPIDER_MODULES = ['core.spiders']
NEWSPIDER_MODULE = 'core.spiders'

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 10,

}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'umcrawler (+http://www.yourdomain.com)'
