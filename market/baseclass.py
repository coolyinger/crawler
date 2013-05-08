#!/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
working_dir = os.path.abspath(os.path.realpath(__file__)+ '/../../')
sys.path.append (working_dir)

from core.items import CoreItem

class baseclass (object):

    def __init__ (self):
        pass

    @classmethod
    def parse (cls, reponse):
        item = CoreItem
        return item
