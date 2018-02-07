#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server.py

Created by 彭思聪 on 2018/2/5 上午12:42.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sk.bind(('localhost', 8080))

sk.listen(300)

while True:

    conn, addr = sk.accept()

    print(conn)

    recv_data = conn.recv(1024)

    conn.send("HTTP/1.1 200 OK\r\n\r\n".encode('utf8'))

    with open('基本标签.html', 'r', encoding='utf8') as f:

        data = f.read()

    conn.sendall(data.encode('utf8'))

    conn.close()




