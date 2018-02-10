#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: string_constants.py

Created by 彭思聪 on 2018/2/10 下午4:55.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import inspect
import string


def is_str(s):
    if isinstance(s, str):
        return True
    else:
        return False


for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s:%r\n' % (name, value))
