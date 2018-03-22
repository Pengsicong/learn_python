#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: wsgiref模块实例.py

Created by 彭思聪 on 2018/3/21 下午8:27.
Copyright © 2018年 彭思聪. All rights reserved.

"""

from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(environ)
    start_response('200 ok', [('Content-Type', 'text/html')])
    return [b'<h1>Hello Web!<h1>']


httpd = make_server('', 8080, application)

httpd.serve_forever()

