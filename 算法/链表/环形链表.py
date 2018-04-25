#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 环形链表.py

Created by 彭思聪 on 2018/4/25 下午1:03.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    Hash Table
    时间复杂度 O(n)
    空间复杂度 O(n)
    执行用时：100 ms
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_seen = set()

        while head:
            if head in node_seen:
                return True
            else:
                node_seen.add(head)
            head = head.next
        return False


class Solution2(object):
    """
    Two Pointers
    时间复杂度 O(n)
    空间复杂度 O(1)
    执行用时: 56 ms
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
