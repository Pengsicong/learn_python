#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server_command.py

Created by 彭思聪 on 2017/12/1 上午12:44.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import socket
import subprocess

# 创建socket
sk = socket.socket()

# 设置ip和port
adress = ('127.0.0.1', 8080)

# 为socket绑定ip和port
sk.bind(adress)

# 设置最大请求
sk.listen(1)


while True:

    # accept阻塞，直到有客户端连接过来
    conn, addr = sk.accept()
    print(conn)

    while True:
        command = conn.recv(1024)
        if command:
            a = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            data = a.stdout.read()
            if not data:
                data = b''

            length = str(len(data))
            conn.sendall(length.encode())
            conn.sendall(data)

        else:
            conn.close()
            break
