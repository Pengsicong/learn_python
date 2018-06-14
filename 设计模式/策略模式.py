#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 策略模式.py

Created by 彭思聪 on 2018/6/11 上午8:19.
Copyright © 2018年 彭思聪. All rights reserved.

"""


class QuackBase(object):
    """鸭子叫的行为基类"""
    def quack(self):
        pass


class Quack(QuackBase):
    """实现鸭子呱呱叫"""
    def quack(self):
        print('我是一只平凡的鸭子~~')


class Squeak(QuackBase):
    """橡皮鸭子呱呱叫"""
    def quack(self):
        print('我是一只橡皮鸭~~')


class MuteQuack(QuackBase):
    """什么都不做,不会叫"""
    def quack(self):
        print('我是一只哑巴鸭子~~')


class FlyBase(object):
    """飞行行为的基类"""
    def fly(self):
        pass


class FlyWithWings(FlyBase):
    """实现用翅膀飞行"""
    def fly(self):
        print('我在用翅膀飞行')


class FlyNoWay(FlyBase):
    """什么都不做, 不会飞"""
    def fly(self):
        print('不会飞')


class Duck(object):
    """所有鸭子的基类"""
    def __init__(self):
        self.quackBehavior = QuackBase()
        self.flyBehavior = FlyBase()

    def performQuack(self):
        self.quackBehavior.quack()

    def performFly(self):
        self.flyBehavior.fly()

    def setQuackBehavior(self, fb):
        self.quackBehavior = fb

    def setFlyBehavior(self, fb):
        self.flyBehavior = fb

    def swim(self):
        pass

    def display(self):
        pass


class MallardDuck(Duck):
    """绿头鸭的类"""
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()


if __name__ == '__main__':
    d = MallardDuck()
    d.performQuack()
    d.performFly()
    d.setQuackBehavior(Squeak())
    d.setFlyBehavior(FlyNoWay())
    d.performQuack()
    d.performFly()
