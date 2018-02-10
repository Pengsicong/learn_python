#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: textwrap_handing_indent.py

Created by 彭思聪 on 2018/2/10 下午5:37.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50,
                    ))
