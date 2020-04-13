#!/bin/python3
'''
Author: gal davidi
'''

import os
import time
import sys
from docopt import docopt

DEFAULT_SAMPLE_INTERVAL = 60  # 60 sec
DOC_MSG = '''main.
Usage:
  watchdog.py  <path>  <sec>


Options:
  -h --help     Show this screen.
  --version     Show version.

'''


def interval(dir_path, sec=DEFAULT_SAMPLE_INTERVAL):
    old_file_list = []
    while True:
        old_file_list = sample(dir_path, old_file_list)
        time.sleep(sec)


def sample(path, old_ls):
    new_ls = os.listdir(path)
    if not old_ls:
        return new_ls
    elif len(new_ls) > len(old_ls):
        new_files = set(new_ls) - set(old_ls)
        for i in new_files:
            print("New file created: ", i)
        return new_ls
    else:
        return new_ls


def main():
    arguments = docopt(DOC_MSG, help=True, version="1")
    dir_path = arguments['<path>']
    interval_time = int(arguments['<sec>'])
    interval(dir_path, interval_time)


if __name__ == '__main__':
    main()
