#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: python中的编码探究.py

Created by 彭思聪 on 2017/12/6 下午12:55.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import sys

html = '你好 hi'

print(len(html))
print(html)
print(repr(html))
print([html])
print(type(html))

print('###################################')

if sys.version_info.major == 2:
    with open('/text', 'r') as f:
        text = f.read()

    print(text)
    print(repr(text))
    print(len(text))
    print(type(text))

    print('###################################')
    # python2 的str类型默认为bytes, 可以使用decode方法, 此时的text为Unicode
    text = text.decode('utf8')
    print(text)
    print(repr(text))
    print(len(text))
    print(type(text))

if sys.version_info.major == 3:
    # python3, 打开文件默认可能按照ascii编码的模式打开因此, 需要申明编码
    with open('./text', 'r', encoding='utf8') as f:
        text = f.read()

    # python3中str类型的默认为Unicode, 因此str.decode('utf8')会报错
    # text = text.decode('utf8')
    print(text)
    print(repr(text))
    print(len(text))
    print(type(text))


print('###################################')
# python会进行强类型转换, 统一为Unicode
s = 'hello' + u'world'
print(s)
print(repr(s))
print(type(s))

