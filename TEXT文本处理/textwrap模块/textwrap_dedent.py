#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: textwrap_dedent.py

Created by 彭思聪 on 2018/2/10 下午5:16.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

from textwrap_example import sample_text
import textwrap


dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)