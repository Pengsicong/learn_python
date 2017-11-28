#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 单例模式.py

Created by 彭思聪 on 2017/11/28 下午6:00.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

"""
单例模式
    单例，永远使用同一份实例（对象), 在创建对象时只需在内存中创建一份即可，并在这个对象中封装一些成员。典型使用场景，数据库的连接，
    数据库连接池的实现（只创建一份）

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
