#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: minimize.py

Created by 彭思聪 on 2017/12/6 下午8:24.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from functools import reduce, wraps
from random import shuffle
from time import process_time


def show_times(times):

    def show_fast(func):

        # @wraps(func)
        def wrapper(*args):
            start = process_time()

            for _ in range(times):
                func(*args)

            end = process_time()

            print("%s run %s times cost %s sec" % (func.__name__, times, (end-start)))

        return wrapper

    return show_fast


def minimize_coroutine():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


def minimize_reduce(x, y):
    return min(x, y)


@show_times(100)
def test_reduce(l):
    return reduce(minimize_reduce, l)


@show_times(100)
def test_coroutine(l):
    it = minimize_coroutine()
    next(it)
    return list(map(it.send, l))[-1]


@show_times(1000)
def test_custom(l):
    minimum = l[0]

    for item in l:
        if item < minimum:
            minimum = item

    return minimum


if __name__ == '__main__':

    li = list(range(10000))
    shuffle(li)

    test_reduce(li)
    test_coroutine(li)
    test_custom(li)
