#!/bin/env python
#-*- coding:utf-8 -*-
from baseclass import baseclass

class AndrmarketItemConfig (baseclass):
    domain = "play.google.com"

#    config = {
#        "name": {
#            "select": '//h1[@class=\"doc-banner-title\"]/text()',
#            "result": [0],
#        },
#
#        "update_time": {
#            "select": "//time[@itemprop=\"datePublished\"]/text()",
#            "result": [0]
#        },
#
#        "app_version": {
#            "select": "//dd[@itemprop=\"softwareVersion\"]/text()",
#            "result": [0],
#        },
#
#        "developer": {
#            "select": "//a[@class=\"doc-header-link\"]/text()",
#            "result": [0]
#        },
#        "icon": {
#            "select" :"//div[@class=\"doc-banner-icon\"]/img/@src",
#            "result": [0]
#        },
#
#        "download_num": {
#            "select": "//dd[@itemprop=\"numDownloads\"]/text()",
#            "result": [0],
#        },
#        
#        "description": {
#            "select": "//div[@id=\"doc-original-text\"]",
#            "result": [0],
#            "additional": True
#        },
#
#        "images": {
#            "select": "//div[@class=\"screenshot-image-wrapper goog-inline-block lightbox\"]/img/@src"
#        },
#
#        "related_app": {
#            "select": "//a[@class=\"common-snippet-title\"]/@title",
#            "result": [0],
#            "additional": [0]
#        },
#
#        "email": {
#            "select": "//*[@id=\"details-tab-1\"]/div[2]/a[3]/@href",
#            "result": [0],
#            "additional": True
#        },
#
#        'level': {
#            "select": "//table[@class=\"doc-banner-table\"]/div[@class=\"badges-badge-title goog-inline-block\"]/text()",
#            "result": [0]
#        },
#
#        'devpage': {
#            "select": "//div[@class=\"doc-overview\"]/a[@rel=\"nofollow\"]/@href",
#            "additional": True
#        },
#
#        'rate': {
#            "select": "//td[@class=\"doc-details-ratings-price\"]/div/div[@class=\"ratings goog-inline-block\"]/@title",
#            "result": [0],
#            "additional": True
#        },
#
#        'rate_num': {
#            "select": "//td[@class=\"doc-details-ratings-price\"]/div/div[@class=\"goog-inline-block\"]/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        'category_detail': {
#            "select": "//dl[@class=\"doc-metadata-list\"]/dd/a/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        'price': {
#            "select": "//dd[@itemprop=\"offers\"]/text()",
#            "result": [0]
#        },
#
#        'package_name': {
#            "select": "//link[@rel=\"canonical\"]/@href",
#            "result": [0],
#            "additional": True
#        },
#
#        "comment_url": {
#            "select": '//input[@id=\"reviewAjaxUrl\"]/@value',
#            "result": [0],
#            "additional": True
#        },
#
#        'app_id': {
#            "select": "//link[@rel=\"canonical\"]/@href",
#            "result": [0],
#            "additional": True
#        }
# 
#    }
#
#    #should rename to postprocess 
#    def extraction_postprocess(self, atr_name, raw_data):
#        try:
#            if atr_name == "email":
#                if type(raw_data) == list and len(raw_data) > 0:
#                    email = raw_data[len(raw_data)-1]
#                    return email.replace('mailto:','')
#                elif type(raw_data) == list and len(raw_data) == 0:
#                    return ''
#                else:
#                    return raw_data.replace('mailto:','')
#            elif atr_name == 'devpage':
#                if type(raw_data) == list and len(raw_data) == 4:
#                    return raw_data[0]
#                else:
#                    return ''
#            elif atr_name == 'package_name' or atr_name == 'app_id':
#                if raw_data == None:
#                    return ''
#                else:
#                    return raw_data[raw_data.rfind('=') + 1 : ]
#            elif atr_name == 'comment_url':
#                comment_url = "https://play.google.com" + raw_data.replace('amp;','')
#                return comment_url
#            elif atr_name == 'category_detail':
#                category_detail = CategoryMap.CategoryDetailMapDic["AndrmarketItem"].get(raw_data,"Others")
#                return category_detail
#            elif atr_name == "description":
#                desc = re.sub (r'</?\w+[^>]*>', '', raw_data)
#                return desc
#            elif atr_name == "rate":
#                rate = re.search('\d[\._\d]*\d',raw_data)
#                return rate.group()
#            elif atr_name == "rate_num":
#                rateNum_str = raw_data.strip("()")
#                rateNum = int(rateNum_str.replace(',', ''))
#                return rateNum
#            return raw_data 
#        except Exception as error:
#            logger.error(error)
