#!/bin/env python
#-*- coding:utf-8 -*-

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

                "version_name": {
                    # non use
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
                    "select": "//label[@id=\"ctl00_AndroidMaster_Content_Apk_Description\"]/text()"
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

    def post_appid_hiapk (self, val_raw):
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

    def post_lang_hiapk (self, val_raw):
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
