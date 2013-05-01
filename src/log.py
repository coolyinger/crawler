#!/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import traceback
import logging
from logging import handlers
from datetime import datetime
try:
    import codecs
except ImportError:
    codecs = None

import config
import utils

class DateRotaingFileHandler (handlers.TimedRotatingFileHandler):

    def __init__ (self, base_dir, namebyPID = True, *args, **kwargs):
        super (DateRotaingFileHandler, self).__init__ (*args, **kwargs)
        self.base_dir = base_dir

    def doRollover (self):
        today = utils.get_today ()
        log_path = '%s/%s' % (self.base_dir, today)

        if not os.path.exists (log_path):
            os.makedirs (log_path)

        basename = os.path.basename (self.baseFilename)
        self.baseFilename = "%s/%s" % (log_path, basename)

        if self.encoding:
            self.stream = codecs.open(self.baseFilename, 'a', self.encoding)
        else:
            self.stream = open(self.baseFilename, 'a')
            self.rolloverAt = self.rolloverAt + self.interval


# @appname: log dir
# @namebyPID: whether devide different log-level into different file
#
def setup_logging (appname, namebyPID = True):

    FILE_NAME = "%s.log" % appname
    BASE_DIR = config.log_path
    FILE_MODE = "ae"
    FILE_FORMAT = "[%(asctime)s %(process)-5d] " \
            "%(levelname)-7s (%(filename)s:%(lineno)d) : %(message)s"
    DATEFMT = "%Y-%m-%d %H:%M:%S"

    CATEGORY = {"debug" : logging.DEBUG,
                "error" : logging.ERROR}

    log_dir = os.path.expanduser ("%s/%s" % (BASE_DIR, appname))
    if not os.access (log_dir, os.W_OK):
        if os.path.exists (log_dir):
            raise RuntimeError ("No write access to %s" % log_dir)
        try:
            os.makedirs (log_dir, 0751)
        except IOError, e:
            raise RuntimeError ("Could not create directory %s: %s" %
                                (log_dir, e))

    rootLogger = logging.getLogger ()
    rootLogger.setLevel (logging.DEBUG)
    log_fmt = logging.Formatter (FILE_FORMAT, DATEFMT)
    pid = os.getpid ()

    # add stream handler
    streamHandler = logging.StreamHandler (sys.stdout)
    streamHandler.setLevel (logging.DEBUG)
    streamHandler.setFormatter (log_fmt)
    rootLogger.addHandler (streamHandler)

    # add timedRotating handler
    today = utils.get_today ()
    filepath = "%s/%s" % (log_dir, today)
    if not os.path.exists (filepath):
        os.makedirs (filepath)
    for name, level in CATEGORY.items ():

        if namebyPID:
            filename = '%s/%s_%d.log' % (filepath, name, pid)
        else:
            filename = '%s/%s.log' % (filepath, name)

        fileHandler = DateRotaingFileHandler (filename = filename, when = 'D',
                                              interval = 1, base_dir = log_dir)
        fileHandler.setFormatter (log_fmt)
        fileHandler.setLevel (level)
        rootLogger.addHandler(fileHandler)

    def exception_log (typ, val, tb):
        s = traceback.format_exception (typ, val, tb)
        logging.error ("Uncaught exception:\n" + "".join (s))
        sys.__excepthook__ (typ, val, tb)

    sys.excepthook = exception_log


def test ():
    setup_logging ("test")
    import time
    while (True):
        logging.debug ("this is test (DEBUG)")
        logging.info ("this is test (INFO)")
        logging.warning ("this is test (WARNING)")
        logging.error ("this is test (ERROR)")
        time.sleep (1)

if __name__ == "__main__":
    test ()
