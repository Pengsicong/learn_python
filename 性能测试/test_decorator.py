#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: test_decorator.py

Created by 彭思聪 on 2017/11/28 下午7:39.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from time import perf_counter, process_time
from functools import wraps


# 计算程序运行的cpu时间的装饰器
def process_test(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = process_time()
        result = func(*args, **kwargs)
        duration = process_time() - start_time
        print('%s cost %0.3f ms' % (wrapper.__name__, duration * 1000))
        return result

    return wrapper


# 计算程序运行时间(包括sleep时间)的装饰器
def perf_test(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - start_time
        print('%s cost %0.3f ms' % (wrapper.__name__, duration * 1000))
        return result

    return wrapper
