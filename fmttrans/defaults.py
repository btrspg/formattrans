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

samtag_description = {
    'tp': 'Type of aln: P/primary, S/secondary and I,i/inversion',
    'cm': 'Number of minimizers on the chain',
    's1': 'Chaining score',
    's2': 'Chaining score of the best secondary chain',
    'NM': 'Total number of mismatches and gaps in the alignment',
    'MD': 'To generate the ref sequence in the alignment',
    'AS': 'DP alignment score',
    'ms': 'DP score of the max scoring segment in the alignment',
    'nn': 'Number of ambiguous bases in the alignment',
    'ts': 'Transcript strand (splice mode only)',
    'cg': 'CIGAR string (only in PAF)',
    'cs': 'Difference string',
    'dv': 'Approximate per-base sequence divergence',
    'de': 'Gap-compressed per-base sequence divergence',
    'rl': 'Length of query regions harboring repetitive seeds',
}
