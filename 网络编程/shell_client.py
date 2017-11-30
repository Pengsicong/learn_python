#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: shell_client.py

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

buffer_size = 1024

while True:
    data = input('>>>').encode()
    if data:
        sk.send(data)

        length = sk.recv(24)

        try:
            length = int(length)
        except Exception as e:
            print(e)
            print(length)
            length = 1

        data = b''

        for _ in range((length + buffer_size - 1) // buffer_size):

            recv = sk.recv(buffer_size)
            data += recv

        print(data.decode('utf8'))


    else:
        sk.close()
        break

