#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: demo.py

Created by 彭思聪 on 2017/11/30 下午4:01.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import subprocess

a = subprocess.Popen(b'l', shell=True, stdout=subprocess.PIPE)
# print(a.stdout.read().decode())
# print(a.stderr.read(), 'hh')
result =  a.stdout.read()
if not result:
    print(result)
else:
    print('hi')