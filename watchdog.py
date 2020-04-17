#!/bin/python3
'''
Author: Gal Davidi
'''

import os
import sys
import time
import signal
from docopt import docopt

from dir_op import DirOp

DEFAULT_SAMPLE_INTERVAL = 60  # 60 sec
DOC_MSG = '''main.
Usage:
  watchdog.py  <path>  <sec> <logfile_path>


Options:
  -h --help     Show this screen.
  --version     Show version.

'''


def interval(dir_path, sec=DEFAULT_SAMPLE_INTERVAL):
    old_file_list = []
    while True:
        old_file_list = sample(dir_path, old_file_list, sec)
        time.sleep(sec)


def sample(path, old_ls, sec):
    new_ls = os.listdir(path)
    if not old_ls:
        return new_ls
    else:
        watch_dir = DirOp(os.listdir(path), sec, old_ls)
        watch_dir.new_file_in_dir()
        watch_dir.new_subdir_in_dir()
        watch_dir.deleted_files()
        return new_ls


def sig_handler(signum, frame):
    while True:
        ans = input("are you shure you want to exit? (y/n)")
        if ans == 'y':
            sys.exit(0)
        elif ans == 'n':
            return


def main():
    signal.signal(signal.SIGINT, sig_handler)
    arguments = docopt(DOC_MSG, help=True, version="1")
    dir_path = arguments['<path>']
    interval_time = int(arguments['<sec>'])
    logfile_path = arguments['<logfile_path>']
    interval(dir_path, interval_time)


if __name__ == '__main__':
    main()
