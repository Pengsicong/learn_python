#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: photocut.py

Created by 彭思聪 on 2018/4/5 下午2:24.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import numpy as np
from PIL import Image


def photocut(source_file, destination_file):

    s_img = Image.open(source_file)
    img_array = np.array(s_img)

    for col in range(img_array.shape[0]):
        for row in range(img_array.shape[1]):
            if [114, 243, 74, 255] == list(img_array[col][row]):
                img_array[col][row] = [0, 0, 0, 0]

    d_img = Image.fromarray(img_array)

    d_img.save(destination_file)


if __name__ == '__main__':

    photocut('58.png', 'p-58.png')