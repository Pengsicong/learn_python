#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server.py

Created by 彭思聪 on 2017/11/30 上午12:20.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import socket, sys, os
from threading import Thread


class ClientThread(Thread):
    def __init__(self, client_conn, *, daemon=None):
        super(ClientThread, self).__init__(daemon=daemon)
        self.client_conn = client_conn
        self._closed = False

    def run(self):
        print("%s established" % self.client_conn)
        try:
            while True:
                recv = self.client_conn.recv(1024)
                if len(recv) > 0:
                    print('%s: %s' % (self.client_conn.getpeername(), recv))
                else:
                    break
        finally:
            print('%s closed' % self.client_conn)
            self.client_conn.close()
            self._closed = True

    def __del__(self):
        if not self._closed:
            print('%s closed again' % self.client_conn)
            self.client_conn.close()


def monitor(sk):
    """监听程序控制事件"""
    while True:
        command = input().lower()
        if command in ['quit', 'q']:
            # sys.exit()  #只能结束线程，无法结束主进程
            os._exit(0)   # 关闭主进程
        else:
            print(sk)


def main():
    # 创建socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置服务端套接字端口可以重用, 防止程序关闭后一段时间内端口TIME_WAIT
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 设置ip和port
    adress = ('', 8081)

    # 为socket绑定ip和port
    sk.bind(adress)

    # 设置最大请求
    sk.listen(30)

    # 创建socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置服务端套接字端口可以重用, 防止程序关闭后一段时间内端口一直占用
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 设置ip和port
    adress = ('', 8081)

    # 为socket绑定ip和port
    sk.bind(adress)

    # 设置最大请求
    sk.listen(30)

    monitor_thread = Thread(target=monitor, args=(sk,), daemon=True)
    monitor_thread.start()

    while True:
        # accept阻塞，直到有客户端连接过来
        conn, addr = sk.accept()
        ClientThread(conn, daemon=True).start()


if __name__ == '__main__':
    main()
