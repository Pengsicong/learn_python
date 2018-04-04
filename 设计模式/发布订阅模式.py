#!/usr/bin/env python3 
# encoding: utf-8  

from collections import defaultdict

""" 

File Name: 发布订阅模式.py

Created by 彭思聪 on 2018/4/4 下午2:27.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
发布订阅模式是一种编程模式.
    消息的发送者(发布者)不会发送其消息给特定的接受者(订阅者), 而是将发布的消息分为不同的类别直接发布, 并不关注订阅者是谁.
    而订阅者可以对一个或多个类别感兴趣, 且只接受感兴趣的消息, 并且不关注是哪个发布者发布的消息.
    这种模式可以允许更好的可拓展性和更为动态的网络拓扑
优点是发布者和订阅者松散的耦合
    双方不需要知道对方的存在. 由于主题是被关注的, 发布者和订阅者可以对系统拓扑毫无所知. 无论对方是否存在, 发送者和订阅者都可以继续正常操作.
    要实现这种模式, 就需要一个中间代理人, 在实现中一般被称为Broker, 它维护者发布者和订阅者的关系: 订阅者把感兴趣的主题告诉它, 而发布者的信息
    也通过它路由到各个订阅者处.
"""


class Broker(object):

    route_table = defaultdict(list)

    def sub(self, topic, callback):
        if callback in self.route_table[topic]:
            return
        self.route_table[topic].append(callback)

    def pub(self, topic, *args, **kwargs):
        for func in self.route_table[topic]:
            func(*args, **kwargs)


if __name__ == '__main__':
    def gretting(name):
        print('hello, %s!' % name)


    broker = Broker()
    broker.sub('greet', gretting)
    broker.pub('greet', 'congcong')
