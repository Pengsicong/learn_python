#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 字符串format.py

Created by 彭思聪 on 2017/12/5 上午11:56.
Copyright © 2017年 彭思聪. All rights reserved.

"""  


li = ['Tony', 18]

"""
1. 使用位置参数
    位置参数不受顺序约束，且可以为{},只要format里有相对应的参数值即可,
    参数索引从0开，并可以指定索引
    传入位置参数列表可用*列表
"""

print('1. 使用位置参数\n')

print('my name is {}, age {}'.format('Tony', 18))

print('my name is {1}, age {0}'.format(18, 'Tony'))

print('my name is {1}, age {0}. my name is {1}, age {0}'.format(18, 'Tony'))

print('my name is {}, age {}'.format(*li))


"""
2、使用关键字参数
    关键字参数值要对得上.
    可用字典当关键字参数传入值，字典前加**即可
"""

di = {
    'name': 'Tony',
    'age': 18,
}

print('\n2、使用关键字参数\n')

print('my name is {name}, age {age}'.format(name='Tony', age=18))

print('my name is {name}, age {age}'.format(age=18, name='Tony'))

print('my name is {name}, age {age}'.format(**di))


"""
3、填充与格式化
    :[填充字符][对齐方式 <^>][宽度]
"""

print('\n3、填充与格式化\n')

print('左对齐:   {0:*<10}'.format(10))

print('中对齐:   {0:*^10}'.format(10))

print('右对齐:   {0:*>10}'.format(10))

"""
4、精度与进制
    :[宽度].[精度][进制]
    :[宽度].[进制]
"""

print('\n4、精度与进制\n')

print('浮点型:    {0:*>5.2f}'.format(1/3))
print('二进制:    {0:5b}'.format(10))
print('八进制:    {0:5o}'.format(10))
print('十六进制:  {0:>5x}'.format(10))


"""
5、使用索引
"""

print('\n5、使用索引\n')

print('my name is {0[0]}, age {0[1]}'.format(li))
