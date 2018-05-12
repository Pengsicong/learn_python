#!/usr/bin/env python3
# encoding: utf-8

"""

File Name: 元类__metaclass__.py

Created by 彭思聪 on 2018/5/11 下午8:04.
Copyright © 2018年 彭思聪. All rights reserved.

"""

"""
元类决定了类是如何创建的
"""


def upper_attr(class_name, class_parents, class_attrs):

    new_attr = {}

    for name, value in class_attrs.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    return type(class_name, class_parents, new_attr)


# python2版本
# class Foo(object):
#     __metaclass__ = upper_attr
#
#     bar = 'hello'

# python3版本
class Foo(object, metaclass=upper_attr):
    bar = 'hello'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
