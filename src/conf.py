#!/bin/env python
#-*- coding:utf-8 -*-

import os
import sys

working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../..')
sys.path.insert (0, working_dir)
from config import *
from mongoUtil import mongoUtil

if not IP:
    IP = "localhost"
if not PORT:
    PORT = 27017


def check_config ():
    if not mongoUtil.check_conn (IP, PORT):
        return False
    return True





if __name__ == "__main__":
    ret = check_config ()
    print ret
