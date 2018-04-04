#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 单例模式.py

Created by 彭思聪 on 2017/11/28 下午6:00.
Copyright © 2017年 彭思聪. All rights reserved.

"""
import threading

"""
单例模式
    单例，永远使用同一份实例（对象), 在创建对象时只需在内存中创建一份即可，并在这个对象中封装一些成员.
    通过单例模式可以保证系统中一个类只有一个实例而且该实例易于被外界访问, 从而方便对实例个数的控制并节约系统资源.
    典型使用场景，数据库的连接，
    数据库连接池的实现（只创建一份)

        # 简单单例模式的创建
        class Bar:

            __v = None

            @classmethod
            def get_instance(cls):
                if cls.__v:
                    return cls.__v

                else:
                    cls.__v = Bar()
                    return cls.__v


        obj1 = Bar.get_instance()
        print(obj1)         # <__main__.Bar object at 0x103a3bcc0>  

        obj2 = Bar.get_instance()
        print(obj2)         # <__main__.Bar object at 0x103a3bcc0>

"""


# 基本上保证只能有一个实例的要求, 但是在并发的情况下可能会发生意外
class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


# 带锁的版本
class Singleton2(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()

        try:
            if cls in cls.objs:
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()

        return cls.objs[cls]


if __name__ == '__main__':
    s1 = Singleton2()
    s2 = Singleton2()
    assert id(s1) == id(s2)