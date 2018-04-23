#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 反转字符串.py

Created by 彭思聪 on 2018/4/21 下午1:11.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
请编写一个函数，其功能是将输入的字符串反转过来。

示例：

输入：s = "hello"
返回："olleh"

"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        str_list.reverse()
        return ''.join(str_list)


if __name__ == '__main__':
    s = "hello"
    print(Solution().reverseString(s))