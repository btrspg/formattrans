#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 8/1/2020 6:18 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : paf2gtf
# @Software: PyCharm

from fmttrans.paf import Paf
from fmttrans.utils import *

def paf2gtf(paf_file,gtf_file,mapped_length_r=0.9,mapping_q=60,align_ident=0.9):
    '''

    :param paf_file:
    :param gtf_file:
    :param mapped_length_r:
    :param mapping_q:
    :param align_ident:
    :return:
    '''
    paf = Paf(paf_file)
    for pafe in paf:
        if mapped_length_rate(paf) > mapped_length_r and \
                float(pafe.mapping_quality) > mapping_q and \
                align_identity(pafe) > align_ident:
           exons=align2exons(int(pafe.target_start),
                             int(pafe.target_end),
                             extract_cg_value(pafe.sam_tag['cg']),
                             pafe.strand)
           print(pafe)
           print(exons)
    return True
