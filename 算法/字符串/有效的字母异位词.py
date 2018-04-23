#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 有效的字母异位词.py

Created by 彭思聪 on 2018/4/21 下午9:15.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

例如，
s = "anagram"，t = "nagaram"，返回 true
s = "rat"，t = "car"，返回 false

注意:
假定字符串只包含小写字母。

提升难度:
输入的字符串包含 unicode 字符怎么办？你能能否调整你的解法来适应这种情况？
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        d = {letter: s.count(letter) for letter in set(s)}

        for letter in set(t):
            if d.get(letter, None) != t.count(letter):
                return False
        return True


class Solution2:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        from collections import Counter

        return Counter(s) == Counter(t)


if __name__ == '__main__':
    s = "ab"
    t = "ba"
    print(Solution2().isAnagram(s, t))

