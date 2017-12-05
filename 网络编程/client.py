#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: client.py

Created by 彭思聪 on 2017/12/1 上午9:32.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

from socket import socket


# 创建socket
sk = socket()


# 设置ip和port
adress = ('127.0.0.1', 8088)

# 建立连接
sk.connect(adress)

buffer_size = 1024

while True:
    data = input('>>>').encode('utf8')
    if data:
        sk.send(data)

        recv = sk.recv(buffer_size)
        print(recv.decode('utf8'))

    else:
        print('end')
        sk.close()
        break


