#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: demo.py

Created by 彭思聪 on 2017/11/25 下午10:33.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import configparser

"""
[DEFAULT]
timeout = 10
isdireact = no
theads = 4

[PROXY]
port = 
addr = 
"""

# 获取一个文件配置的句柄
config = configparser.ConfigParser()

# 添加内容
config['DEFAULT'] = {'Theads': '4',
                     'TimeOut': '10',
                     'IsDireact': 'no', }

config['PROXY'] = {'addr': '',
                   'port': '', }

with open('settings', 'w') as configfile:
    config.write(configfile)
