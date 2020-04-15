#!/bin/python3
'''
Author: gal davidi
'''

import os
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')


class DirOp:
    def __init__(self, dir_content, time_interval, old_dir_content):
        self.dir_content = dir_content
        self.time_interval = time_interval
        self.old_dir_content = old_dir_content
        self.current_time = time.time()

    def new_file_in_dir(self):
        for i in self.dir_content:
            if os.path.isfile(i) & (self.current_time - os.path.getctime(i) < self.time_interval):  # check if its file and if it was craeted in less than intervsl time
                logging.info(" new file: {}".format(i))

    def new_subdir_in_dir(self):
        for i in self.dir_content:
            if os.path.isdir(i) & (self.current_time - os.path.getctime(i) < self.time_interval):  # check if its dir and if it was craeted in less than intervsl time
                logging.info("dir: {}".format(i))

    def deleted_files(self):
        if self.dir_content < self.old_dir_content:
            deleted_files = set(self.old_dir_content) - set(self.dir_content)
            for i in deleted_files:
                logging.info("file is deleted: {}".format(i))

