#!/bin/env python
#-*- coding:utf-8 -*-

import fcntl
import os
import sys
import log
import logging
import optparse

import conf

APP_NAME = 'xlcrawler'
APP_VERSION = "1.0"

def pidfile_acquire (pidfile):
    fp = open (pidfile, "w")
    fcntl.lockf (fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    return fp

def pidfile_release (pidfile, pidfile_fd):
    fcntl.lockf (pidfile_fd, fcntl.LOCK_UN)
    os.unlink (pidfile)

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

def main ():

    log.setup_logging (APP_NAME, True)

    (option, ignore) = parse_commandline ()

    if not conf.check_config ():
        sys.exit (1)

    #logging.info ("%s startup ..." % APP_NAME)

    #pidfile_path = "%s.pid" % APP_NAME
    #pidfile_fd = pidfile_acquire (pidfile_path)

    #try:
    #    import time
    #    time.sleep (5)
    #finally:
    #    pidfile_release (pidfile_path, pidfile_fd)
    #logging.info ("%s finish ..." % APP_NAME)

if __name__ == "__main__":
    main ()
