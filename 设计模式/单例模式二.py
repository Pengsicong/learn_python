#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 单例模式二.py

Created by 彭思聪 on 2018/5/5 下午6:00.
Copyright © 2018年 彭思聪. All rights reserved.

"""  


class Foo:
    """I am doc"""

    _instance = None

    def __init__(self):
        print('----初始化----')

    def __new__(cls):
        if cls._instance is None:
            print('----新对象创建中----')
            cls._instance = object.__new__(cls)
        else:
            print('----对象已经存在----')

        return cls._instance

    def __del__(self):
        print('----已经删除----')


bar = Foo()
bar2 = Foo()

print(bar.__doc__)

print(bar.__str__())
print(bar2.__str__())

print(bar.__repr__())
print(bar2.__repr__())
