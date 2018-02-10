#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: textwrap_shorten.py

Created by 彭思聪 on 2018/2/10 下午5:39.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print('Original:\n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('\nShortened:\n')
print(shortened_wrapped)
