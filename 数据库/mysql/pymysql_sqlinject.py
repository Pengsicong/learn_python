#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: pymysql_sqlinject.py

Created by 彭思聪 on 2018/1/24 下午9:11.
Copyright © 2018年 彭思聪. All rights reserved.

"""

import pymysql

"""
所谓SQL注入，就是通过把SQL命令插入到Web表单提交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令。
具体来说，它是利用现有应用程序，将（恶意的）SQL命令注入到后台数据库引擎执行的能力，它可以通过在Web表单中输入（恶意）SQL语句得到一个
存在安全漏洞的网站上的数据库，而不是按照设计者意图去执行SQL语句。[1]  比如先前的很多影视网站泄露VIP会员密码大多就是通过WEB表单递交
查询字符暴出的，这类表单特别容易受到SQL注入式攻击．
"""
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='shop')

# 创建游标
cursor = conn.cursor()

# 推荐使用元组来传入数据
cursor.execute('select name, passwd from user where name=%s and passwd=%s', ('Tony', 123))

print(cursor.fetchone())

# 使用字符串拼接,会造成SQL注入的严重问题
sql = 'select name, passwd from user where name=%s and passwd=%s'

# 已知用户名的情况,使用mysql的注释符号 '--' 对数据库进行欺骗
cursor.execute(sql % ("'Tony'-- ", 66666))
print(cursor.fetchall())

# 未知用户名的情况, 使用 or 1=1 -- 使sql语句恒成立
cursor.execute(sql % ("'heh' or 1=1 --", 45611))

print(cursor.fetchall())

# 关闭游标
conn.close()
