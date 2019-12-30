#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 30/12/2019 12:14 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : utils
# @Software: PyCharm

import os


def file_exists(*filenames):
    return [os.path.exists(filename) for filename in filenames]
