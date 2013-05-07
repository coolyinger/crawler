#!/bin/env python
#-*- coding:utf-8 -*-

import subprocess

class crawlerJob (object):
    
    def __init__ (self, arglist):
        self.market = arglist[0]
        self.links = arglist[1]
        self.category_general = arglist[2]
        self.rule = arglist[3]

    def start (self):
        #subproc = subprocess.Popen(
        #        "sudo nohup scrapy crawl umspider > "+log_path+item_name+".file", 
        #        stdin = subprocess.PIPE,shell = True)
        subproc = subprocess.Popen(
                "scrapy crawl test > nohup.out",
                stdin = subprocess.PIPE, shell = True)
        subproc.stdin.write (self.market + "\n")
        subproc.stdin.write (str (self.links) + "\n")
        subproc.stdin.write (self.category_general + "\n")
        subproc.stdin.write (self.rule)
        subproc.stdin.flush ()
        subproc.communicate ()


def test ():
    arglist = []
    arglist.append ("market")
    arglist.append (["link1", "link2", "link3"])
    arglist.append ("category")
    arglist.append ("rule")
    job = crawlerJob (arglist)
    job.start ()

if __name__ == "__main__":
    test ()
