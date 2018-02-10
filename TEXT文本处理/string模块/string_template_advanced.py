#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: string_template_advanced.py

Created by 彭思聪 on 2018/2/10 下午4:34.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import string


# 继承string模块中的Template类, 修改终止符以及匹配模式
class MyTemplate(string.Template):
    delimiter = '#'
    idpattern = '[a-z]+_[a-z]+'


template_text = """
Delimiter   : ##
Replaced    : #with_underscored
Ingored     : #no underscored"""


values = {
    'with_underscored': 'replaced',
    'no underscored': 'not replaced'
}

t = MyTemplate(template_text)

print(t.safe_substitute(values))