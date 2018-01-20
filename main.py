#!/usr/bin/env python

import json
from time import time
from clip import Recorder
import conf

content = None
directory = conf.directory

def save_word(word):
    """

    """
    start = time()
    global content
    with open(directory, 'w+') as dic:
        content = dic.read()
        if content == '':
            content = '{}'
        content = json.loads(content)

        if word:
            content[word] = content.get(word, 0) + 1
            dic.write(json.dumps(content))

    stop = time()
    print(str(stop-start) + "秒")



if __name__ == '__main__':
    r = Recorder()
    r.save_word = save_word
    r.run()
