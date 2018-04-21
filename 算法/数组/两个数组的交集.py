#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 两个数组的交集.py

Created by 彭思聪 on 2018/4/20 下午8:25.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
描述:
给定两个数组，写一个方法来计算它们的交集。

例如:
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

注意：

       输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
       我们可以不考虑输出结果的顺序。

跟进:

    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？

"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1.sort()
        nums2.sort()

        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            return []

        intersect = list()

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersect.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return intersect

if __name__ == '__main__':
    nums1 = [-2147483648,1,2,3]

    nums2 = [1,-2147483648,-2147483648]
    print(Solution().intersect(nums1, nums2))
