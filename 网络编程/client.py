#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: client.py

Created by 彭思聪 on 2017/12/1 上午9:32.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from socket import socket

#
# # 创建socket
# sk = socket()
#
#
# # 设置ip和port
# adress = ('127.0.0.1', 8080)
#
# # 建立连接
# sk.connect(adress)
#
# buffer_size = 1024
#
# while True:
#     data = input('>>>').encode()
#     if data:
#         sk.send(data)
#         while True:
#             recv = sk.recv(buffer_size)
#             if recv:
#                 print(recv)
#             else:
#                 break
#     else:
#         sk.close()
#         break
#
# f = open('request_baidu_https', 'rb')
# sk = socket()
# sk.connect(('115.239.211.112', 443))
#
# while True:
#     data = sk.recv(8196)
#     if data:
#         print(data)
#     else:
#         sk.close()
#         break
# f.close()
str
