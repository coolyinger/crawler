#!/bin/env python
#-*- coding:utf-8 -*-

import logging
import pymongo
from pymongo.connection import Connection

class mongoUtil (object):

    def __init__ (self, database, table, ip = "localhost", port = 27017):
        if isinstance (port, str):
            port = int(port)
        conn = Connection (host = ip, port = port)
        db = conn[database]
        self.form = db[table]

    def update_items (self, spec, val):
        self.form.update (spec, {"$set":val}, upsert = False, multi = True)

    def upsert_item (self, spec, val):
        self.form.update (spec, {"$set":val}, upsert = True)

    def find_and_modify (self, query = {}, update = None, sort = {},
                         fields = {}, upsert = False, new = False):
        return self.form.find_and_modify (query = query,
                                          update = update, sort = sort,
                                          fields = fields, upsert = upsert,
                                          new = new)

    def get_item_property (self, key, fields = None):
        if fields is None:
            return self.form.find(key)
        else:
            return self.form.find(key,fields=fields)

    @staticmethod
    def check_conn (ip = "localhost", port = 27017):
        try:
            port = int(port)
            conn = Connection (host = ip, port = port)
        except Exception as E:
            logging.error (E)
            return False
        else:
            conn.close ()
            return True

def test ():
    isOk = mongoUtil.check_conn ("localhost", "27017")
    print isOk

if __name__ == "__main__":
    test ()

