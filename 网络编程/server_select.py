#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server_select.py

Created by 彭思聪 on 2018/1/10 下午4:16.
Copyright © 2018年 彭思聪. All rights reserved.

"""


from select import select
import socket


"""
IO多路复用:
    可以在不使用多线程与多进程的情况下, 对于多个socket套接字进行处理

方式:
    select(轮询检测): 跨平台, 但是单个进程能够监听的文件描述符的数量存在限制, 在liunx系统下, 32位为1024个, 64位为2048个
    poll(轮询检测): 和select一样, 但是没有数量限制
    epoll(事件通知): 同样没有数量限制 
"""

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_addr = ('', 8080)
sk.bind(server_addr)

sk.listen(3)
mainsocks, readsocks, writesocks = [], [], []
mainsocks.append(sk)
readsocks.append(sk)

print('select-server loop starting')

while True:
    # read表示是否可以收数据, write表示是否可以发数据, exception表示是否产生异常
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    print('readables: ', readables)
    print('readsocks ', readsocks)
    print('#'*50)

    for sockobj in readables:
        # 用来接收新客户端连接
        if sockobj in mainsocks:
            new_client_conn, new_client_addr = sockobj.accept()
            print(new_client_addr, '已经连接!')
            readsocks.append(new_client_conn)

        # 用来处理客户端连接
        else:
            data = sockobj.recv(1024).decode()
            client_addr = sockobj.getpeername()

            if len(data) > 0:
                print('got', data, 'from', client_addr)
                reply = 'Echo=>%s' % data
                sockobj.send(reply.encode('utf8'))
            else:
                print(client_addr, '已经关闭!')
                sockobj.close()
                readsocks.remove(sockobj)

    print('#'*50)
