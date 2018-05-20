#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: pymongo简单.py

Created by 彭思聪 on 2018/5/20 下午1:21.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import pymongo


user = 'admin'
passwd = '123456'
ip = 'localhost'
port = 27017
db = 'admin'

mongo_url = 'mongodb://{user}:{passwd}@{ip}:{port}/{db}'.format(user=user, passwd=passwd, ip=ip, port=port, db=db)

# 建立客户端, 连接MongoDB服务器
client = pymongo.MongoClient(mongo_url)

# 连接数据库
mongo_db = 'py3'
db = client[mongo_db]

# 获取集合
collection = 'stu'
stu = db[collection]

# 获取单条数据
# one_data = stu.find_one()
# one_data = stu.find().limit(1).next()

# 添加数据, 返回_id
# s1 = stu.insert({'name': 'aliex', 'age': 18})

# 更新数据, 返回删除信息
# u1 = stu.update_many({'name': 'aliex'}, {'$set': {'name': 'alex'}})

# 删除单条数据, 返回删除信息
# r1 = stu.delete_one({'name': 'alex'})
# r1 = stu.remove({'name': 'aliex'}, multi=False)

# 关闭连接
client.close()
