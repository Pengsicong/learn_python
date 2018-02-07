#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server.py

Created by 彭思聪 on 2017/11/30 上午12:20.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import socket

# 创建socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 设置ip和port
adress = ('127.0.0.1', 8081)

# 为socket绑定ip和port
sk.bind(adress)

# 设置最大请求
sk.listen(30)


while True:

    # accept阻塞，直到有客户端连接过来
    conn, addr = sk.accept()
    print(conn)
    recv = conn.recv(1024)
    print(recv)

