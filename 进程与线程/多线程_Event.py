#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 多线程_Event.py

Created by 彭思聪 on 2017/12/5 下午10:33.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import threading
import time
import random

"""
条件同步和条件变量同步差不多意思，只是少了锁功能，因为条件同步设计于不访问共享资源的条件环境。event=threading.Event()：条件环境对象，初始值 为False；

    event.isSet()：返回event的状态值；

    event.wait()：如果 event.isSet()==False将阻塞线程；

    event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；

    event.clear()：恢复event的状态值为False。
"""

Q_A = {
    '1+1': 2,
    '1+2': 3,
    '2+2': 4,
    '2+3': 5,
}


class Teacher(threading.Thread):

    def run(self):
        global answer
        global winner_name
        while True:
            winner_name = ''
            question, answer = random.choice(list(Q_A.items()))
            print('-------------------------------------------')
            print('| Teacher: what is the answer about %s ? |' % question)
            print('-------------------------------------------\n')
            q_event.isSet() or q_event.set()
            end_event.wait()
            if a_event.isSet():
                print('\nThe winner is %s\n' % winner_name)
                a_event.clear()
            else:
                print('\nthere is no winner!\n')
            q_event.clear()
            print('wait 3 sec...\n')
            time.sleep(3)
            end_event.clear()


class Student(threading.Thread):

    def __init__(self, name):
        super(Student, self).__init__()
        self.student_name = name

    def run(self):
        global winner_name

        while True:
            q_event.wait()
            local_answer = random.randint(1, 10)
            print('%s : the answer is %s' % (self.student_name, local_answer))
            if answer == local_answer:
                winner_name = ' '.join([winner_name, self.student_name])
                if not a_event.isSet():
                    a_event.set()
            time.sleep(1)
            if q_event:
                q_event.clear()
            end_event.set()


def main():
    threads = []
    t = Teacher()
    t.setDaemon(True)
    t.start()
    threads.append(t)

    names = ['Tom', 'Jack', 'Lady', 'Gaga', 'Angel']

    for name in names:
        t = Student(name)
        t.setDaemon(True)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    q_event = threading.Event()
    a_event = threading.Event()
    end_event = threading.Event()
    winner_name = ''
    answer = ''
    main()
