#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 列表漏删.py

Created by 彭思聪 on 2018/5/8 上午10:16.
Copyright © 2018年 彭思聪. All rights reserved.

"""  
a = [11, 22, 33, 44, 55, 66, 77]

# 由于在删除33的时候, 后面所有元素向前进位顾会漏删44
for i in a:
    if i == 33 or i == 44:
        a.remove(i)


print(a)


a = [11, 22, 33, 44, 55, 66, 77]

for i in a[::-1]:
    if i == 33 or i == 44:
        a.remove(i)


print(a)