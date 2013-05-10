#!/bin/env python
#-*- coding:utf-8 -*-

import re
from baseclass import baseclass

class HiApkItemConfig(baseclass):
    domain = "apk.hiapk.com"

    def __init__ (self):
        self.config = {
                "app_id": {
                    "select": "//a[@class=\"linkbtn d1\"]/@href",
                    "result":0,
                    "additional": self.post_appid_hiapk,
                },

                "app_version": {
                    "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftVersionName\"]/text()",
                    "result": 0,
                },

                "market": {
                    # pass in
                },

                "name": {
                    "select": '//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftName\"]/text()'  ,
                    "result": 0,
                },

                "size": {
                    "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftSize\"]/text()",
                    "result": 0,
                },

                "language": {
                    "select": '//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftName\"]/text()'  ,
                    "result": 0,
                    "additional": self.post_lang_hiapk,
                },

                "package_name": {
                    # cannot found, parse by decompilating
                },

                "developer": {
                    "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftDeveloper\"]/text()",
                    "result": 0,
                },

                "update_time": {
                    "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftPublishTime\"]/text()",
                    "result": 0,
                },

                "description": {
                    "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_Description\"]/text()",
                    "result": 0,
                },

                "category_general": {
                    # pass in
                },

                "category_detail": {
                    "select": "//span[@id=\"ctl00_AndroidMaster_Content_Soft_CurrentCategory\"]/text()",
                    "result": 0,
                },

                "icon": {
                    "select": "//div[@class=\"detail_content\"]/div[1]/div[1]/img/@src",
                    "result": 0
                },

                "images": {
                    "select": "//div[@class=\"screenimg\"]//img/@src",
                },

                "comment_url": {
                    "select": "//input[@id=\"PublishSoft_ApkId\"]/@value | //input[@id=\"PublishSoft_SoftCode\"]/@value",
                    "result":1000,
                    "additional": self.post_commenturl_hiapk,
                },

                "package_url": {
                    "select": "//a[@class=\"linkbtn d1\"]/@href",
                    "result":1000,
                    "additional": self.post_packageurl_hiapk,
                },

                "url": {
                        # pass in
                },

                "related_app": {
                    "select": "//div[@id=\"relatedSoftBox\"]//dt/a/text()",
                },

                "os_support_version": {
                    "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftSuitSdk\"]/text()",
                    "result":0,
                },

                #"price": {
                #    "select": "//ul[@id=\"detail_line_ul\"]/li[6]/span/text()",
                #    "result":0,
                #    "additional": self.post_price_anzh,
                #},

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

    def post_appid_hiapk (self, val_raw):
        val = re.findall(r'[0-9].*[0-9]', val_raw, re.M)[0]
        return val

    def post_lang_hiapk (self, val_raw):
        if len (val_raw.encode ("utf-8")) != len (val_raw):
            return "ch"
        else:
            return "en"

    def post_commenturl_hiapk (self, val_raw):
        return val_raw

    def post_packageurl_hiapk (self, val_raw):
        return val_raw
