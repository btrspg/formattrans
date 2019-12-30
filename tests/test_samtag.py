#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 30/12/2019 12:25 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : test_samtag
# @Software: PyCharm

import unittest
from unittest import TestCase
from fmttrans.samtag import Samtag

class TestSamtag(TestCase):
    def setUp(self):
        self.st = Samtag('tp:A:P')

    def test_equal(self):
        self.assertEqual(self.st,Samtag('tp:A:P','test'))
        self.assertNotEqual(self.st,Samtag('tp:A:S','test'))


