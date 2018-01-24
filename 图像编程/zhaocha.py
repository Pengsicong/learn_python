#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: zhaocha.py

Created by 彭思聪 on 2018/1/15 下午12:49.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

from enum import Enum


class Week(Enum):
    Sunday = 0
    Monday = 1


print(Week(1))