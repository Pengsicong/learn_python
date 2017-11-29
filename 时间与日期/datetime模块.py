#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: datetime模块.py

Created by 彭思聪 on 2017/11/29 下午5:16.
Copyright © 2017年 彭思聪. All rights reserved.

"""

from datetime import timedelta

"""
datetime模块介绍
    提供多个关于时间与日期的类，用以处理一些简单或者复杂的操作
    
    timedelta类
        原型：class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        
        参数介绍：
            seconds：秒数
            
            microseconds：微秒
            
            milliseconds：毫秒
        
        通过total_seconds方法来获得一个timedelta对象的浮点型的秒数
    
    
"""

t = timedelta(days=1, milliseconds=1, microseconds=1)

# 86400.001001
print(t.total_seconds())
