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


def parse_commandline ():

    optParse = optparse.OptionParser (version = conf.APP_VERSION,
                                    usage = conf.APP_NAME + " [options]")
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

    log.setup_logging (conf.APP_NAME, False)

    (option, ignore) = parse_commandline ()

    if not conf.check_config ():
        sys.exit (1)

    logging.info ("%s startup by %s" % (conf.APP_NAME, sys.argv))

    if option.clean:
        crawl_clean ()
        return


    crawler = Crawler (testmode = option.test)
    crawler.start ()

    logging.info ("%s finish ..." % conf.APP_NAME)

if __name__ == "__main__":
    main ()
