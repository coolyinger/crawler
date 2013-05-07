#!/bin/env python
#-*- coding:utf-8 -*-

import fcntl
import os
import sys
import log
import logging
import optparse

import conf
from crawler import Crawler

APP_NAME = 'xlcrawler'
APP_VERSION = "1.0"

def parse_commandline ():

    optParse = optparse.OptionParser (version = APP_VERSION,
                                    usage = APP_NAME + " [options]")
    optParse.add_option ("--test", action = "store_true", dest = "test",
                         help = "crawling few link to test XPATH",
                         default = False)
    optParse.add_option ("--clean", action = "store_true", dest = "clean",
                         help = "cleanup expired DATA and FILE",
                         default = False)
    return optParse.parse_args ()


def crawl_clean ():
    print "=========== crawl clean ...."

def main ():

    log.setup_logging (APP_NAME, True)

    (option, ignore) = parse_commandline ()

    if not conf.check_config ():
        sys.exit (1)

    logging.info ("%s startup by %s" % (APP_NAME, sys.argv))

    if option.clean:
        crawl_clean ()
        return


    crawler = Crawler (testmode = option.test)
    crawler.start ()

    logging.info ("%s finish ..." % APP_NAME)

if __name__ == "__main__":
    main ()
