#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: yield示例.py

Created by 彭思聪 on 2018/5/16 下午7:12.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import time


def print_a():
    while True:
        print('----A----')
        yield
        time.sleep(0.5)


def print_b(c):
    while True:
        print('----B----')
        next(c)
        time.sleep(0.5)


if __name__ == '__main__':
    temp = print_a()
    print_b(temp)
