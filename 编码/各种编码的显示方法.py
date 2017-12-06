#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 各种编码的显示方法.py

Created by 彭思聪 on 2017/12/6 下午1:07.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import json


def show_unicode(s):
    return json.dumps(s)


def show_utf8(s):
    return bytes(s, 'utf8')


def show_gbk(s):
    return bytes(s, 'gbk')


if __name__ == '__main__':
    s = '彭思聪'

    print(show_unicode(s))
    print(show_utf8(s))
    print(show_gbk(s))
