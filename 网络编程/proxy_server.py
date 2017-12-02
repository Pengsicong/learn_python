#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: proxy_server.py

Created by 彭思聪 on 2017/12/1 上午11:05.
Copyright © 2017年 彭思聪. All rights reserved.

"""  

import socket
from threading import Thread
import re
import requests


def save_image(url, filename=''):
    headers = {
        'Referer': 'http://i.meizitu.net/'
    }
    if filename == '':
        filename = url.split('/')[-1]

    r = requests.get(url, headers=headers)

    with open(filename, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    # r = requests.get('http://i.meizitu.net/2017/11/30b03.jpg')
    # html = r.text
    # print(re.findall(r'http://i\.meizitu\.net[^\"|\']+?', html))
    url = 'http://i.meizitu.net/2017/11/30b03.jpg'
    save_image(url, 'meizi10.jpg')
