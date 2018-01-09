#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 初窥greenlet.py

Created by 彭思聪 on 2017/12/6 下午10:19.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from gevent.greenlet import greenlet

"""
什么是greenlet
    greenlet是一个用C实现的协程模块，相比与python自带的yield，
    它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
"""


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()

