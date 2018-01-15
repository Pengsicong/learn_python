#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 图片格式转换.py

Created by 彭思聪 on 2018/1/15 上午2:22.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

from PIL import Image
import os


def topng(filepath):
    im = Image.open(filepath)
    pngImg = os.path.splitext(filepath)[0] + '.png'
    try:
        im.save(pngImg)
        print('png convert successful!')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    topng('lena_512.jpg')

