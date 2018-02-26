#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server_select.py

Created by 彭思聪 on 2018/1/10 下午4:16.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

from select import select
import socket
import time
import sys


def now():
    return time.ctime(time.time())


ip = '127.0.0.1'

port = 8080

if len(sys.argv) == 3:
    ip, port = sys.argv[1:]

addr = (ip, port)

mainsocks, readsocks, writesocks = [], [], []

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk.bind(addr)

sk.listen(3)

mainsocks.append(sk)
readsocks.append(sk)

print('select-server loop starting')

while True:
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        # 用来接收新客户端连接
        if sockobj in mainsocks:
            conn, addr = sockobj.accept()
            print('Connect:', addr, id(conn))
            readsocks.append(conn)
        # 用来处理客户端连接
        else:
            data = sockobj.recv(1024).decode()
            print('got', data, 'on', id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                reply = 'Echo=>%s at %s' % (data, now())
                sockobj.send(reply.encode())
