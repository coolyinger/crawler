#!/bin/env python
#-*- coding:utf-8 -*-

from AnzhItem import AnzhItemConfig
from HiApkItem import HiApkItemConfig
from AppchItem import AppchItemConfig
from NDuoaItem import NDuoaItemConfig
from ITunesItem import ITunesItemConfig
from WanDouJiaItem import WanDouJiaItemConfig
from AndrmarketItem import AndrmarketItemConfig


def get_market_config (market):
    config = None
    config_str = market + "Config"
    try:
        config = eval (config_str)
    except NameError:
        config = None
    return config ()

