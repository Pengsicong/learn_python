#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: 颜色反转.py

Created by 彭思聪 on 2018/1/16 下午6:37.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import numpy as np
from PIL import Image


def main(img_path):
    img = Image.open(img_path)

    n_white = np.ones_like(img) * 255

    reverse_vector = img ^ n_white

    revese_img = Image.fromarray(reverse_vector)

    return revese_img


if __name__ == '__main__':
    path = './lena_512.jpg'

    im = main(path)

    im.show()
