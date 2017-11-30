#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: port_scanner.py

Created by 彭思聪 on 2017/11/30 上午2:25.
Copyright © 2017年 彭思聪. All rights reserved.

"""

from time import perf_counter
from socket import socket

"""
一个简单的端口扫描器
"""


def is_port_open(adress, timeout=1):
    try:
        sk = socket()
        sk.settimeout(timeout)
        start = perf_counter()
        sk.connect(adress)
        print(perf_counter() - start)
        sk.shutdown(2)
        return True
    except Exception as e:
        print(e)
        sk.close()


def port_scanner(ip, ports, timeout=1):
    open_ports = []

    if isinstance(ports, int):
        port = ports
        ports = [port]

    for port in ports:
        adress = (ip, port)
        if is_port_open(adress, timeout):
            open_ports.append(port)
    return open_ports


if __name__ == '__main__':
    ip = '45.77.192.16'
    print(port_scanner(ip, [888]))
    # import sys
    #
    # try:
    #     args = sys.argv[1:]
    #     ip = args[0]
    #     port = int(args[1])
    #     print(port_scanner(ip, port))
    # except Exception as e:
    #     pass

