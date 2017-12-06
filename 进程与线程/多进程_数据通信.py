#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多进程_数据通信.py

Created by 彭思聪 on 2017/12/6 下午3:41.
Copyright © 2017年 彭思聪. All rights reserved.

"""

from multiprocessing import Process, Queue, Pipe, Manager

"""
不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法：
    1. Queues
        注意这里的队列不是线程中的队列, 它通过from multiprocessing import Queue来引用
        
    2. Pipes
        The Pipe function returns a pair of connection objects connected by a pipe which by default is duplex (two-way)
        
        The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has 
        send() and recv() methods (among others). Note that data in a pipe may become corrupted if two processes 
        (or threads) try to read from or write to the same end of the pipe at the same time. Of course there is no risk
         of corruption from processes using different ends of the pipe at the same time.
    3. Managers
        A manager object returned by Manager() controls a server process which holds Python objects and allows other 
        processes to manipulate them using proxies.

        A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, Semaphore, 
        BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array. 
"""


def foo_queue(queue):
    print('foo q id:%s' % id(queue))
    for _ in range(30):
        queue.put('foo')


def bar_queue(queue):
    print('bar q id: %s' % id(queue))
    for _ in range(30):
        queue.put('bar')


def foo_pipe(conn):
    conn.send('hi, I am foo!')
    print(conn.recv())
    conn.close()


def bar_pipe(conn):
    conn.send('hi, I am bar!')
    print(conn.recv())
    conn.close()


def test_queue():
    q = Queue()

    print('main q id: %s' % id(q))
    p1 = Process(target=foo_queue, args=(q,))
    p2 = Process(target=bar_queue, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    qsize = 0
    while not q.empty():
        print(q.get())
        qsize += 1

    print('qsize: %s' % qsize)


def test_pipe():
    parent_conn, child_conn = Pipe()

    p1 = Process(target=foo_pipe, args=(child_conn, ))
    p2 = Process(target=bar_pipe, args=(child_conn, ))

    p1.start()
    p2.start()

    print(parent_conn.recv())
    parent_conn.send('hi foo, I am your father!')

    print(parent_conn.recv())
    parent_conn.send('hi bar, I am your father!')

    p1.join()
    p2.join()


def foo_manager(di, li, namespace, lock):
    di['foo'] = 'hi'

    for _ in range(10):
        li.append('foo')

    for _ in range(10000):

        lock.acquire()
        namespace.x -= 1
        lock.release()


def bar_manager(di, li, namespace, lock):
    di['bar'] = 'hi'

    for _ in range(10):
        li.append('bar')

    for _ in range(10000):

        lock.acquire()
        namespace.x += 1
        lock.release()


def test_manager():
    with Manager() as manager:

        # 创建共享字典
        di = manager.dict()

        # 创建共享列表
        li = manager.list()

        # 创建共享命名空间
        namespace = manager.Namespace()

        # 创建共享锁
        lock = manager.Lock()

        namespace.x = 0

        p1 = Process(target=foo_manager, args=(di, li, namespace, lock))
        p2 = Process(target=bar_manager, args=(di, li, namespace, lock))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        for k, v in di.items():
            print(k, v)

        for item in li:
            print(item)

        print('x = %s' % namespace.x)


if __name__ == '__main__':
    # test_queue()
    # test_pipe()
    test_manager()
