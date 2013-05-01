#!/bin/env python
#-*- coding:utf-8 -*-

from datetime import datetime


def get_today ():
    now = datetime.now ()
    return "%d-%d-%d" % (now.month, now.day, now.year)

