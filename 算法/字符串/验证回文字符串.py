#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 验证回文字符串.py

Created by 彭思聪 on 2018/4/21 下午9:37.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false

"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j = len(s) - 1
        i = 0
        letter_digst = set('abcdefghijklmnopqrstuvwxyz0123456789')

        s = s.lower()

        while i < len(s):
            if s[i] in letter_digst:
                while j > 0:
                    if s[j] in letter_digst:
                        if s[j] == s[i]:
                            j -= 1
                            break
                        else:
                            return False
                    j -= 1
            i += 1
        return True


class Solution2:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanlist = [x for x in s.lower() if x.isalnum()]
        return cleanlist[::] == cleanlist[::-1]

if __name__ == '__main__':
    s = "aca"
    print(Solution2().isPalindrome(s))



