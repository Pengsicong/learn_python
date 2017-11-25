#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: fibonacci.py

Created by 彭思聪 on 2017/11/24 下午9:21.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import time
from functools import wraps


def speed_test(func):

    @wraps(func)
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        duration = end - start
        duration *= 1000
        print('%s cost %0.2f ms' % (wrapper.__name__, duration))
    return wrapper


# 普通版本，
def fibonacci(maxnum):
    a = 0
    b = 1
    n = 0
    fibo = []
    while n < maxnum:
        fibo.append(a)
        a, b = b, a+b
        n += 1
    return fibo


# 递归版本，给定一个n输出fibonacci数列的第n个值
def fibonacci_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)


# 生成器版本
def fibonacci_generator(maxnum):
    a = 0
    b = 1
    n = 0
    while n < maxnum:
        yield a
        a, b = b, a + b
        n += 1


@speed_test
def normal_edit(num):
    print('普通版本：', end='')
    fibo_list = fibonacci(num)
    for item in fibo_list:
        print(item, end=' ')
    print()


@speed_test
def recursion_edit(num):
    print('递归版本：', end='')
    for i in range(num):
        print(fibonacci_recursion(i), end=' ')
    print()


@speed_test
def generator_edit(num):
    print('生成器版本：', end='')
    for item in fibonacci_generator(num):
        print(item, end=' ')
    print()


if __name__ == '__main__':
    n = 100
    normal_edit(n)
    # recursion_edit(n)
    generator_edit(n)
