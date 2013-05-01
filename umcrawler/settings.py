# Scrapy settings for umcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'umcrawler'

SPIDER_MODULES = ['umcrawler.spiders']
NEWSPIDER_MODULE = 'umcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'umcrawler (+http://www.yourdomain.com)'
