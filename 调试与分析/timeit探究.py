#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: timeit探究.py

Created by 彭思聪 on 2017/11/29 下午2:24.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import timeit
import time

"""
timeit模块
    简介
        Measure execution time of small code snippets
        测试代码块的执行时间的计时器
    python接口
        含有timeit、repeat、default_timer这三个内置函数，以及一个Timeit类
        
        timeit
            原型：timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
            
            stmt
                需要测试的代码块或者函数入口
                
            setup
                在测试开始时提前所运行的代码，默认为pass
                
            timer
                默认为time.perf_count用来计算代码块运行时间（包括sleep)
            
            number
                代码块运行的次数，默认为一百万
            
            globals
                是否引入当前文件的所有函数
                
            
                        
"""


def f(x):
    return x**2


def g(x):
    return x**4


def h(x):
    return x**8


def bar():
    time.sleep(0.1)


if __name__ == "__main__":
    for func in [f, g, h]:
        print(timeit.timeit('func(30)', number=10000, globals=globals()))
    print(timeit.timeit(stmt='bar()', timer=time.perf_counter, number=10, setup="from __main__ import bar"))
    print(timeit.timeit('bar()', timer=time.process_time, number=10, setup="from __main__ import bar"))



