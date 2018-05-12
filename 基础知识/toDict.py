#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: toDict.py

Created by 彭思聪 on 2018/5/11 上午10:09.
Copyright © 2018年 彭思聪. All rights reserved.

"""  


class ToDictMixin(object):
    """将内存中的python对象转换为字典形式"""
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, val) for val in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(10, left=BinaryTree(5), right=BinaryTree(15))
print(tree.to_dict())
