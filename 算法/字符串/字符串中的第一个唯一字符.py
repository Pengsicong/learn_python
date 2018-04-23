#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 字符串中的第一个唯一字符.py

Created by 彭思聪 on 2018/4/21 下午1:26.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

 

注意事项：您可以假定该字符串只包含小写字母。
"""
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = OrderedDict()
        for i, val in enumerate(s):
            i2 = d.get(val, None)
            # 存在重复
            if i2 is not None:
                d[val] = -1
            else:
                d[val] = i

        for val in d.values():
            if val != -1:
                return val
        return -1


import string
class Solution2:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min([s.index(ch) for ch in string.ascii_lowercase if s.count(ch) == 1] or [-1])


if __name__ == '__main__':
    print(Solution2().firstUniqChar("loveleetcode"))
