#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 关于字符串拼接那些事.py

Created by 彭思聪 on 2017/11/28 下午7:28.
Copyright © 2017年 彭思聪. All rights reserved.

"""


from test import TestFunction

strlist = ['test' for _ in range(1)]


def test_join():
    return ''.join(strlist)


def test_puls():
    result = ''
    for s in strlist:
        result += s
    return result


def test_puls_enumerate():
    result = ''
    for i, v in enumerate(strlist):
        result += v
    return result


if __name__ == '__main__':
    test_times = 100
    for func in [test_join, test_puls, test_puls_enumerate]:

        obj = TestFunction(func)
        obj.test(test_times)
        obj.show()


