#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: string_template.py

Created by 彭思聪 on 2018/2/10 下午4:09.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import string

values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable""")

print('TEMPLATE:', t.substitute(values))

print('#'*30)

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable"""

print('INTERPOLATION:', s % values)

print('#'*30)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable"""

print('FORMAT:', s.format(**values))

print('#'*30)

