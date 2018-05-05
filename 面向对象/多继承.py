#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多继承.py

Created by 彭思聪 on 2018/5/5 上午10:47.
Copyright © 2018年 彭思聪. All rights reserved.

"""  


class Base(object):

    def test(self):
        print('Base')


class A(Base):

    def test(self):
        print('A')


class B(Base):

    def test(self):
        print('B')


class C(A, B):

    def test(self):
        print('C')


c = C()

c.test()

# 类的方法与属性的搜索顺序
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
print(C.__mro__)
