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


def show_perf(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s start at thread %s" % (wrapper.__name__, threading.current_thread()))
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("%s end after %s sec" % (wrapper.__name__, (end-start)))
        return result
    return wrapper


@show_perf
def foo(x):
    global num
    # CPU bounch
    for i in range(1000):
        for j in range(1000):
            num += 1

    # IP bounch
    time.sleep(x)


@show_perf
def bar(x):
    global num
    # CPU bounch
    for i in range(1000):
        for j in range(1000):
            num += 1

    # IO bounch
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

    # join 方法表示主线程等待子线程执行完毕,才继续执行下一步
    t1.join()
    t2.join()
    print('Thread active count: %s (after join)' % threading.active_count())
    print('num = %s' % num)


if __name__ == '__main__':
    num = 0
    main()
