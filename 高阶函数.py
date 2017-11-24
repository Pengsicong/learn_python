#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: 高阶函数.py

Created by 彭思聪 on 2017/11/24 下午8:52.
Copyright © 2017年 彭思聪. All rights reserved.

"""  


def func(x):
    return x * x


# 高阶函数，调用函数的函数，f做为参数名传入函数。
def foo(a, b, f):
    return f(a) + f(b)


if __name__ == '__main__':
    result = foo(2, 3, func)
    print(result)
