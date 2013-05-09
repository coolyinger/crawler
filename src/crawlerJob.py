#!/bin/env python
#-*- coding:utf-8 -*-

import subprocess
import logging
import pprint

class crawlerJob (object):

    # [market, links, category_general, rule]

    def __init__ (self, arglist):
        self.market = arglist[0].strip ()
        self.links = arglist[1]
        self.category_general = arglist[2]
        self.rule = arglist[3]

    def start (self):

        if len (self.links) == 0 or (not self.market):
            logging.warn ("Skip links: %s" % pprint.pformat (self.links))
            return

        subproc = subprocess.Popen("scrapy crawl UMSpider >out 2>&1",
                                   stdin = subprocess.PIPE, shell = True)
        subproc.stdin.write (self.market + "\n")
        subproc.stdin.write (str (self.links) + "\n")
        subproc.stdin.write (self.category_general + "\n")
        subproc.stdin.write (self.rule)
        subproc.stdin.flush ()
        subproc.communicate ()


def test ():
    arglist = []
    job = crawlerJob (arglist)
    job.start ()

if __name__ == "__main__":
    test ()
