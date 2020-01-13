#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 24/12/2019 11:12 AM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : fmttrans
# @Software: PyCharm

import argparse
from fmttrans.args import *
def main():
    parser = argparse.ArgumentParser(description='Biology data format transform',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser_sub = parser.add_subparsers(dest='subparser_name', help='Sub-commands (use with -h for more info)')

    # minimap2 paf file transform to gtf file
    paf2gtf_args(parser_sub)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()