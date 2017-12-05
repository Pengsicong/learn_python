#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多线程_信号量.py

Created by 彭思聪 on 2017/12/5 下午7:53.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import threading
import time

"""
信号量
    控制可以执行的线程数
"""

semaphore = threading.BoundedSemaphore(3)


class MyThread(threading.Thread):

    def __init__(self, sleep_time):
        # threading.Thread.__init__(self)
        super(MyThread, self).__init__()
        self.sleep_time = sleep_time

    def run(self):
        if semaphore.acquire():
            print('%s start in %s, now active threads %s' % (self.name, time.ctime(), threading.active_count()))
            time.sleep(self.sleep_time)
            print('%s end in %s' % (self.name, time.ctime()))
            semaphore.release()


def main():

    threads = []

    for i in range(1, 10):
        t = MyThread(i)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()


