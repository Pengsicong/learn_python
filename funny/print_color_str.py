#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: print_color_str.py

Created by 彭思聪 on 2017/11/27 下午12:45.
Copyright © 2017年 彭思聪. All rights reserved.

"""  


import re
import random


"""
-------------------------------------------
-------------------------------------------
字体色     |       背景色     |      颜色描述
-------------------------------------------
30        |        40       |       黑色
31        |        41       |       红色
32        |        42       |       绿色
33        |        43       |       黃色
34        |        44       |       蓝色
35        |        45       |       紫红色
36        |        46       |       青蓝色
37        |        47       |       白色
-------------------------------------------
-------------------------------
显示方式     |      效果
-------------------------------
0           |     终端默认设置
1           |     高亮显示
4           |     使用下划线
5           |     闪烁
7           |     反白显示
8           |     不可见
-------------------------------
print('This is a \033[1;35m test \033[0m!')
print('This is a \033[1;32;43m test \033[0m!')
print('\033[1;33;44mThis is a test !\033[0m')
"""


def get_color_str(txt, display=0):

    color_pre = 0
    for word in re.finditer(r'\b\w+\b', txt):
        color = random.randint(30, 37)

        # 相邻颜色不重复
        while color == color_pre:
            color = random.randint(30, 37)

        color_pre = color

        new_word = '\033[%s;%sm' % (display, color) + word.group() + '\033[0m'

        txt = re.sub(r'\b%s\b' % word.group(), new_word, txt)

    return txt


def print_color_str(txt, display=0):
    txt = get_color_str(txt, display)
    print(txt)


if __name__ == '__main__':
    s = "These six words are very happy!"
    print_color_str(s, 1)
