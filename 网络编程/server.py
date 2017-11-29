#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server.py

Created by 彭思聪 on 2017/11/30 上午12:20.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from socket import socket


# 创建socket
sk = socket()

# 设置ip和port
adress = ('127.0.0.1', 8080)

# 为socket绑定ip和port
sk.bind(adress)

# 设置最大请求
sk.listen(3)

while True:
    # accept阻塞，直到有客户端连接过来
    conn, addr = sk.accept()
    print(conn)
    # data = input("server:")
    # conn.send(data.encode('utf8'))
    data = conn.recv(1024)
    print(data.decode('utf8'))

