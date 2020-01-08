#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 30/12/2019 12:14 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : utils
# @Software: PyCharm

import os
from fmttrans.pattern import cg_tag_pattern
from fmttrans.defaults import fill_namedtuple, region


def file_exists(*filenames):
    return [os.path.exists(filename) for filename in filenames]


def merge_regions(region_list):
    '''
    the region must be sorted from small to big (position)

    :param region_list:
    :return:
    '''
    temp_region = fill_namedtuple(region, [None, None, None])
    new_region_list = []
    for rg in region_list:
        rgn = fill_namedtuple(region, [None, *rg])
        if temp_region.start is None:
            temp_region = rgn
        elif rgn.start <= temp_region.end:
            temp_region = temp_region._replace(end=rgn.end)
        else:
            new_region_list.append([temp_region.start, temp_region.end])
            temp_region = fill_namedtuple(region, [None, *rg])
    new_region_list.append([temp_region.start, temp_region.end])
    return new_region_list


def extract_cg_value(value):
    '''
>>> extract_cg_value('1000M137N209M273N85M104N606M2D40M')
[('1000', 'M'), ('137', 'N'), ('209', 'M'), ('273', 'N'), ('85', 'M'), ('104', 'N'), ('606', 'M'), ('2', 'D'), ('40', 'M')]

    '''
    return cg_tag_pattern.findall(value)


def align2exons(target_start, target_end, samtag_value_list, strand='+'):
    '''

    :param target_start:
    :param target_end:
    :param strand:
    :param samtag_value_list:
    :return:
    '''
    exons = []

    for tag in samtag_value_list:
        length, align_tag = int(tag[0]), tag[1]
        if align_tag == 'M':
            exons.append([target_start, target_start + length])
            target_start += length
        elif align_tag == 'N':
            target_start += length
        elif align_tag == 'D':
            target_start += length
            last_exon = exons.pop()
            last_exon[1] = last_exon[1] + length
            exons.append(last_exon)
        elif align_tag == 'I':
            pass
        else:
            raise ValueError('{} was not one of [MNDI]'.format(align_tag))

    if exons[-1][1] != target_end:
        raise TypeError('Methods err: ' + str(exons[-1][1]) + '!=' + str(target_end))

    exons = merge_regions(exons)

    if strand == '-':
        exons.reverse()
    elif strand not in ['-', '+']:
        raise ValueError('strand can only be -/+ not {}'.format(strand))

    return exons


def mapped_length_rate(pafe):
    '''

    :param pafe:
    :return:
    '''
    return (float(pafe.query_end) - float(pafe.query_start)) / float(pafe.query_length)


def align_identity(pafe):
    '''

    :param pafe:
    :return:
    '''
    return float(pafe.number_match) / float(pafe.align_block_len)


def main():
    regions = [(1, 2), (2, 3), (7, 9)]
    print(merge_regions(regions))
    regions = '491M115N304M156N323M102N1045M'
    print(align2exons(67173553, 67176089, extract_cg_value(regions), '-'))
    print(align2exons(67173553, 67176089, extract_cg_value(regions)))


if __name__ == '__main__':
    main()
