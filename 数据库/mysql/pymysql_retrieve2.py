#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: pymysql_retrieve2.py

Created by 彭思聪 on 2018/1/24 下午9:38.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import pymysql


# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='shop')

# 创建游标, 可以指定字典游标类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行查询操作,r为影响的条数, 且不需要commit操作
r = cursor.execute('select * from tb1 LIMIT 5 OFFSET 0')

# 通过游标的fetchall函数取出查询的所有结果
result = cursor.fetchall()
print(result)

# 游标回溯, 通过绝对位置移动到起点
cursor.scroll(0, mode='absolute')

# fetchmany取出任意个
many = cursor.fetchmany(3)
print(many)

# 游标回溯, 通过相对位置移动到上一个位置
cursor.scroll(-1, mode='relative')

# fetchone取出第一个
one = cursor.fetchone()
print(one)

# 关闭游标
conn.close()
