#!/usr/bin/python

__author__ = 'svtter'

import time
import re
import pyperclip



class Recorder:

    def __init__(self):
        self.pattern = re.compile(r'^[a-zA-Z]+$')
        self.pre = pyperclip.paste()
        self.counter = 1
        self.save_word = self.save_example

    def event_change(self, pbstring):
        """
        clipboard change
        """
        # print u"Pastboard string: %s".encode("utf-8") % repr(pbstring)
        print(pbstring)
        word = self.pattern.match(pbstring)
        if word:
            # print('match.....')
            word = word.group(0)
            self.save_word(word)


    def run(self):
        """
        detect if clipboard content change
        """
        while True:
            time.sleep(self.counter)
            if self.pre != pyperclip.paste():
                self.pre = pyperclip.paste()
                self.pbstring = self.pre
                self.event_change(self.pbstring)


    def save_example(self, word):
        print('Word saved. Saved word is: ', word)


if __name__ == '__main__':
    """
    use for test
    """

    print('clip running...')
    r = Recorder()
    r.run()
