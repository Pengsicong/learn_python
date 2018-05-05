#!/usr/bin/env python
# encoding: utf-8

""" 

File Name: 装饰器之登陆练习.py

Created by 彭思聪 on 2017/11/25 上午11:57.
Copyright © 2017年 彭思聪. All rights reserved.

"""

jd_user = {'Tony': '111111'}

wechat_user = {'Jack': '222222'}

login_status = False


def login(auth_type):

    def authentication(func):

        def wrapper():

            global login_status
            if login_status is False:
                if auth_type == 'jd':
                    username = input('username:')
                    if username in jd_user.keys():
                        passwd = input('passwd:')
                        if jd_user[username] == passwd:
                            print('login successful!')
                            func()
                            login_status = True
                        else:
                            print('passwd wrong! login failure!')
                            return
                    else:
                        print('username wrong! login failure!')
                        return

                elif auth_type == 'wechat':
                    username = input('username:')
                    if username in wechat_user.keys():
                        passwd = input('passwd:')
                        if wechat_user[username] == passwd:
                            print('login successful!')
                            func()
                            login_status = True
                        else:
                            print('passwd wrong! login failure!')
                            return
                    else:
                        print('username wrong! login failure!')
                        return

            else:
                func()

        return wrapper

    return authentication


@login(auth_type='jd')
def home():
    print('welcome to home')


@login(auth_type='wechat')
def finance():
    print('welcome to finance')


@login(auth_type='jd')
def book():
    print('welcome to book')


def run():

    while 1:
        print("(1) home")
        print("(2) finance")
        print("(3) book")
        print("(q) exit")
        key = input("your selection:")

        if key == '1':
            home()

        elif key == '2':
            finance()

        elif key == '3':
            book()

        elif key == 'q':
            print('已退出！')
            return


if __name__ == '__main__':
    run()
