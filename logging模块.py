#!/usr/bin/env python
# encoding: utf-8

"""

File Name: logging模块.py

Created by 彭思聪 on 2017/11/26 上午10:58.
Copyright © 2017年 彭思聪. All rights reserved.

"""

import logging


logger = logging.getLogger('mylooger')

fh = logging.FileHandler('test.log')
sh = logging.StreamHandler()

fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

fh.setFormatter(fmt)
sh.setFormatter(fmt)

logger.addHandler(fh)
logger.addHandler(sh)

logger.setLevel('DEBUG')

# logger.removeHandler(fh)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

