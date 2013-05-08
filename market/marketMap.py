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
    if market == "AnzhItem":
        config = AnzhItemConfig
    elif market == "HiApkItem":
        config = HiApkItemConfig
    elif market == "AppchItem":
        config = AppchItemConfig
    elif market == "NduoaItem":
        config = NDuoaItemConfig
    elif market == "ITunesItem":
        config = ITunesItemConfig
    elif market == "WanDouJiaItem":
        config = WanDouJiaItemConfig
    elif market == "AndrmarketItem":
        config = AndrmarketItemConfig
    return config
