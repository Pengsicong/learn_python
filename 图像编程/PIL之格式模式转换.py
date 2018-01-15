#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: PIL之格式模式转换.py

Created by 彭思聪 on 2018/1/15 上午1:48.
Copyright © 2018年 彭思聪. All rights reserved.

"""

from PIL import Image

"""
在数字图像处理中，针对不同的图像格式有其特定的处理算法。所以在做图像处理之前，我们需要考虑清楚自己要基于哪种格式的图像进行算法设计及其实现

对于彩色图像，不管其图像格式是PNG，还是BMP，或者JPG，在PIL中，使用Image模块的open()函数打开后，返回的图像对象的模式都是“RGB”。
而对于灰度图像，不管其图像格式是PNG，还是BMP，或者JPG，打开后，其模式为“L”。

对于PNG、BMP和JPG彩色图像格式之间的互相转换都可以通过Image模块的open()和save()函数来完成。
具体说就是，在打开这些图像时，PIL会将它们解码为三通道的“RGB”图像。用户可以基于这个“RGB”图像，对其进行处理。处理完毕，使用函数save()，
可以将处理结果保存成PNG、BMP和JPG中任何格式。这样也就完成了几种格式之间的转换。同理，其他格式的彩色图像也可以通过这种方式完成转换。
当然，对于不同格式的灰度图像，也可通过类似途径完成，只是PIL解码后是模式为“L”的图像。

这里，详细介绍一下Image模块的convert()函数，用于不同模式图像之间的转换。

Convert()函数有三种形式的定义，它们定义形式如下：

im.convert(mode) ⇒ image

im.convert(“P”, **options) ⇒ image

im.convert(mode, matrix) ⇒ image

使用不同的参数，将当前的图像转换为新的模式，并产生新的图像作为返回值。

PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。

这里采用的示例图像是图像处理中经典的lena照片。分辨率为512x512

"""

# 打开原图
lena = Image.open('lena_512.jpg')

# RGB
print(lena.mode)

# 获取坐标(0,0)像素的值,这里为RGB值(226, 137, 123)
print(lena.getpixel((0, 0)))

# 模式“1”为二值图像，非黑即白。但是它每个像素用8个bit表示，0表示黑，255表示白。
lena_1 = lena.convert("1")
# lena_1.show()

# 白色255
print(lena_1.getpixel((0, 0)))

# 模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# 在PIL中，从模式“RGB”转换为“L”模式是按照下面的公式转换的：
# L = R * 299/1000 + G * 587/1000+ B * 114/1000
lena_L = lena.convert("L")
lena_L.show()

# 226*299/1000 + 137*587/1000 + 123*114/1000 ~= 162
print(lena_L.getpixel((0, 0)))






