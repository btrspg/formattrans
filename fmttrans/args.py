#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 13/1/2020 11:37 AM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : args
# @Software: PyCharm


from fmttrans.paf2gtf import paf2gtf
from fmttrans.divide2bed import divide2bed
from fmttrans.defaults import PLOT_GENE_LIST


def paf2gtf_args(parser_sub):
    '''

    :param parser_sub:
    :return:
    '''
    sp = parser_sub.add_parser('paf2gtf',
                               help='transform paf file to gtf file')

    sp.add_argument('--paf', required=True,
                    help='input file (PAF), see https://github.com/lh3/miniasm/blob/master/PAF.md')
    sp.add_argument('--gtf', required=True,
                    help='output gtf file')
    sp.add_argument('--mapped-length-rate', default=0.9, type=float,
                    help='threshold for filter the mapping length rate')
    sp.add_argument('--mapping-quality', default=60, type=int,
                    help='threshold for filter the mapping quality')
    sp.add_argument('--align-identity', default=0.9, type=float,
                    help='threshold for alignment identity')
    sp.add_argument('--tag', default='assembly', type=str,
                    help='tag for source column in gtf file')
    sp.set_defaults(func=paf2gtf)
    return sp


def divide2bed_args(parser_sub):
    '''

    :param parser_sub:
    :return:
    '''
    sp = parser_sub.add_parser('gffcompare2beds',
                               help='gffcompare results extract')

    sp.add_argument('--annotate-gtf', required=True,
                    help='annotate gtf file')
    sp.add_argument('--test-gtf', required=True,
                    help='test gtf file')
    sp.add_argument('--gffcompare-prefix', required=True,
                    help='gffcompare results prefix')
    sp.add_argument('--prefix', required=True,
                    help='output bed files prefix')
    sp.add_argument('--gene-list', nargs='+', default=PLOT_GENE_LIST,
                    help='plot gene list')
    sp.set_defaults(func=divide2bed)
    return sp
