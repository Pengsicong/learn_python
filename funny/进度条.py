#!/usr/bin/env python3
# encoding: utf-8  

""" 

File Name: 进度条.py

Created by 彭思聪 on 2018/5/13 下午5:25.
Copyright © 2018年 彭思聪. All rights reserved.

"""  
import time

for i in range(1, 101):
    current = '*' * i
    print('\r%s' % current, end='')
    time.sleep(0.1)
