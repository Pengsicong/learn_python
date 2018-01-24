#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: pymysql_create2.py

Created by 彭思聪 on 2018/1/24 下午7:13.
Copyright © 2018年 彭思聪. All rights reserved.

"""  
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='shop')

# 创建游标
cursor = conn.cursor()

# 带插入数据
valuses = (
    (100,),
    (101,),
    (102,),
    (103,),
    (104,),
)

# 批量插入, 注意这里不能使用 % 的字符串拼接, 防止SQL注入
cursor.executemany('insert into tb1(num) values (%s)', valuses)

# 向数据库服务器提交SQL语句
conn.commit()

# 关闭游标
conn.close()
