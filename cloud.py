#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : cloud.py
# Author            : Svtter <svtter@qq.com>
# Date              : 05.02.2018
# Last Modified Date: 24.02.2018
# Last Modified By  : Svtter <svtter@qq.com>
import leancloud
from conf import AppID, AppKey

leancloud.init(AppID, AppKey)

debug = False

if debug:
    import logging
    logging.basicConfig(level=logging.DEBUG)


# class Todo(leancloud.Object):
    # pass

# todo = Todo()

# todo.set('title', '工程师周会')
# todo.set('content', '每周工程师会议')

# todo.save()

def save_word(spell):
    Word = leancloud.Object.extend('Word')
    query = Word.query
    word = Word()

    word_spell = spell
    query.equal_to('spell', word_spell)
    query_list = query.find()

    if query_list:
        res = query_list[0]
        res.increment('count', 1)
        res.fetch_when_save = True
        res.save()
    else:
        word.set('spell', word_spell)
        word.set('count', 1)
        word.save()
