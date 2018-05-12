n#!/usr/bin/env python
# encoding: utf-8  

""" 

File Name: 闭包.py

Created by 彭思聪 on 2017/11/24 下午11:15.
Copyright © 2017年 彭思聪. All rights reserved.

"""

"""
闭包                          
    定义：如果在一个内部函数里，对在 外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure).
    
开放封闭原则:
    开放: 对拓展开放
    封闭: 对已经实现功能的代码块
"""


def outer(x):

    def inner():
        i = 250
        i = i + x
        print(i)
        return i
    return inner


f = outer(250)     # 唯一调用inner的方式, 且inner函数为闭包（closure）
i = f()         # f就是inner
print(i)

# inner()   # 直接调用报错，inner为outer的内部函数，和x不能直接调用同理




