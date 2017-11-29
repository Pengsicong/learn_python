#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: client.py

Created by 彭思聪 on 2017/11/30 上午12:26.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from socket import socket


# 创建socket
sk = socket()


# 设置ip和port
adress = ('127.0.0.1', 8080)

# 建立连接
sk.connect(adress)


# sk.send('hi'.encode('utf8'))
# 接受消息
# data = sk.recv(1024)
# print(data.decode('utf8'))

