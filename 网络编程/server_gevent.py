#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server_gevent.py

Created by 彭思聪 on 2018/5/16 下午7:56.
Copyright © 2018年 彭思聪. All rights reserved.

"""

from gevent import socket, monkey
import gevent
monkey.patch_all()


def handle_request(conn):
    while True:
        data = conn.recv(1024)
        client_addr = conn.getpeername()
        if not data:
            conn.close()
            print("%s 已经关闭" % str(client_addr))
            break
        else:
            print("%s>>>%s" % (client_addr, data))


def server(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(5)

    while True:
        client_conn, client_addr = s.accept()
        print('%s 已经连接' % str(client_addr))
        gevent.spawn(handle_request, client_conn)


if __name__ == '__main__':
    server(8080)
