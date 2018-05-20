#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: redis简单.py

Created by 彭思聪 on 2018/5/20 下午9:29.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import redis


r = redis.Redis(host='127.0.0.1', port=6379)

r.set('hello', 'world')
data = r.get('hello')
keys = r.keys()

print(data, keys)
