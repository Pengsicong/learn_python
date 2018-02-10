#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: textwrap_fill.py

Created by 彭思聪 on 2018/2/10 下午5:10.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import textwrap
from textwrap_example import sample_text


print(textwrap.fill(sample_text, width=70))