#!/usr/bin/env python3 
# encoding: utf-8
import sys

""" 

File Name: del方法.py

Created by 彭思聪 on 2018/5/5 上午10:08.
Copyright © 2018年 彭思聪. All rights reserved.

"""  


class Foo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name + ": I am dying")


foo = Foo('foo')

foo2 = Foo('foo2')
foo3 = foo2
print('foo2 引用计数:', sys.getrefcount(foo2))

del foo

print('end')
