#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 新式类与经典类.py

Created by 彭思聪 on 2018/5/8 上午9:31.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
Python中的类有经典类和新式类，新式类的属性比经典类的属性丰富。（ 如果类继object，那么该类是新式类 ）
"""


# 经典类
class Goods:

    @property
    def price(self):
        return 2333


obj = Goods()
result = obj.price
print(result)


#新式类
class Goods2(object):

    def __init__(self):
        self._price = 2333

    @property
    def price(self):
        print('@property')
        return self._price

    @price.setter
    def price(self, val):
        print('@setter')
        self._price = val

    @price.deleter
    def price(self):
        print('@deleter')
        self._price = 0


obj2 = Goods2()

result = obj2.price

obj2.price = 1

del obj2.price
