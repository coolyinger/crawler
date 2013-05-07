import fcntl
import os
import sys

import log
import logging

APP_NAME = 'xlcrawler'

def pidfile_acquire (pidfile):
    fp = open (pidfile, "w")
    fcntl.lockf (fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    return fp

def pidfile_release (pidfile, pidfile_fd):
    fcntl.lockf (pidfile_fd, fcntl.LOCK_UN)
    os.unlink (pidfile)

def main ():

    log.setup_logging (APP_NAME, True)
    logging.info ("%s startup ..." % APP_NAME)

    pidfile_path = "%s.pid" % APP_NAME
    pidfile_fd = pidfile_acquire (pidfile_path)

    try:
        import time
        time.sleep (5)
    finally:
        pidfile_release (pidfile_path, pidfile_fd)
    logging.info ("%s finish ..." % APP_NAME)

if __name__ == "__main__":
    main ()
