#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 存在重复.py

Created by 彭思聪 on 2018/4/20 下午9:01.
Copyright © 2018年 彭思聪. All rights reserved.

"""

"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。
"""


class SolutionSort:
    """Runtime: 80ms"""
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) == 1:
            return False
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


class SolutionHash:
    """Runtimes 72ms """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()

        for val in nums:

            if val in s:
                return True
            s.add(val)

        return False


class SolutionHash2:
    """Runtimes 72ms """

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)

        if len(s) != len(nums):
            return True

        return False


if __name__ == '__main__':
    nums = [2,14,18,22,13]
    print(SolutionHash2().containsDuplicate(nums))


