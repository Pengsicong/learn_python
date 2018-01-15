#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: zhaocha.py

Created by 彭思聪 on 2018/1/15 下午12:49.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import wda
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


c = wda.Client()

c.screenshot('./1.png')

im = Image.open('./1.png').convert('RGB')

p1 = im.crop((148, 713, 721, 1286))

p2 = im.crop((148, 116, 721, 689))


n1 = np.array(p1)
n2 = np.array(p2)
n3 = n1 ^ n2

im3 = Image.fromarray(n3, 'RGB')

plt.subplot(131)
plt.imshow(n1)

plt.subplot(132)
plt.imshow(n2)

plt.subplot(133)
plt.imshow(im3.convert('L'))

plt.show()

