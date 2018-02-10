#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: textwrap_indent.py

Created by 彭思聪 on 2018/2/10 下午5:28.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

from textwrap_example import sample_text
import textwrap


dedented_text = textwrap.dedent(sample_text)
wrapped_text = textwrap.fill(dedented_text, width=45)
wrapped_text += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped_text, '>')

print('Quoted block:\n')
print(final)