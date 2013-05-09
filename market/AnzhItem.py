#!/bin/env python
#-*- coding:utf-8 -*-

import re
import os

from baseclass import baseclass
import CategoryMap

class AnzhItemConfig(baseclass):
    domain = "anzhi.com"

    def __init__ (self):
        self.config = {
                "app_id": {
                    "select": "//div[@class=\"detail_down\"]/a/@onclick",
                    "result":0,
                    "additional": self.post_appid_anzh,
                },

                "app_version": {
                    "select": "//div[@class=\"detail_line\"]/span/text()",
                    "result": 0,
                    "additional": self.post_version_anzh,
                },

                "market": {
                    # pass in
                },

                "name": {
                    "select": '//div[@class=\"detail_line\"]/h3/text()',
                    "result": 0,
                },

                "size": {
                    "select": "//ul[@id=\"detail_line_ul\"]//li/span/text()",
                    "result": 1,
                    "additional": self.post_size_anzh,
                },

                "language": {
                    "select": '//div[@class=\"detail_line\"]/h3/text()',
                    "result": 0,
                    "additional": self.post_lang_anzh,
                },

                "package_name": {
                    "select": "//div[@class=\"detail_icon\"]/img/@src",
                    "result": 0,
                    "additional": self.post_packagename_anzh,
                },

                "version_name": {
                    # non use
                },

                "developer": {
                    "select": "//div[@class=\"detail_line\"]/span/text()",
                    "result": 1,
                    "additional": self.post_developer_anzh,
                },

                "update_time": {
                    "select": "//ul[@id=\"detail_line_ul\"]/li/text()",
                    "result": 1,
                    "additional": self.post_updatetime_anzh,
                },

                "description": {
                    "select": "//div[@class=\"app_detail_infor\"]/p/text()",
                    "result": 0,
                    "additional": self.post_desc_anzh,
                },

                "category_general": {
                    # pass in
                },

                "category_detail": {
                    "select": "//ul[@id=\"detail_line_ul\"]/li/text()",
                    "result": 0,
                    "additional": self.post_categorydetail_anzh,
                },

                "icon": {
                    "select": "//div[@class=\"detail_icon\"]/img/@src",
                    "result": 0
                },

                "images": {
                    "select": "//ul[@id=\"detail_slider_ul\"]/li/img/@src"
                },

                "comment_url": {
                    "select": "//div[@class=\"detail_down\"]/a/@onclick",
                    "result":0,
                    "additional": self.post_comenturl_anzh,
                },

                "package_url": {
                    "select": "//div[@class=\"detail_down\"]/a/@onclick",
                    "result":0,
                    "additional": self.post_packageurl_anzh,
                },

                "url": {
                        # pass in
                },

                "related_app": {
                    "select": "//ul[@class=\"recommend2 hotlist\"]/li/a/@title"
                },

                "os_support_version": {
                    "select": "//ul[@id=\"detail_line_ul\"]/li[5]/text()",
                    "result":0,
                    "additional": self.post_ossupport_anzh,
                },

                "price": {
                    "select": "//ul[@id=\"detail_line_ul\"]/li[6]/span/text()",
                    "result":0,
                    "additional": self.post_price_anzh,
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

    def post_updatetime_anzh (self, val_raw):
        val = '-'.join (re.findall (r'\d+', val_raw, re.M))
        return val

    def post_developer_anzh (self, val_raw):
        val = val_raw[4:].strip ()
        return val

    def post_appid_anzh (self, val_raw):
        val = re.findall(r'[0-9].*[0-9]', val_raw, re.M)[0]
        return val

    def post_version_anzh (self, val_raw):
        val = re.findall(r'[0-9].*[0-9]', val_raw, re.M)[0]
        return val

    def post_size_anzh (self, val_raw):
        val = val_raw[5:]
        return val

    def post_packagename_anzh (self, val_raw):
        base = os.path.basename (val_raw)
        val = base.split ('_')[0]
        return val

    def post_desc_anzh (self, val_raw):
        val = val_raw.strip ()
        return val

    def post_categorydetail_anzh (self, val_raw):
        category = val_raw[5:]
        val = CategoryMap.CategoryDetailMapDic["AnzhItem"].get(category,
                                                               "Others")
        return val

    def post_lang_anzh (self, val_raw):
        if len (val_raw.encode ("utf-8")) != len (val_raw):
            return "ch"
        else:
            return "en"

    def post_comenturl_anzh (self, val_raw):
        app_id = self.post_appid_anzh (val_raw)
        comment_url = "http://anzhi.com/comment.php?softid=%s" % app_id
        return comment_url

    def post_packageurl_anzh (self, val_raw):
        app_id = self.post_appid_anzh (val_raw)
        package_url = "http://anzhi.com/dl_app.php?s=%s&n=5" % app_id
        return package_url

    def post_ossupport_anzh (self, val_raw):
        os = val_raw[5:]
        return os

    def post_price_anzh (self, val_raw):
        price = val_raw[3:]
        return price
