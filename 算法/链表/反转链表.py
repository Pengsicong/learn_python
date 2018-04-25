#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 反转链表.py

Created by 彭思聪 on 2018/4/24 下午9:17.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

"""
反转一个单链表。

进阶:
链表可以迭代或递归地反转。你能否两个都实现一遍？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next

        return '->'.join(map(str, result))


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        self.recursion_reverse_list(head)

        return self.tail

    def recursion_reverse_list(self, current_node):
        """

        :type current_node: ListNode
        """

        if current_node.next.next is None:
            self.tail = current_node.next
        else:
            self.recursion_reverse_list(current_node.next)

        current_node.next.next = current_node
        current_node.next = None


class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        previous = head
        current = head.next

        head.next = None

        while current.next:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        current.next = previous

        return current




if __name__ == '__main__':
    head = ListNode(1)
    current_node = head
    for i in range(2, 5):
        node = ListNode(i)
        current_node.next = node
        current_node = node

    print(Solution2().reverseList(head))
