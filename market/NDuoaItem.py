#!/bin/env python
# -*- coding: utf-8 -*-

import re
import datetime

from baseclass import baseclass

class NDuoaItemConfig(baseclass):
    domain = "nduoa.com"

    def __init__ (self):
        self.config = {
                "app_id": {
                    "select": "//div[@class=\"icon\"]/img/@src",
                    "result":0,
                    "additional": self.post_appid_nduoa,
                },

                "app_version": {
                    "select": "//div[@class=\"name\"]/span[@class=\"version\"]/text()",
                    "result": 0,
                    "additional": self.post_version_nduoa,
                },

                "market": {
                    # pass in
                },

                "name": {
                    "select": '//div[@class=\"name\"]/span[@class=\"title\"]/text()',
                    "result": 0
                },

                "size": {
                    "select": "//div[@class=\"apkinfo\"]/div[3]/text()",
                    "result": 0,
                    "additional": self.post_size_nduoa,
                },

                "language": {
                    "select": '//div[@class=\"name\"]/span[@class=\"title\"]/text()',
                    "result": 0,
                    "additional": self.post_lang_nduoa,
                },

                "package_name": {
                    # cannot found in web, parse by later
                },

                "developer": {
                    "select": "//div[@class=\"author row\"]/span/a/text()",
                    "result": 0,
                },

                "update_time": {
                    "select": "//div[@class=\"updateTime row\"]/em/text()",
                    "result": 0,
                    "additional": self.post_updatetime_nduoa,
                },

                "description": {
                    "select": "//div[@id=\"detailInfo\"]/div[@class=\"content\"]/div[@class=\"inner\"]",
                    "result": 0,
                    "additional": self.post_desc_nduoa,
                },

                "category_general": {
                    # pass in
                },

                "category_detail": {
                    "select": "//div[@id=\"breadcrumbs\"]/span[3]/a/text()",
                    "result": 0,
                },

                "icon": {
                    "select": "//div[@class=\"icon\"]/img/@src",
                    "result": 0
                },

                "images": {
                    "select": "//ul[@class=\"shotbox\"]/li/img/@src"
                },

                "comment_url": {
                    "select": "//div[@class=\"normal\"]/a[@class=\"d_pc_normal\"]/@href",
                    "result":0,
                    "additional": self.post_comenturl_nduoa,
                },

                "package_url": {
                    "select": "//div[@class=\"normal\"]/a[@class=\"d_pc_normal\"]/@href",
                    "result":0,
                    "additional": self.post_packageurl_nduoa,
                },

                "url": {
                        # pass in
                },

                "related_app": {
                    "select": "//ul[@class=\"apkbox apkbox_72 clearfix\"]/li/span[@class=\"name\"]/a/text()"
                },

                "os_support_version": {
                    "select": "//div[@class=\"adapt row popup\"]/h4/text()",
                    "result":0,
                },

                #"email": {
                #    "select": "//ul[@id=\"detail_line_ul\"]/li[6]/text()",
                #    "result":0,
                #    "additional": self.post_price_anzh,
                #},
                #"devpage": {
                #    "select": "//ul[@id=\"detail_line_ul\"]/li[6]/text()",
                #    "result":0,
                #    "additional": self.post_price_anzh,
                #},
            }

    def post_appid_nduoa (self, val_raw):
        appid_list = re.findall(r'(\d+)/icon', val_raw)
        if appid_list:
            return appid_list[0]

    def post_version_nduoa (self, val_raw):
        version = val_raw.strip('()')
        return version

    def post_size_nduoa (self, val_raw):
        size = val_raw[3:]
        return size

    def post_lang_nduoa (self, val_raw):
        if len (val_raw.encode ("utf-8")) != len (val_raw):
            return "ch"
        else:
            return "en"

    def post_updatetime_nduoa (self, val_raw):
        time_list = re.findall(r'\d+', val_raw)
        if time_list:
            time_format = "%Y-%m-%d"

            time_delta = int(time_list[0])
            today = datetime.date.today()

            if u"天前" in val_raw:
                d = datetime.timedelta(days = time_delta)
                update_time = today - d
                return update_time.strftime(time_format)
            else:
                return today.strftime(time_format)

    def post_desc_nduoa (self, val_raw):
        desc = re.sub (r'</?\w+[^>]*>', '', val_raw)
        return desc.strip()

    def post_comenturl_nduoa (self, val_raw):
        appid = re.findall(r'\d+', val_raw)[0]
        return "http://market.nduoa.com/webv2/ajax/getComments/targetType/1/targetId/%s/show/2/page/1" % appid

    def post_packageurl_nduoa (self, val_raw):
        return "http://www.nduoa.com%s" % val_raw

