#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 9/1/2020 11:58 AM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : test_paf2gtf
# @Software: PyCharm
import unittest
from unittest import TestCase
from fmttrans.paf2gtf import paf2gtf


class Test(TestCase):
    def setUp(self):
        self.paf_file = './tests/test-data/other/trinity.paf'
        self.gtf_file = './tests/test-data/trinity.gtf'

    def test_paf2gtf(self):
        from collections import namedtuple
        Args=namedtuple('Args',['paf','gtf','mapped_length_rate','mapping_quality','align_identity','tag'])
        args=Args(paf=self.paf_file,
                  gtf=self.gtf_file,
                  mapped_length_rate=0,
                  mapping_quality=0,
                  align_identity=0,
                  tag='test')
        self.assertEqual(paf2gtf(args), True, msg='run work')


if __name__ == '__main__':
    unittest.main()
