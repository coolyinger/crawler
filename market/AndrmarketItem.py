#!/bin/env python
#-*- coding:utf-8 -*-
import re

import CategoryMap
from baseclass import baseclass

class AndrmarketItemConfig (baseclass):
    domain = "play.google.com"

    def __init__ (self):
        self.config = {
                "app_id": {
                    "select": "//link[@rel=\"canonical\"]/@href",
                    "result":0,
                    "additional": self.post_appid_andr,
                },

                "app_version": {
                    "select": "//dd[@itemprop=\"softwareVersion\"]/text()",
                    "result": 0,
                },

                "market": {
                    # pass in
                },

                "name": {
                    "select": "//h1[@class=\"doc-banner-title\"]/text()",
                    "result": 0,
                },

                "size": {
                    "select": "//dd[@itemprop=\"fileSize\"]/text()",
                    "result": 0,
                },

                "language": {
                    "select": "//h1[@class=\"doc-banner-title\"]/text()",
                    "result": 0,
                    "additional": self.post_lang_andr,
                },

                "package_name": {
                    "select": "//link[@rel=\"canonical\"]/@href",
                    "result": 0,
                    "additional": self.post_packagename_andr,
                },

                "developer": {
                    "select": "//a[@class=\"doc-header-link\"]/text()",
                    "result": 0,
                },

                "update_time": {
                    "select": "//time[@itemprop=\"datePublished\"]/text()",
                    "result": 0,
                },

                "description": {
                    "select": "//div[@id=\"doc-original-text\"]",
                    "result": 0,
                    "additional": self.post_desc_andr,
                },

                "category_general": {
                    # pass in
                },

                "category_detail": {
                    "select": "//dl[@class=\"doc-metadata-list\"]/dd/a/text()",
                    "result": 0,
                    "additional": self.post_categorydetail_andr,
                },

                "icon": {
                    "select" :"//div[@class=\"doc-banner-icon\"]/img/@src",
                    "result": 0
                },

                "images": {
                    "select": "//div[@class=\"screenshot-image-wrapper goog-inline-block lightbox\"]/img/@src"
                },

                "comment_url": {
                    "select": '//input[@id=\"reviewAjaxUrl\"]/@value',
                    "result":0,
                    "additional": self.post_comenturl_andr,
                },

                #"package_url": {
                #       cannot found
                #},

                "url": {
                        # pass in
                },

                "related_app": {
                    "select": "//a[@class=\"common-snippet-title\"]/@title",
                },

                "os_support_version": {
                    "select": "//dt[@itemprop=\"operatingSystems\"]/following::dd/text()",
                    "result":0,
                },

                "price": {
                    "select": "//dd[@itemprop=\"offers\"]/text()",
                    "result": 0,
                },

                "email": {
                    "select": "//*[@id=\"details-tab-1\"]/div[2]/a[3]/@href",
                    "result":0,
                    "additional": self.post_email_andr,
                },

                "devpage": {
                    "select": "//div[@class=\"doc-overview\"]/a[@rel=\"nofollow\"]/@href",
                    "additional": self.post_devpage_andr,
                },
            }


    def post_appid_andr (self, val_raw):
        return val_raw[val_raw.rfind('=') + 1 : ]

    def post_lang_andr (self, val_raw):
        if len (val_raw.encode ("utf-8")) != len (val_raw):
            return "ch"
        else:
            return "en"

    def post_packagename_andr (self, val_raw):
        return val_raw[val_raw.rfind('=') + 1 : ]

    def post_desc_andr (self, val_raw):
        desc = re.sub (r'</?\w+[^>]*>', '', val_raw)
        return desc

    def post_categorydetail_andr (self, val_raw):
        category_detail = CategoryMap.CategoryDetailMapDic["AndrmarketItem"].get(val_raw, "Others")
        return category_detail

    def post_comenturl_andr (self, val_raw):
        comment_url = "https://play.google.com" + val_raw.replace('amp;','')
        return comment_url

    def post_email_andr (self, val_raw):
        if type(val_raw) == list and len(val_raw) > 0:
            email = val_raw[len(val_raw)-1]
            return email.replace('mailto:','')
        elif type(val_raw) == list and len(val_raw) == 0:
            return ''
        else:
            return val_raw.replace('mailto:','')

    def post_devpage_andr (self, val_raw):
        if type(val_raw) == list and len(val_raw) == 4:
            return val_raw[0]
        else:
            return ''
