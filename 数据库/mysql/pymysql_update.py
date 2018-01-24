#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: pymysql_update.py

Created by 彭思聪 on 2018/1/24 下午7:42.
Copyright © 2018年 彭思聪. All rights reserved.

"""
import pymysql


# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='shop')

# 创建游标
cursor = conn.cursor()

# 将tb1表中num值大于100的都改为100
cursor.execute('update tb1 set num=100 WHERE num > 100')

# 向数据库服务器提交SQL语句
conn.commit()

# 关闭游标
conn.close()
