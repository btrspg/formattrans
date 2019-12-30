#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 30/12/2019 12:01 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : samtag
# @Software: PyCharm

from fmttrans.defaults import samtag_description


class Samtag:
    def __init__(self, samtag, description=None):
        self.tag, self.type, self.value = samtag.split(':')
        if description:
            self.description = description
        elif self.tag in samtag_description:
            self.description = samtag_description[self.tag]
        else:
            self.description = 'samtag need description'

    def __eq__(self, other):
        return self.tag == other.tag and self.type == other.type and self.value == other.value

    def __str__(self):
        return self.tag

    def __repr__(self):
        return self.tag, self.type, self.value, self.description
