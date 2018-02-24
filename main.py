#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : main.py
# Author            : Svtter <svtter@qq.com>
# Date              : 24.02.2018
# Last Modified Date: 24.02.2018
# Last Modified By  : Svtter <svtter@qq.com>

import json
from time import time
from clip import Recorder
from cloud import save_word as save_cloud
import conf
import os
from tinydb import TinyDB, Query
db = TinyDB('db.json')

content = None
directory = conf.directory


# TODO: untested
def save_local_db(word):
    """
    save word in TinyDB
    """
    start = time()
    word_query = Query()
    word_item = db.search(word_query.spell == word)

    if word_item:
        count = word_item[0]['count']
        db.update({'count': count+1}, word_query.spell == word)
    else:
        db.insert({'spell': word, "count": 1})

    stop = time()
    print('cost', str(stop-start), 's')


def save_local(word):
    """
    save word in local json file
    """
    start = time()
    global content

    if os.path.exists(directory):
        with open(directory, 'r') as dic:
            content = json.load(dic)
            print('origin: ', content)
    else:
        content = {}

    with open(directory, 'w') as dic:
        if word:
            content[word] = content.get(word, 0) + 1
            print('dump: ', content)
            json.dump(content, dic)

    stop = time()
    print(str(stop-start) + "秒")


if __name__ == '__main__':
    r = Recorder()
    if conf.cloud:
        r.save_word = save_cloud
    else:
        r.save_word = save_local
    r.run()
