#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: __slots__.py

Created by 彭思聪 on 2018/5/10 上午10:55.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
__slots__的作用:
    限制实例能添加的属性
注意:
    1. __slots__只能限制实例对象的属性添加, 二不限制类对象
    2. 对继承的子类不起作用
"""


class Person(object):

    __slots__ = ['name', 'age']


class Man(Person):
    pass


tom = Person()
tom.name = 'tom'

try:
    tom.gender = 'male'
except AttributeError:
    print('添加失败!')

# __slots__只能限制实例对象的属性添加
Person.gender = 'male'
jack = Person()
print(jack.gender)


# 对继承的子类不起作用
alex = Man()
alex.gender = 'male'
