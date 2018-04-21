#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 两数之和.py

Created by 彭思聪 on 2018/4/21 上午11:51.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d_hash = dict()

        for i, val in enumerate(nums):

            val2 = target - val
            i2 = d_hash.get(val2, None)

            if i2 is not None:
                return [i2, i]

            d_hash[val] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))

