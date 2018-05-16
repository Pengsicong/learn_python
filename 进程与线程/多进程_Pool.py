#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多进程_Pool.py

Created by 彭思聪 on 2017/12/6 下午5:03.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from multiprocessing import Pool
import time

"""
进程池Pool
    进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，
    如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中有两个方法：
    1. apply(func[, args[, kwds]])是阻塞的
       父进程阻塞直到进程池中的进程执行完毕 
        
    2. apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞
        维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
"""


def func(my_msg):
    print("my_msg:", my_msg)
    time.sleep(3)
    print("end", my_msg)


if __name__ == "__main__":
    pool = Pool(processes=3)
    for i in range(4):
        msg = "hello %d" % i
        # pool.apply(func, (msg, ))   # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.apply_async(func, (msg, ))   # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("Sub-process(es) done.")
