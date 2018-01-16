#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: plot_analysis.py

Created by 彭思聪 on 2018/1/15 下午11:38.
Copyright © 2018年 彭思聪. All rights reserved.

"""
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import csv


# 数据集路径
data_path = './survey_row.csv'


def run():
    contury_set = dict()
    with open(data_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        keys = reader.__next__()

        for row in reader:

            try:
                contury_set[row[3]] += 1
            except KeyError:
                contury_set[row[3]] = 1

        group_data = []
        group_names = []
        items = sorted(contury_set.items(), key=lambda d: d[1])

        for item in items:
            if item[1] > 4:
                group_names.append(item[0])
                group_data.append(item[1])

        idx = np.arange(len(group_data))

        color = cm.jet(np.array(group_data) / max(group_data))
        plt.barh(idx, group_data, color=color)
        plt.yticks(idx, group_names)

        plt.show()


if __name__ == '__main__':
    run()
