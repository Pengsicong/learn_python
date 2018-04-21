#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 移动零.py

Created by 彭思聪 on 2018/4/20 下午10:01.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

注意事项:

    必须在原数组上操作，不要为一个新数组分配额外空间。
    尽量减少操作总数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        old_nums = nums.copy()
        nums.clear()
        zero_count = 0

        for val in old_nums:
            if val != 0:
                nums.append(val)
            else:
                zero_count += 1

        nums.extend([0] * zero_count)


class SolutionOptimal:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        none_zero_at = 0

        for i, val in enumerate(nums):
            if val != 0:
                nums[none_zero_at] = val
                none_zero_at += 1

        nums[none_zero_at:] = [0] * (len(nums) - none_zero_at)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12, 1, 2, 3, 3]
    SolutionOptimal().moveZeroes(nums)
    print(nums)
