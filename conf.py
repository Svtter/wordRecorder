#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : conf.py
# Author            : Svtter <svtter@qq.com>
# Date              : 24.02.2018
# Last Modified Date: 24.02.2018
# Last Modified By  : Svtter <svtter@qq.com>
# coding: utf-8

import os
try:
    import conf_example
except BaseException as e:
    print('Error with AppID, AppKey.')

AppID = conf_example.AppID
AppKey = conf_example.AppKey
cloud = True
home = os.environ['HOME']
directory = home + '/Config/word.json'
