#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 8/1/2020 2:53 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : test_utils
# @Software: PyCharm
import unittest
from unittest import TestCase
from fmttrans.utils import *


class Test(TestCase):
    def test_file_exists(self):
        self.assertEqual(file_exists('./test/not-a-file'), [False], msg='test_file_exists')
        self.assertEqual(file_exists(__file__, __file__), [True, True], msg='test_file_exists')

    def test_merge_regions(self):
        regions = [(1, 2), (2, 3), (7, 9)]
        self.assertEqual(merge_regions(regions), [[1, 3], [7, 9]], msg='merge region wrong')
        regions = [(1, 2), (4, 6), (7, 9)]
        self.assertEqual(merge_regions(regions), [[1, 2], [4, 6], [7, 9]], msg='merge region wrong')

    def test_extract_cg_value(self):
        self.assertEqual(extract_cg_value('1000M137N209M273N85M104N606M2D40M'),
                         [('1000', 'M'), ('137', 'N'), ('209', 'M'), ('273', 'N'), ('85', 'M'),
                          ('104', 'N'), ('606', 'M'), ('2', 'D'), ('40', 'M')],
                         msg='extract cg value wrong')

    def test_align2exons(self):
        tag = '491M115N304M156N323M102N1045M'
        self.assertEqual(align2exons(67173553, 67176089, extract_cg_value(tag), '-'),
                         [[67175044, 67176089], [67174619, 67174942], [67174159, 67174463], [67173553, 67174044]],
                         msg='align2exons error minus ')
        self.assertEqual(align2exons(67173553, 67176089, extract_cg_value(tag)),
                         [[67173553, 67174044], [67174159, 67174463], [67174619, 67174942], [67175044, 67176089]],
                         msg='align2exons error plus ')

        with self.assertRaises(TypeError):
            align2exons(67173553, 67176084, extract_cg_value(tag))



if __name__ == '__main__':
    unittest.main()
