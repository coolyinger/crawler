#!/bin/env python
# -*- coding: utf-8 -*-

from baseclass import baseclass

class NDuoaItemConfig(baseclass):
    domain = "nduoa.com"

#    config = {
#        "name": {
#            "select": '//div[@class=\"name\"]/span[@class=\"title\"]/text()',
#            "result": [0]
#        },
#
#        "update_time": {
#            "select": "//div[@class=\"updateTime row\"]/em/text()",
#            "result": [0],
#            "additional": True
#        },
#        
#        "app_version": {
#            "select": "//div[@class=\"name\"]/span[@class=\"version\"]/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        "developer": {
#            "select": "//div[@class=\"author row\"]/span/a/text()",
#            "result": [0]
#        },
#
#        "icon": {
#            "select": "//div[@class=\"icon\"]/img/@src",
#            "result": [0]
#        },
#
#        "download_num": {
#            "select": "//span[@class=\"count\"]/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        "description": {
#            "select": "//div[@id=\"detailInfo\"]/div[@class=\"content\"]/div[@class=\"inner\"]",
#            "result": [0],
#            "additional": True
#        },
#
#        "images": {
#            "select": "//ul[@class=\"shotbox\"]/li/img/@src"
#        },
#
#        "related_app": {
#            "select": "//ul[@class=\"apkbox apkbox_72 clearfix\"]/li/span[@class=\"name\"]/a/text()"
#        },
#
#        "level": {
#            "select": "//div[@class=\"levelCount\"]/span[@class=\"level\"]/text()",
#            "result": [0]
#        },
#
#        "rate": {
#            "select": "//div[@class=\"starWrap\"]/span[@class=\"star\"]/s/@class"
#        },
#
#        "category_detail": {
#            "select": "//div[@id=\"breadcrumbs\"]/span[3]/a/text()",
#            "result": [0]
#        },
#
#        "app_id": {
#            "select": "//div[@class=\"icon\"]/img/@src",
#            "result": [0],
#            "additional": True
#        },
#
#        "package_url": {
#            "select": "//div[@class=\"normal\"]/a[@class=\"d_pc_normal\"]/@href",
#            "result": [0],
#            "additional": True
#        },
#        'comment_url': {
#            "select": "//div[@class=\"normal\"]/a[@class=\"d_pc_normal\"]/@href",
#            "result": [0],
#            "additional": True
#        }
#    }
#
#    def extraction_postprocess(self, atr_name, raw_data):
#        if atr_name == "update_time":
#
#            time_list = re.findall(r'\d+', raw_data)
#            if time_list:
#                time_format = "%Y-%m-%d"
#
#                time_delta = int(time_list[0])
#                today = datetime.date.today()
#
#                if u"天前" in raw_data:
#                    d = datetime.timedelta(days = time_delta)
#                    update_time = today - d
#                    return update_time.strftime(time_format)
#                else:
#                    return today.strftime(time_format)
#
#        elif atr_name == "app_version":
#            version = raw_data.strip('()')
#            return version
#
#        elif atr_name == "download_num":
#            num_str_list = re.findall(r'\d+', raw_data)
#            num = 0
#            for num_str in num_str_list:
#                num *= 1000
#                num += int(num_str)
#
#            return num
#        elif atr_name == 'rate':
#            rate = 0
#            for value in raw_data:
#                if value == 'full':
#                    rate += 1
#                elif value == 'half':
#                    rate += 0.5
#            return rate
#
#        elif atr_name == "app_id":
#            appid_list = re.findall(r'(\d+)/icon', raw_data)
#            if appid_list:
#                return appid_list[0]
#
#        elif atr_name == "package_url":
#            return "http://www.nduoa.com%s" % raw_data
#
#        elif atr_name == 'comment_url':
#            appid = re.findall(r'\d+', raw_data)[0]
#            return "http://market.nduoa.com/webv2/ajax/getComments/targetType/1/targetId/%s/show/2/page/1" % appid
#        elif atr_name == "description":
#            desc = re.sub (r'</?\w+[^>]*>', '', raw_data)
#            return desc.strip()
#
#        return raw_data

