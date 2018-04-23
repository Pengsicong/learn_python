#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 颠倒整数.py

Created by 彭思聪 on 2018/4/21 下午1:15.
Copyright © 2018年 彭思聪. All rights reserved.

"""

"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321

 示例 2:

输入: -123
输出: -321

示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str_list = list(str(x))

        x_str_list.reverse()

        if x_str_list[-1] == '-':
            reverse_x =  -int(''.join(x_str_list[:-1]))
        else:
            reverse_x = int(''.join(x_str_list))

        if reverse_x > 2**31-1 or reverse_x < -2**31:
            reverse_x = 0

        return reverse_x


if __name__ == '__main__':
    x = 1563847412
    print(Solution().reverse(x))

