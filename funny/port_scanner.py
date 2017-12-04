#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: port_scanner.py

Created by 彭思聪 on 2017/11/30 上午2:25.
Copyright © 2017年 彭思聪. All rights reserved.

"""
from time import perf_counter
import gevent
from gevent import socket
from gevent.pool import Pool

"""
一个简单的端口扫描器
"""

pool = Pool(65535)


def foo(n):
    print('%d start------>%s pool' % (n, len(pool)))
    gevent.sleep(1)
    print('%d end------>%s pool' % (n, len(pool)))


def port_scaner(port, timeout=2):
    ip = '127.0.0.1'
    address = (ip, port)
    try:
        sk = socket.create_connection(address, timeout=timeout)
        sk.close()
        return port
    except Exception as e:
        # print(e)
        return None


if __name__ == '__main__':
    start = perf_counter()

    # jobs = [gevent.spawn(port_scaner, ('127.0.0.1' , port), 3) for port in range(1, 1025)]
    # gevent.joinall(jobs, timeout=2)
    # for job in jobs:
    #     if job.value:
    #         print(job.value)

    ports = pool.map(port_scaner, range(0, 65536))

    for port in ports:
        if port:
            print(port)
print(perf_counter() - start)



