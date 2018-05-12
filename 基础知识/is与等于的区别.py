#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: is与等于的区别.py

Created by 彭思聪 on 2018/5/8 下午2:55.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
is 是比较两个引用是否指向了同一个对象(引用比较)
== 是比较两个对象是否相等"""

a = [11, 22, 33]
b = [11, 22, 33]

print(a == b)
print(a is b)
print('id of a: %s' % id(a))
print('id of b: %s' % id(b))
