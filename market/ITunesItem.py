#!/bin/env python
#-*- coding:utf-8 -*-

from baseclass import baseclass

class ITunesItemConfig(baseclass):
    domain = "itunes.apple.com"

#    config = {
#        "name": {
#            "select": "//div[@id=\"title\"]/div[@class=\"left\"]/h1/text()",
#            "result": [0],
#        },
#
#        "update_time": {
#            "select": "//li[@class=\"release-date\"]/text()",
#            "result": [0]
#        },
#
#        "app_version": {
#            "select": "//div[@class=\"lockup product application\"]/ul/li[4]/text()",
#            "result": [0],
#        },
#
#        "developer": {
#            "select": "//div[@id=\"title\"]/div[@class=\"left\"]/h2/text()",
#            "result": [0],
#        },
#        "icon": {
#            "select" :"//div[@class=\"lockup product application\"]/a/div/img/@src",
#            "result": [0]
#        },
#
#        "description": {
#            "select": u"//div[@metrics-loc=\"Titledbox_内容提要\"]/p".encode('utf8')
#        },
#
#        "images": {
#            "select": "//div[@class=\"content iphone-screen-shots\"]/div/div/img/@src"
#        },
#
#        "related_app": {
#            "select": "//div[@class=\"swoosh lockup-container application large\"]//div[@class=\"lockup small application\"]//li[1]/a/text()",
#        },
#
#        'devpage': {
#            "select": "//div[@class=\"app-links\"]/a[2]/@href",
#            "result": [0],
#        },
#
#        'rate': {
#            "select": "//div[@class=\"extra-list customer-ratings\"]/div[2]/div/span",
#            'additional': True,
#        },
#
#        'rate_num': {
#            "select": "//div[@class=\"extra-list customer-ratings\"]/div[2]/span",
#            "result": [0],
#            'additional': True,
#        },
#
#        'all_rate': {
#            "select": "//div[@class=\"extra-list customer-ratings\"]/div[4]/div/span",
#            'additional': True,
#        },
#
#        'all_rate_num': {
#            "select": "//div[@class=\"extra-list customer-ratings\"]/div[4]/span",
#            "result": [0],
#            'additional': True,
#        },
#
#        'category_detail': {
#            "select": "//div[@class=\"lockup product application\"]/ul/li[2]/a/text()",
#            "result": [0],
#            'additional': True,
#        },
#
#        'size': {
#            'select': "//div[@class=\"lockup product application\"]/ul/li[5]/text()",
#            'result': [0]
#        },
#
#        'price': {
#            "select": "//div[@class=\"lockup product application\"]/ul/li[1]/div/text()",
#            "result": [0]
#        },
#
#        "comment_url": {
#            "select": "//div[@class=\"lockup product application\"]/a[1]/@href",
#            "result": [0],
#            "additional": True
#        },
#
#        'app_id': {
#            "select": "//div[@class=\"lockup product application\"]/a[1]/@href",
#            "result": [0],
#            "additional": True
#        }
# 
#    }
#
#    #should rename to postprocess 
#    def extraction_postprocess(self, atr_name, raw_data):
#        try:
#            if atr_name == 'update_time':
#                ''' Apr 20, 2011 '''
#                the_time = time.strptime(raw_data, '%b %d, %Y')
#                return time.strftime("%Y-%m-%d", the_time)
#            elif atr_name == 'app_id':
#                appid = re.findall(r'id(\d+)', raw_data)[0]
#                return appid
#            elif atr_name == 'rate' or atr_name == 'all_rate':
#                cl_list = [re.findall(r'"(.+)"', span)[0] for span in raw_data]
#                return cl_list.count('rating-star') + 0.5 * cl_list.count('rating-star half')
#            elif atr_name == 'rate_num' or atr_name == 'all_rate_num':
#                num = re.findall(r'\d+', raw_data)[0]
#                return num
#            elif atr_name == 'comment_url':
#                appid = re.findall(r'id(\d+)', raw_data)[0]
#                comment_url = "http://itunes.apple.com/WebObjects/MZStore.woa/wa/customerReviews?update=1&id=%s&displayable-kind=11&appVersion=current&page=1&sort=4" % appid
#                return comment_url
#            elif atr_name == 'category_detail':
#                cate = CategoryMap.CategoryDetailMapDic["ITunesItem"].get(raw_data,"Others")
#                if cate == 'Others':
#                    return raw_data
#                return cate
#            return raw_data 
#        except Exception as error:
#            e = traceback.format_exc()
#            logger.error(e)
