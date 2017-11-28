#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 关于字符串拼接那些事.py

Created by 彭思聪 on 2017/11/28 下午7:28.
Copyright © 2017年 彭思聪. All rights reserved.

"""


from test_decorator import process_test

strlist = ['test' for _ in range(1000000)]


@process_test
def test_join():
    return ''.join(strlist)


@process_test
def test_puls():
    result = ''
    for s in strlist:
        result += s
    return result


@process_test
def test_puls_enumerate():
    result = ''
    for i, v in enumerate(strlist):
        result += v
    return result


if __name__ == '__main__':

    test_join()
    test_puls()
    test_puls_enumerate()
