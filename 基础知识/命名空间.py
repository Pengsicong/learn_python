#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 命名空间.py

Created by 彭思聪 on 2018/5/10 上午9:46.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
什么是命名空间:
    对一个对象起作用的范围

globals, locals:
    
    globals()查看当前命名空间的所有全局变量
    locals()查看所有的局部变量

LEGB:
    python使用LEGB的顺序来查找一个符号对应的对象
    locals -> enclosing function -> globals -> builtins
    
    locals, 当前所在命名空间(如函数, 模块), 函数的参数也属于命名空间内的变量
    enclosing, 外部嵌套函数的命名空间(闭包中常见)
    globals: 全局变量, 函数定义所在模块的命名空间
    builtins: python内置对象
"""


def test():
    a = 100
    b = 200
    print(locals())


print(globals())
test()


