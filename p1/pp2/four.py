#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: four.py

Created by 彭思聪 on 2017/11/27 上午8:49.
Copyright © 2017年 彭思聪. All rights reserved.

"""  
import sys
import os
sys.path.insert(1, os.path.abspath('..'))
print(sys.path)


from pp1 import second
print(__file__, __name__)
print('\033[1;32mhello\033[0m \033[1;35mworld\033[0m')
print('This is a \033[1;35m test \033[0m!')