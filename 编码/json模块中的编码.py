#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: json模块中的编码.py

Created by 彭思聪 on 2017/12/6 下午2:00.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import json


s = '你好 hi'

# 按照ascii编码写入文件
with open('json_ascii.json', 'w', encoding='ascii') as f:
    json.dump(s, f, ensure_ascii=True)

# 按照utf8编码写入文件
with open('json_utf8.json', 'w', encoding='utf8') as f:
    json.dump(s, f, ensure_ascii=False)
