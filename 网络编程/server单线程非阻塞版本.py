#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: server单线程非阻塞版本.py

Created by 彭思聪 on 2018/5/16 下午2:28.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import socket


def main():
    # 创建socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 设置ip和port
    adress = ('', 1234)
    sk.bind(adress)

    # 让accept非阻塞
    sk.setblocking(False)

    sk.listen(30)

    # 用来保存所有已经连接的客户端的信息
    client_list = []

    while True:
        try:
            conn, addr = sk.accept()
            client_list.append((conn, addr))
        except:
            pass
        else:
            print('%s 已经连接' % str(addr))
            print('当前已连接客户端:', [client[1] for client in client_list])
            print('#'*100)

        for client_sk, client_addr in client_list:
            try:
                recv_data = client_sk.recv(1024)
            except:
                pass
            else:
                if len(recv_data) > 0:
                    print("%s: %s" % (client_addr, recv_data))

                else:
                    print('%s 已经关闭' % str(client_addr))
                    client_sk.close()
                    client_list.remove((client_sk, client_addr))
                    print('当前已连接客户端:', [client[1] for client in client_list])
                    print('#'*100)

if __name__ == '__main__':
    main()

