#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: string_template_defaultepattern.py

Created by 彭思聪 on 2018/2/10 下午4:44.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import string

t = string.Template('$var')

print(t.pattern.pattern)
