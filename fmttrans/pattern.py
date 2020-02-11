#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 8/1/2020 1:40 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : pattern
# @Software: PyCharm

import re

cg_tag_pattern = re.compile('([0-9]+)([MNDI])')
gtf_transcript_pattern = re.compile('transcript_id "([\.A-Z0-9]+?)"')
