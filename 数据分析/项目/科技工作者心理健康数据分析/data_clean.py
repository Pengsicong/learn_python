#!/usr/bin/env python3 
# encoding: utf-8  

""" 

File Name: data_clean.py

Created by 彭思聪 on 2018/1/15 下午11:33.
Copyright © 2018年 彭思聪. All rights reserved.

"""  

import csv

# 数据集路径
data_path = './survey_row.csv'


def run():
    gender_set = set()
    contury_set = dict()
    with open(data_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        keys = reader.__next__()

        for row in reader:
            gender_set.add(row[2].lower())

            try:
                contury_set[row[3]] += 1
            except KeyError:
                contury_set[row[3]] = 1

        print(gender_set)
        print(contury_set)


if __name__ == '__main__':
    run()