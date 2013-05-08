#!/bin/env python
#-*- coding:utf-8 -*-

from baseclass import baseclass

class WanDouJiaItemConfig(baseclass):
    domain = "wandoujia.com"

#    config = {
#        "name": {
#            "select": '//div[@class=\"app-tile clearfix\"]/h3[@class=\"name\"]/text()',
#            "result": [0],
#        },
#
#        "update_time": {
#            "select": "//ul[@class=\"app-meta\"]/li[5]/span[2]/text()",
#            "result": [0]
#        },
# 
#        "app_version": {
#            "select": "//ul[@class=\"app-meta\"]/li[2]/span[@class=\"meta\"]/text()",
#            "result": [0]
#        },
#
#        "size": {
#            "select": "//ul[@class=\"app-meta\"]/li[1]/span[@class=\"meta\"]/text()",
#            "result": [0]
#        },
#
#        "icon": {
#            "select": "//span[@class=\"img-wp\"]/img/@src",
#            "result": [0]
#        },
#
#        "download_num": {
#            "select": "//ul[@class=\"app-meta\"]/li[4]/span[2]/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        "description": {
#            "select": "//div[@class=\"description\"]/text()",
#            "result": [0]
#        },
#
#        "images": {
#            "select": "//div[@class=\"carousel-items clearfix\"]/img/@src"
#        },
#
#        #TODO rate
#        #"rate": {
#        #    "select": ""
#        #},
#
#        "category_detail": {
#            "select": "//ul[@class=\"app-meta\"]/li[3]/a/text()",
#            "result": [0]
#        },
#
#        "package_name": {
#            "select": "//div[@class=\"app-install\"]/a/@data-packagename",
#            "result": [0]
#        },
#
#        "comment_url": {
#            "select": "//div[@class=\"app-install\"]/a/@data-packagename",
#            "result": [0]
#        }
#    }
#
#    def extraction_postprocess(self, atr_name, raw_data):
#        if atr_name == "download_num":
#            num_str_list = re.findall(r'\d+', raw_data)
#            if num_str_list:
#                num = int(num_str_list[0])
#
#                if u"万次" in raw_data:
#                    num *= 10000
#
#                return num
#
#        elif atr_name == "comment_url":
#            url = "http://comment.wandoujia.com/comment/comment!getCommentSummary.action?callback=handleCommentData&target=%s&pageNum=1&pageSize=10" % raw_data
#
#            return url
#
#        return raw_data

