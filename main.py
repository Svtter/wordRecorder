#!/usr/bin/env python

import json
from time import time
from clip import Recorder
import conf
import os

content = None
directory = conf.directory

def save_word(word):
    """

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
    r.save_word = save_word
    r.run()
