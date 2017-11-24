#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: fibonacci.py

Created by 彭思聪 on 2017/11/24 下午9:21.
Copyright © 2017年 彭思聪. All rights reserved.

"""  


def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


for i in range(10):
    print(i, ' : ', fibonacci(i))
