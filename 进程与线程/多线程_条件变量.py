#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多线程_条件变量.py

Created by 彭思聪 on 2017/12/5 下午8:26.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import threading
import time
import random

"""
条件变量同步(Condition)
    有一类线程需要满足条件之后才能够继续执行, python提供了threading.Condition对象用于条件变量线程的支持,他除了能提供RLock()或Lock()
    的方法外,还提供了wait(), notify(), notifyAll()方法
    
    lock_con=threading.Condition([Lock/Rlock])： 锁是可选选项，不传人锁，对象自动创建一个RLock()。

    wait()：条件不满足时调用，线程会释放锁并进入等待阻塞；
    notify()：条件创造后调用，通知等待池激活一个线程；
    notifyAll()：条件创造后调用，通知等待池激活所有线程。
"""

# 生产缓冲区
buffer = []

# 缓冲区大小
BUFFER_MAX = 100

# 产品编号
i = 0

# 条件变量
lock_con = threading.Condition()


# 生产者
class Producer(threading.Thread):

    def __init__(self, people):
        super(Producer, self).__init__()
        self.people = people

    # 每1秒生产一个产品
    def run(self):
        global buffer
        global i
        while True:
            if len(buffer) < BUFFER_MAX and lock_con.acquire():
                item = 'item%s' % i
                time.sleep(0.2)
                buffer.append(item)
                i += 1
                print('producer %s produce %s at %s, buffer size: %s' % (self.people, item, time.ctime(), len(buffer)))
                # 通知所有等待的consumer,所以consumer不能超过一个
                lock_con.notify(1)
                lock_con.release()

            # 如果生产者没有获取锁或者缓冲区满则等待0.01秒, 优先消费者获取锁
            time.sleep(0.01)


# 消费者
class Consumer(threading.Thread):

    def __init__(self, people):
        super(Consumer, self).__init__()
        self.people = people

    # 在0-1秒之间的随机时间内随机消费一个产品
    def run(self):
        global buffer

        while True:
            lock_con.acquire()

            if len(buffer) == 0:
                print('consumer %s wait...' % self.people)

                # wait方法会有一个锁的释放过程
                lock_con.wait()
                print('consumer %s wake up!' % self.people)

                # 这一步很关键, 当消费者线程wake up时要重新判读buffer的情况,不然很可能会出现缓冲区为空(别的线程消费了)
                continue

            cost_time = random.random()
            item = buffer.pop(random.choice(range(len(buffer))))
            print('consumer %s consum %s cost %0.3f sec at %s, buffer size %s' %
                  (self.people, item, cost_time, time.ctime(), len(buffer)))

            lock_con.release()

            time.sleep(cost_time)


# 通过条件变量来模拟生产者-消费之模型
def main():
    threads = []

    # 两个生产者
    for people in range(2):
        t = Producer(people+1)
        threads.append(t)
        t.setDaemon(True)
        t.start()

    # 五个消费者
    for people in range(50):
        t = Consumer(people+1)
        threads.append(t)
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':

    main()
