# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import os
import sys
import logging
import pprint
from scrapy.exceptions import DropItem

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../src')
sys.path.append(working_dir)

import config_factory
from mongoUtil import mongoUtil
import conf

def log_item (item, new_app):
    if new_app:
        log_str = "crawl a new APP:\n"
    else:
        log_str = "modify a APP:\n"

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

class UmcrawlerPipeline(object):

    appmeta = mongoUtil (conf.DB, "appmeta",
                         conf.IP, conf.PORT)
    def process_item (self, item, spider):
        app_id = item.get ("app_id", None)
        app_ver = item.get ("app_version", None)
        market = item.get ("market", None)

        if (not app_id) or (not app_ver) or (not market):
            # filter crawled web which don't belong APP detail web
            raise DropItem("item name invalid: %s" % item)

        # store item
        key = {"app_id": app_id,
               "app_version": app_ver,
               "market": market}
        new_app = False

        cursor = self.appmeta.get_item_property (key)

        if cursor.count() == 0:
            new_app = True
            # report a new app is crawled
            pass

        self.appmeta.upsert_item (key, dict(item))
        log_item (item, new_app)
        return item
