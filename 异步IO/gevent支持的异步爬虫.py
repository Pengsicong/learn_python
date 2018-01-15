#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: gevent支持的异步爬虫.py

Created by 彭思聪 on 2018/1/9 下午10:53.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

from gevent import monkey
import gevent
import requests


def gethtml(url):
    try:
        print(url)
        resp = requests.get(url)
        print(resp.status_code)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    monkey.patch_all()
    gevent.joinall([
        gevent.spawn(gethtml, 'http://www.gevent.org/'),
        gevent.spawn(gethtml, 'http://www.gevent.org/'),
        gevent.spawn(gethtml, 'http://www.gevent.org/'),
        gevent.spawn(gethtml, 'http://www.gevent.org/'),
        gevent.spawn(gethtml, 'http://www.gevent.org/'),
        gevent.spawn(gethtml, 'http://www.gevent.org/'),
    ])
