# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CoreItem(Item):

    app_id              = Field ()
    app_version         = Field ()
    market              = Field ()

    name                = Field ()
    size                = Field ()
    language            = Field ()
    package_name        = Field ()
    developer           = Field ()
    update_time         = Field ()
    description         = Field ()
    category_general    = Field ()
    category_detail     = Field ()
    icon                = Field ()
    images              = Field ()
    comment_url         = Field ()
    package_url         = Field ()
    url                 = Field ()
    related_app         = Field ()
    os                  = Field ()
    os_support_version  = Field ()
    price               = Field ()
    available           = Field ()
    email               = Field ()
    devpage             = Field ()
    #all_rate        = Field ()
    #all_rate_num    = Field ()
    #rate            = Field ()
    #rate_num        = Field ()
