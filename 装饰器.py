#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: 装饰器.py

Created by 彭思聪 on 2017/11/24 下午11:51.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import time


def show_time(f):

    def inner():
        start = time.time()
        f()
        end = time.time()
        duration = end - start
        print("cost time : %0.2f sec" % duration)

    return inner


def show_time2(f):

    def inner(*args):
        start = time.time()
        s = f(*args)
        end = time.time()
        duration = end - start
        print("cost time : %0.2f sec" % duration)
        return s

    return inner


def logger(Flag):
    def show_time3(f):

        def inner(*args):
            start = time.time()
            s = f(*args)
            end = time.time()
            duration = end - start
            print("cost time : %0.2f sec" % duration)

            if Flag == True:
                print('logging......')
            return s

        return inner

    return show_time3


# 不带参数函数的装饰器
@show_time         #等价于 func = show_time(func)  # func 保存的是show_time函数的闭包inner
def func():
    print('processing....')
    time.sleep(1)


# 带参数函数的装饰器
@show_time2        #等价于 add = show_time2(add)   # 注意这里show_time2是函数名，且add函数带参数一起传入装饰器
def add(*args):
    s = 0
    for i in args:
        s += i
    time.sleep(1)
    return s


# 装饰器带参数的类型
@logger(True)      # 注意这里的logger带上了括号，所以首先运行logger函数，返回一个装饰器show_time3
def multiply(*args):
    s = 1
    for i in args:
        s *= i
    time.sleep(1)
    return s


# func()                  # 执行的是闭包inner函数
# t = add(1, 2, 3)
t = multiply(1, 2, 3)
print(t)

