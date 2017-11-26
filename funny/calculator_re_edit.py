#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: calculator_re_edit.py

Created by 彭思聪 on 2017/11/26 下午7:55.
Copyright © 2017年 彭思聪. All rights reserved.

"""


import re

# f = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# result =  2776672.6952380957


def str2digit(s):
    if s == '':
        return 0

    try:
        return int(s)

    except ValueError:
        return float(s)


def cal_2factor(a, sign, b):
    a = str2digit(a)
    b = str2digit(b)

    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        if a == 0:
            print('除零错！已退出')
            exit()
        else:
            return a / b

    return None


def cal_nobrackets(form):
    pattern_1 = re.compile('([\d.]+)([+-])([\d.-]+)')
    pattern_2 = re.compile('([\d.]+)([*/])([\d.-]+)')

    pat2_result = pattern_2.search(form)
    while pat2_result:
        a = pat2_result.group(1)
        sign = pat2_result.group(2)
        b = pat2_result.group(3)
        result = cal_2factor(a, sign, b)
        result = str(result)
        form = pattern_2.sub(result, form, 1)

        pat2_result = pattern_2.search(form)

    pat1_result = pattern_1.search(form)
    while pat1_result:
        a = pat1_result.group(1)
        sign = pat1_result.group(2)
        b = pat1_result.group(3)
        result = cal_2factor(a, sign, b)
        result = str(result)
        form = pattern_1.sub(result, form, 1)

        pat1_result = pattern_1.search(form)

    return form


def cal_brackets(form):
    # 匹配最里面括号以及括号里面内容
    pattern = re.compile('(\()([^(]+)(\))')

    pat_result = pattern.search(form)
    while pat_result:
        # 计算括号里面的结果
        result = cal_nobrackets(pat_result.group(2))
        form = pattern.sub(result, form, 1)

        pat_result = pattern.search(form)

    return form


def run():
    # formula = input()
    formula = '1/3+1/3+1/3 + 1/3 + 1/3 + 1/3'
    #  除去多余空白
    formula = formula.replace(' ', '')

    # 首先去除括号，并计算括号内容
    formula = cal_brackets(formula)

    # 直接计算
    result = cal_nobrackets(formula)

    print('result =  %s' % result)


if __name__ == '__main__':
    run()
