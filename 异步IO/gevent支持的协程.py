#!/usr/bin/env python3
# encoding: utf-8  

""" 

File Name: gevent支持的协程.py

Created by 彭思聪 on 2018/1/9 下午10:44.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import gevent


def foo():
    print('foo running...')
    gevent.sleep(2)
    print('foo end cost 2 sec')


def bar():
    print('bar running...')
    gevent.sleep(1)
    print('bar end cost 1 sec')


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar)
    ])
