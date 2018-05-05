#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 异常处理.py

Created by 彭思聪 on 2017/11/28 下午4:15.
Copyright © 2017年 彭思聪. All rights reserved.

"""  


"""
try:
    # 代码块
    i = input('input some number')
    i = int(i)
except Exception as e:
    # e是Exception的对象，对象中封装了错误信息，且Exception是其他错误类的父类
    i = 'wrong'
    print(e)
else:
    # 如果没有出错则执行
    print('else')
finally:
    # 不管有没有出错都执行
    print('finally')

print(i)
"""


"""
主动触发异常raise
     raise Exception('some messages!')
     什么时候用？
        当try的代码中执行某些函数或者方法，但是这些函数或者方法一定会返回某个值，我们可以通过返回的这个值来判断是否需要主动触发异常
        比如连接数据库函数，成功返回True，失败返回False，当返回False时主动触发异常
"""


"""
自定义异常
    class MyError(Exception):
        
        def __init__(self, msg):
            self.msg = msg
        
        def __str__(self):
            return self.msg
            
try:
    raise MyError('I am wrong!')
exception MyError as e:
    print(e)        # 对象的__str__方法， 获取返回值
"""


"""
断言assert
    满足条件，继续执行
    不满足条件，触发AssertionError异常
    
    什么时候用？
        可以在不用try-exception语句的情况下，利用条件判断的语法来判读是否触发异常
        用于强制用户服从，不服从就报错，可捕获，当时一般都用在没有try-exception的情况，所以不捕获
"""

