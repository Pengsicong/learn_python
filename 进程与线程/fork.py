#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: fork.py

Created by 彭思聪 on 2018/5/12 下午5:59.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import os
import time


def demo():
    # 主进程创建一个子进程, ret大于0为主进程, 等于0为子进程
    ret = os.fork()

    print(ret)

    # 子进程
    if ret == 0:
        while True:
            print('ret = %d---子进程---%d-of-%d---' % (ret, os.getpid(), os.getppid()))
            time.sleep(1)
    # 父进程
    else:
        while True:
            print('ret = %d---父进程---%d---' % (ret, os.getpid()))
            time.sleep(1)


def demo1():
    os.fork()
    os.fork()
    os.fork()

    print('---1---')


def fork_boom():
    """不要轻易尝试"""
    while True:
        os.fork()


if __name__ == '__main__':
    demo1()
