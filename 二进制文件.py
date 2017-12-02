#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 二进制文件.py

Created by 彭思聪 on 2017/12/1 下午5:22.
Copyright © 2017年 彭思聪. All rights reserved.

"""  


with open('fail_requests', 'rb') as f:
    newdata = (f.read().split(b'\r\n\r\n', 1)[1:])
    with open('fail_request', 'wb') as f1:
        f1.write(newdata[0])