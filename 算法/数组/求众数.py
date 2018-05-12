#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 求众数.py

Created by 彭思聪 on 2018/5/7 下午5:55.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_dic = {}
        majority = None
        maxnum = 0

        for val in nums:
            key = hash_dic.get(val, None)
            if key is None:
                hash_dic[val] = 1
            else:
                hash_dic[val] += 1
            if maxnum < hash_dic[val]:
                maxnum = hash_dic[val]
                majority = val

        if maxnum > len(nums) // 2:
            return majority
        return None

if __name__ == '__main__':
    print(Solution().majorityElement([1]))