#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 父类重写.py

Created by 彭思聪 on 2018/5/5 上午10:31.
Copyright © 2018年 彭思聪. All rights reserved.

"""  


class Animal:

    def eat(self):
        print('----吃----')


class Dog(Animal):

    def eat(self):
        print('---大口吃-----')

        # 三种继承父类的方法
        Animal.eat(self)
        super().eat()
        super(Dog, self).eat()


wangcai = Dog()

wangcai.eat()
