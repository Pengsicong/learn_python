#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: randomcode.py

Created by 彭思聪 on 2017/11/25 下午8:05.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import random
import string


def random_code(size=5):
    code = ''
    for _ in range(size):
        p = random.random()
        if p < 0.5:
            code += str(random.randint(0, 9))
        else:
            code += random.choice(string.ascii_letters)

    return code


if __name__ == '__main__':
    print(random_code(32))
