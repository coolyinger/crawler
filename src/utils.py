#!/bin/env python
#-*- coding:utf-8 -*-

from datetime import datetime
import uuid
import socket


def get_today ():
    now = datetime.now ()
    return "%d-%d-%d" % (now.month, now.day, now.year)


def get_mac_address ():
    node = uuid.getnode ()
    mac = uuid.UUID (int = node).hex[-12:]
    return mac

def get_ip_address ():
    s =  socket.socket (socket.AF_INET,  socket.SOCK_DGRAM)
    s.connect (("www.baidu.com", 80))
    res = s.getsockname ()[0]
    s.close ()
    return res


def test ():
    print get_mac_address ()
    print get_ip_address ()

if __name__ == "__main__":
    test ()
