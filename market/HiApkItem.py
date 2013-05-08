#!/bin/env python
#-*- coding:utf-8 -*-

from baseclass import baseclass

class HiApkItemConfig(baseclass):
    domain = "apk.hiapk.com"

#    config = {
#        "name": {
#            "select": '//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftName\"]/text()'  ,
#            "result": [0],
#        },
#
#        "update_time": {
#            "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftPublishTime\"]/text()",
#            "result": [0]
#        },
#
#        "app_version": {
#            "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftVersionName\"]/text()",
#            "result": [0]
#        },
#
#        "developer": {
#            "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftDeveloper\"]/text()",
#            "result": [0]
#        },
#
#        "icon": {
#            "select": "//div[@class=\"detail_content\"]/div[1]/div[1]/img/@src",
#            "result": [0]
#        },
#
#        "download_num": {
#            "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_Download\"]/text()",
#            "result": [0],
#        },
#
#        "package_url": {
#            "select": "//a[@class=\"linkbtn d1\"]/@href",
#            "result": [0]
#        },
#
#        "description": {
#            "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_Description\"]/text()"
#        },
#
#        "images": {
#            "select": "//div[@class=\"screenimg\"]//img/@src",
#        },
#
#        "related_app": {
#            "select": "//div[@id=\"relatedSoftBox\"]//dt/a/text()",
#        },
#
#        "comment_url": {
#            "select": "//input[@id=\"PublishSoft_ApkId\"]/@value | //input[@id=\"PublishSoft_SoftCode\"]/@value",
#            "additional": True
#        },
#
#        "size": {
#            "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_SoftSize\"]/text()",
#            "result": [0]
#        },
#
#        "app_id": {
#            "select": "//a[@class=\"linkbtn d1\"]/@href",
#            "result": [0],
#            "additional":True
#        },
#
#        "category_detail": {
#            "select": "//span[@id=\"ctl00_AndroidMaster_Content_Soft_CurrentCategory\"]/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        "rate": {
#            "select": "//div[@class=\"star_num\"]/text()",
#            "result": [0],
#        },
#
#        "rate_num": {
#            "select": "//div[@class=\"font14 star_human\"]/text()",
#            "result": [0],
#            "additional": True
#        },
#
#    }
#
#    def extraction_postprocess(self, atr_name, additional):
#        
#        if atr_name == "package_url":
#            base_url = 'http://static.apk.hiapk.com/'
#            return "%s%s" % (base_url, additional)
#        elif atr_name == 'app_id':
#            appid = re.findall(r'\d+', additional)[0]
#            return appid
#        elif atr_name == 'rate_num':
#            num = re.findall(r'\d+', additional)[0]
#            return num
#        elif atr_name == "comment_url":
#            if len(additional)>1:
#                url_to_request = "http://apk.hiapk.com/SoftDetails.aspx?action=FindApkSoftCommentListJson&apkId="+additional[0]+ \
#                                 "&softcode="+additional[1]+"&curPageIndex=1"
#                return url_to_request
#            else:
#                return ""
#        elif atr_name == "category_detail":
#            return CategoryMap.CategoryDetailMapDic['HiApkItem'].get(additional,"others")
#
