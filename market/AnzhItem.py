#!/bin/env python
#-*- coding:utf-8 -*-

from baseclass import baseclass

class AnzhItemConfig(baseclass):
    domain = "anzhi.com"

#    config = {
#        "name": {
#            "select": '//div[@class=\"detail_line\"]/h3/text()',
#            "result": [0],
#        },
#
#        "update_time": {
#            "select": "//ul[@id=\"detail_line_ul\"]/li/text()",
#            "result": [1],
#            "additional": True
#        },
#
#        "developer": {
#            "select": "//div[@class=\"detail_line\"]/span/text()",
#            "result": [1],
#            "additional": True
#        },
#
#        "icon": {
#            "select": "//div[@class=\"detail_icon\"]/img/@src",
#            "result": [0]
#        },
#
#        "download_num": {
#            "select": "//ul[@id=\"detail_line_ul\"]//li/span/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        "size": {
#            "select": "//ul[@id=\"detail_line_ul\"]//li/span/text()",
#            "result": [1],
#            "additional": True
#        },
#
#        "package_url": {
#            "select": "//div[@class=\"detail_down\"]/a/@onclick",
#            "result": [0],
#            "additional": True
#        },
#
#        "app_version": {
#            "select": "//div[@class=\"detail_line\"]/span/text()",
#            "result": [0],
#            "additional": True
#        },
#
#        "description": {
#            "select": "//div[@class=\"app_detail_infor\"]/p/text()"
#        },
#
#        "images": {
#            "select": "//ul[@id=\"detail_slider_ul\"]/li/img/@src"
#        },
#
#        "related_app": {
#            "select": "//ul[@class=\"recommend2 hotlist\"]/li/a/@title"
#        },
#
#        "comment_url": {
#            "select": "//div[@id=\"op_left\"]/a[1]/@href | //div[@class=\"imgoutbox\"]/ul/li[last()]/img/@src",
#            "additional": True
#        },
#
#        "app_id": {
#            "select": "//div[@class=\"detail_down\"]/a/@onclick",
#            "result":[0],
#            "additional": True
#        },
#
#        "category_detail": {
#            "select": "//ul[@id=\"detail_line_ul\"]/li/text()",
#            "result": [0],
#            "additional": True
#        }
#    }
#
#    def extraction_postprocess(self,atr_name,additional): 
#        ch_map = {'万':10000, '千':1000}        
#        try:
#            if atr_name == "update_time" or atr_name == "app_version":
#                return re.findall(r'[0-9].*[0-9]',additional,re.M)[0]
#
#            elif atr_name == "download_num":
#                result = 0
#                if additional not in ['',None,[]]:
#                    base = re.findall(r'[0-9]{0,}',additional,re.M)
#                    base = ''.join(base)
#                    if base != '':
#                        for k,v in ch_map.iteritems():
#                            if k in additional.encode('utf-8'):
#                                result = int(base)*v
#                                break
#                return str(result)
#
#            elif atr_name == "size":
#                return re.findall(r'[0-9].*[0-9].*',additional,re.M)[0]
#            elif atr_name == "developer":
#                return additional[4:].strip()
#            elif atr_name == "comment_url":
#                if len(additional)>1:
#                    apk_id = re.findall(r'[0-9].*[0-9]',additional[0],re.M)[0]
#                    str_list = additional[1].split('/')
#                    t_pkg_name = str_list[len(str_list)-1].rsplit('.',1)[0]
#                    url = "http://www.anzhi.com/comment.php?softid="+apk_id+"&package="+t_pkg_name+"&rand=0.2&c_page=0"
#                    return url
#                else:
#                    return ""
#                    '''
#                    tag_regex_list = ["<h2(.*).*</h2>","<span(.*).*</span>","<div class=\"cot l\">.*</div>"]
#                    myHTMLParser = MyHTMLParser()
#                    return myHTMLParser.start_parsing(url, tag_regex_list)
#                else:
#                    return additional
#                    '''
#            elif atr_name == "app_id":
#                if len(additional)>0:
#                    try:
#                        app_id = re.findall(r'[0-9].*[0-9]',additional,re.M)[0]
#                    except Exception:
#                        app_id = -1
#                else:
#                    app_id = -1
#                return app_id 
#            elif atr_name == 'package_url':
#                app_id = re.findall(r'[0-9]+', additional)[0]
#                pkg_url = "http://www.anzhi.com/dl_app.php?s=%s&n=5" % app_id
#                return pkg_url
#
#            elif atr_name == "category_detail":
#                category_detail_raw = additional.split(u"：")
#                category_detail = ""
#                if len(category_detail_raw) > 1:
#                    category_detail = CategoryMap.CategoryDetailMapDic["AnzhItem"].get(category_detail_raw[1],"Others")
#                return category_detail
#        except Exception as E: 
#            logger.error('parse additional info error: %s' % atr_name)
#            return additional

