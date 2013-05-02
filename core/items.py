# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CoreItem(Item):

    app_id = Field ()
    app_version = Field ()
    app_market = Field ()

    name            = Field ()
    size            = Field ()
    language        = Field ()
    package_name    = Field ()
    developer       = Field ()
    update_time     = Field ()
    description     = Field ()
    category_general = Field ()
    category_detail = Field ()
    icon            = Field ()
    screen_snapshot = Field ()
    #comment_url     = Field ()
    download_url    = Field ()
    url             = Field ()
    related_app     = Field ()
    os              = Field ()
    os_support_ver  = Field ()
    price           = Field ()
    #available       = Field ()
    email           = Field ()
    devpage         = Field ()
    all_rate        = Field ()
    all_rate_num    = Field ()
    rate            = Field ()
    rate_num        = Field ()
