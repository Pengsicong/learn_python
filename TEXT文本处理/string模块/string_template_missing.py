#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: string_template_missing.py

Created by 彭思聪 on 2018/2/10 下午4:23.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import string

values = {'var': 'foo'}

t = string.Template("""$var is here but $missing is not provided.""")

try:
    print('TEMPLATE:', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitute():', t.safe_substitute(values))
