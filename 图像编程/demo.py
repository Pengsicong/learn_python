#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: demo.py

Created by 彭思聪 on 2018/1/15 上午1:13.
Copyright © 2018年 彭思聪. All rights reserved.

"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('lena_512.jpg')

imarry = np.array(im)

print(imarry)

imarry = imarry[:, :, ]

plt.imshow(imarry)
plt.show()

