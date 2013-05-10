#!/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import pprint
import scrapy
import logging
from scrapy.selector import HtmlXPathSelector

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../')
sys.path.append (working_dir)

from core.items import CoreItem

class baseclass (object):

    def __init__ (self):
        pass

    def parse (self, response, item):
        print '====', type(response)
        if not isinstance (response, scrapy.http.response.html.HtmlResponse):
            # crawl a non-text web ( exp: http://***.apk)
            logging.debug ("Skip non-text web:%s" % response.url)
            return item
        hxs = HtmlXPathSelector (response)

        for key, val in self.config.items ():
            if not "select" in val:
                continue

            # xpath processing
            try:
                result = hxs.select (val["select"])
                if "result" in val:
                    result = result[val["result"]]
                result = result.extract ()

                if not result:
                    raise Exception ("result is NULL")
            except Exception as E:
                log_str = "[XPATH-ERROR (%s)-(%s)-(%s)]: %s" % (self.domain,
                                                        key, response.url, E)
                logging.error (log_str)
                item[key] = ""
                continue

            # post processing
            if "additional" in val:
                func = val["additional"]
                try:
                    result = func (result)
                except Exception as E:
                    log_str = "[POST-PROC (%s)-(%s)]: %s" % (self.domain,
                                                    key, E)
                    logging.error (log_str)
                    result = ""

            item[key] = result
        return item
