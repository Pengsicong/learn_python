#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多态.py

Created by 彭思聪 on 2018/5/5 上午11:18.
Copyright © 2018年 彭思聪. All rights reserved.

"""

"""
多态:
    定义一个调用类的方法的函数, 在定义的时候不知道调用谁的方法, 只有在执行的时候才会确定 
"""


class Base(object):

    def test(self):
        print('Base')


class Foo(Base):

    def test(self):
        print('FOO')


def test(cls):
    cls.test()


demo = Base()
demo1 = Foo()

test(demo)
test(demo1)
