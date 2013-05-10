#!/bin/env python
# -*- coding: utf-8 -*-

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
                    "result": [0]
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

    def post_appid_nduoa (self, val_raw):
        appid_list = re.findall(r'(\d+)/icon', raw_data)
        if appid_list:
            return appid_list[0]

    def post_version_nduoa (self, val_raw):
        version = raw_data.strip('()')
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

            if u"天前" in raw_data:
                d = datetime.timedelta(days = time_delta)
                update_time = today - d
                return update_time.strftime(time_format)
            else:
                return today.strftime(time_format)

    def post_desc_nduoa (self, val_raw):
        desc = re.sub (r'</?\w+[^>]*>', '', raw_data)
        return desc.strip()



    


   

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

