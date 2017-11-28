#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: test.py.py

Created by 彭思聪 on 2017/11/28 下午8:14.
Copyright © 2017年 彭思聪. All rights reserved.

"""

from time import perf_counter, process_time
from sys import maxsize


# 计算程序运行的cpu时间的装饰器
def process_test(func):

    def wrapper(*args, **kwargs):
        start_time = process_time()
        func(*args, **kwargs)
        duration = process_time() - start_time
        return duration

    return wrapper


# 计算程序运行时间(包括sleep时间)的装饰器
def perf_test(func):

    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        duration = perf_counter() - start_time
        return duration

    return wrapper


# 测试类
class TestFunction:
    def __init__(self, func, args=(), kwargs={}):
        self.func = func
        self. args = args
        self.kwargs = kwargs
        self.funcname = func.__name__
        self.average_time = 0
        self.max_time = 0
        self.min_time = maxsize

    # 给函数设置一个process_test装饰器，并返回该函数
    def get_process(self):
        test_process_func = process_test(self.func)
        return test_process_func

    # 给函数设置一个perf_test装饰器，并返回该函数
    def get_perf(self):
        test_perf_func = perf_test(self.func)
        return test_perf_func

    # 测试对象的当前函数，通过test_times设置测试次数，test_type设置测试类型
    def test(self, test_times=1, test_type='process'):
        if test_type == 'process':
            test_process_func = self.get_process()
        else:
            test_process_func = self.get_perf()

        total_time = 0
        for _ in range(test_times):
            current_time = test_process_func(*self.args, **self.kwargs)

            if current_time < self.min_time:
                self.min_time = current_time

            if current_time > self.max_time:
                self.max_time = current_time

            total_time += current_time

        self.average_time = total_time / test_times

    # 打印测试后的结果，通过formate参数来设置单位最优化
    def show(self, formate=True):
        if self.average_time == 0:
            self.test()

        if formate:
            if self.average_time > 1:
                unit = 's'
                multiple = 1

            elif self.average_time > 1e-3:
                unit = 'ms'
                multiple = 1e3

            elif self.average_time > 1e-6:
                unit = 'us'
                multiple = 1e6

            else:
                unit = 'ns'
                multiple = 1e9


        else:
            unit = 's'
            multiple = 1

        if self.max_time == self.min_time:
            print("%s cost %0.3f %s" % (self.funcname, self.average_time * multiple, unit))

        else:
            print('%s cost average: %0.3f %s max: %0.3f %s min: %0.3f %s' % (self.funcname,
                                                                             self.average_time * multiple, unit,
                                                                             self.max_time * multiple, unit,
                                                                             self.min_time * multiple, unit))

