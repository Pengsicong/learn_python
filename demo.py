#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: demo.py

Created by 彭思聪 on 2017/11/25 下午10:33.
Copyright © 2017年 彭思聪. All rights reserved.

"""

from funny.print_color_str import print_color_str
from string import ascii_letters

for _ in range(20):
    for letter in ascii_letters:
        print_color_str(letter, end=' ')
    print()
