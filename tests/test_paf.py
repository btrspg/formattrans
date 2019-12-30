#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 24/12/2019 1:05 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : test_paf
# @Software: PyCharm

import unittest
from unittest import TestCase
from fmttrans.paf import Paf
from fmttrans.defaults import paf_elements
from fmttrans.samtag import Samtag


class TestPaf(TestCase):
    def setUp(self):
        self.paf_file = 'tests/test-data/other/trinity.paf'
        self.line = 'TRINITY_DN93842_c0_g1_i1	346	0	345	+	15	101991189	65122294	65122639	336	345	60	tp:A:P	cm:i:94	s1:i:336	s2:i:0	dv:f:0.0021	rl:i:62'
        self.paf = Paf(self.paf_file)
        self.nt = paf_elements(
            query_name='TRINITY_DN93842_c0_g1_i1',
            query_len='346',
            query_start='0',
            query_end='345',
            strand='+',
            target_name='15',
            target_length='101991189',
            target_start='65122294',
            target_end='65122639',
            number_match='336',
            align_block_len='345',
            mapping_quality='60',
            sam_tag=[Samtag('tp:A:P'), Samtag('cm:i:94'), Samtag('s1:i:336'), Samtag('s2:i:0'), Samtag('dv:f:0.0021'),
                     Samtag('rl:i:62')]
        )

    def test_line2elements(self):
        self.assertEqual(self.paf.line2elements(self.line), self.nt, msg='paf elements wrong')

    def test_iter(self):
        for i in self.paf:
            self.assertEqual(i, self.nt, msg='iter+paf elements wrong')
            break

    def test_initial(self):
        with self.assertRaises(FileNotFoundError):
            Paf('file-not-exists.paf')


if __name__ == '__main__':
    unittest.main()
