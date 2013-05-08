#!/bin/env python
#-*- coding:utf8 -*-

from baseclass import baseclass

class AppchItemConfig(baseclass):
    domain = "appchina.com"

#    config = {
#        "name": {
#            "select": "//h1[@class=\"ch-name cutoff fl\"]/text()",
#            "result": [0]
#        },
#    
#        "package_url": {
#            "select": "//div[@class=\"down-box cf\"]/a[2]/@meta-url",
#            "result": [0]
#        },
#    
#        "download_num": {
#            "select": "//ul[@class=\"fl c-black info\"]/li[2]",
#            "result": [0],
#            "additional": True
#        },
#    
#        "app_version": {
#            "select": "//div[@class=\"ad fl c-black\"]/p[1]/text()",
#            "result": [0],
#            "additional": True
#        },
#    
#        "developer": {
#            "select": "//div[@class=\"app-authon\"]/p/span/text()",
#            "result": [0],
#        },
#    
#        "icon": {
#            "select": "//div[@class=\"app-name fl\"]/div/img/@src",
#            "result": [0]
#        },
#    
#        "images": {
#            "select": "//*[@id=\"makeMeScrollable\"]/a/@href"
#        },
#    
#        "size": {
#            "select": "//ul[@class=\"fl c-black info\"]/li[1]/text()",
#            "result": [0],
#            "additional": True
#        },
#    
#        "description": {
#            "select": "//div[@class=\"scroll-content\"]",
#            "result": [0],
#            "additional": True
#        },
#    
#        "related_app": {
#            "select": "//div[@class=\"similiar\"]/a[1]/@title"
#        },
#        
#        "comment_url": {
#            "select": "//input[@id=\"application_id\"]/@value",
#            "result": [0],
#            "additional": True
#        },
#    
#        "app_id": {
#            "select": "//div[@class=\"down-box cf\"]/a[2]/@meta-url",
#            "result": [0],
#            "additional": True
#        },
#    
#        "category_detail": {
#            "select": "//ul[@class=\"fl c-black info\"]/li[3]/text()",
#            "result": [0],
#            "additional": True
#        }
#    }
#    def extraction_postprocess(self,atr_name,additional):
#        try:
#            if atr_name == "app_version":
#                version = ""
#                if len(additional)>0:
#                    info = additional
#                    try:
#                        version = re.search('\d[\._\d]*\d',info)
#                        version = version.group()
#                    except Exception as E:
#                        version = ""
#                else:
#                    version = ""
#                return version
#            elif atr_name == "size":
#                size = ""
#                print 'size = ', additional
#                if len(additional)>0:
#                    info = additional     
#                    results = info.split(' ')
#                    try:
#                        size = results[0]
#                        size = re.search('[0-9].*',size)               
#                        size = size.group()            
#                        if len(results) > 1:
#                            size += results[1]
#
#                    except Exception as E:
#                        size = ""
#                else:
#                    size = ""
#                return size            
#              
#            elif atr_name == "comment_url":
#                comment_url = ""
#                if len(additional)>0:
#                    tmp_url = additional[0]
#                    bk_url = "www.appchina.com/market/comment/getcomments.action"
#                    try:
#                        apk_id = tmp_url
#                        comment_url = bk_url + "?application_id="+apk_id+"&start=0&size=100"
#                    except Exception as E:
#                        pass
#                return comment_url
#            
#            elif atr_name == "category_detail":
#                category_detail = CategoryMap.CategoryDetailMapDic["AppchItem"].get(additional,"Others")
#                return category_detail
#            elif atr_name == "download_num":
#                li = re.findall ("\d+", additional)
#                return str(li[1])
#            elif atr_name == "description":
#                desc = re.sub (r'</?\w+[^>]*>', '', additional)
#                return desc.strip()
#            elif atr_name == "app_id":
#                _id = re.search('\d[\._\d]*\d', additional)
#                _id = _id.group()
#                return str(_id)
#
#
#        except:
#            logger.error('parse additional info error: %s' % atr_name)
#            return additional
#

