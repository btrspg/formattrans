#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 24/12/2019 11:15 AM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : paf
# @Software: PyCharm

from fmttrans.defaults import paf_elements, fill_namedtuple


class Paf:
    '''
PAF file class
source from https://github.com/lh3/miniasm/edit/master/PAF.md

|Col|Type  |Description                               |
|--:|:----:|:-----------------------------------------|
|1  |string|Query sequence name                       |
|2  |int   |Query sequence length                     |
|3  |int   |Query start (0-based; BED-like; closed)   |
|4  |int   |Query end (0-based; BED-like; open)       |
|5  |char  |Relative strand: "+" or "-"               |
|6  |string|Target sequence name                      |
|7  |int   |Target sequence length                    |
|8  |int   |Target start on original strand (0-based) |
|9  |int   |Target end on original strand (0-based)   |
|10 |int   |Number of residue matches                 |
|11 |int   |Alignment block length                    |
|12 |int   |Mapping quality (0-255; 255 for missing)  |

    '''

    def __init__(self, filename):
        self._filename = filename
        self.file_buffer = open(self._filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file_buffer.readline().strip('\n')
        if line:
            return self.line2elements(line)
        else:
            raise StopIteration()

    def line2elements(self, paf_line):
        cells = paf_line.split('\t')
        if len(cells) <= 12:
            return fill_namedtuple(paf_elements, cells)
        else:
            return fill_namedtuple(paf_elements, [*cells[0:12], cells[12:]])

    def __str__(self):
        return 'filename:' + self._filename

    def __repr__(self):
        return 'filename:' + self._filename

    def __del__(self):
        self.file_buffer.close()
