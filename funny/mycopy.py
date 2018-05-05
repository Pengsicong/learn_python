#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: mycopy.py

Created by 彭思聪 on 2018/5/4 下午8:58.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import sys
import os


def mycopy(old_file, new_file):
    if not os.path.exists(old_file):
        print(old_file, ' 不存在!')
        return

    if new_file is None or os.path.isdir(new_file):
        new_file = old_file + '.backup'

    abs_old_file = os.path.join(os.path.dirname(__file__), old_file)
    abs_new_file = os.path.join(os.path.dirname(__file__), new_file)

    with open(abs_old_file, 'rb') as f_old:
        with open(abs_new_file, 'wb') as f_new:
            temp = f_old.read(1024)
            while temp != b'':
                f_new.write(temp)
                temp = f_old.read(1024)


if __name__ == '__main__':
    old_file = sys.argv[1]

    if len(sys.argv) < 3:
        new_file = None
    else:
        new_file = sys.argv[2]

    mycopy(old_file, new_file)
