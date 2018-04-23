#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 数数并说.py

Created by 彭思聪 on 2018/4/21 下午10:45.
Copyright © 2018年 彭思聪. All rights reserved.

"""  
"""
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
7.     13112221
8.     1113213211
9.     311211131221
10.    1321123113112211
11.    1113122112132113212221

1 -> 11
2 -> 12
3 -> 13



1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n ，输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:

输入: 1
输出: "1"

示例 2:

输入: 4
输出: "1211"

"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for _ in range(n-1):
            result = self.get_count_say(result)

        return result

    def get_count_say(self, s):

        pre = s[0]
        result = []
        count = 1
        index = 1

        while index < len(s):
            current_ch = s[index]
            if current_ch != pre:
                result.extend([str(count), pre])
                pre = current_ch
                count = 0
            else:
                count += 1
                index += 1

        result.extend([str(count), pre])

        return ''.join(result)



class Solution2:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        index = 1
        string = '1'
        while index < n:
            num = 0
            nextStr = ''
            prech = string[0]
            for ch in string:
                if ch == prech:
                    num += 1
                else:
                    nextStr += (str(num)+prech)
                    num = 1
                    prech = ch
            nextStr += (str(num)+prech)
            string = nextStr
            index += 1
        return string


if __name__ == '__main__':
    print(Solution().countAndSay(6))
