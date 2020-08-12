#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : nav upd.py
@Time    : 2020/5/25 12:49
@Author  : Shek
@Version : 1.0
@Contact : vflanker@163.com
@License : (C)Copyright 2020-2021, Shek Innovation
@Desc    : An automatic generator for Html5/CSS/Javascript Home Navigation
"""

# here put the import lib
from libs.navupd import H5Navigation

h5 = H5Navigation()
h5.set_verbose(False)
h5.set_head_title('THIS IS HEAD TITLE')
h5.set_main_title('THIS IS MAIN TITLE')
h5.set_sub_title('THIS IS SUB TITLE')
navigations_data = [
    ['WEB1'], ['WEB2'], ['WEB3']
]
h5.set_navigations(navigations_data)
h5.generate()
