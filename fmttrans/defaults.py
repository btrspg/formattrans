#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 24/12/2019 12:34 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : defaults
# @Software: PyCharm


from collections import namedtuple


def fill_namedtuple(nt, list_for_fill):
    return nt._make(list_for_fill)


paf_elements = namedtuple('paf_elements',
                          ['query_name', 'query_len', 'query_start', 'query_end', 'strand', 'target_name',
                           'target_length', 'target_start', 'target_end', 'number_match', 'align_block_len',
                           'mapping_quality', 'sam_tag'])
