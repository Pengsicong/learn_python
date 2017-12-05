#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多线程.py

Created by 彭思聪 on 2017/12/4 下午5:59.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from functools import wraps
import threading
import time

num = 0


def show_perf(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s start at thread %s" % (wrapper.__name__, threading.current_thread()))
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("%s end after %s sec" % (wrapper.__name__, (end-start)))
    return wrapper


@show_perf
def foo(x):
    global num
    # IO bounch
    for i in range(50000000):
        num += 1

    # CPU bounch
    time.sleep(x)


@show_perf
def bar(x):
    global num
    # IO bounch
    for i in range(50000000):
        num += 1

    # CPU bounch
    time.sleep(x)


@show_perf
def main():
    t1 = threading.Thread(target=foo, args=(1,))
    t2 = threading.Thread(target=bar, args=(2,))

    # t1.setDaemon(True)
    # t2.setDaemon(True)

    t1.start()
    t2.start()

    print('Thread active count: %s (in front of join)' % threading.active_count())

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
    print('Thread active count: %s (after join)' % threading.active_count())
    print('num = %s' % num)
