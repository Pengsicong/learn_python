#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server.py

Created by 彭思聪 on 2017/11/30 上午12:20.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import socket

# 创建socket
sk = socket.socket()

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

    client = socket.socket()
    client.connect(('www.baidu.com', 443))

    client.send(recv)
    recv_web = client.recv(8196)
    print(recv_web)

    conn.send(recv_web)
    recv = conn.recv(8196)

    client.send(recv)
    while True:
        data = client.recv(8192)
        if data:
            print(data)
            conn.send(data)
        else:
            client.close()
            break
            # data = input('>>>').encode()
            # conn.send(data)
            # conn.close()
            # break

        

from datetime import datetime

