#!/bin/python3
'''
Author: gal davidi
'''

import os
import time
import logging
import logging.config

CONSOLE_LOG_CONFIG_FILE_PATH = './conf/console_logger.conf'
CONSOLE_LOGGER_NAME = 'cons_logger'
JSON_LOGGER_NAME = 'json_logger'
JSON_FORMAT_STR = ' "event" : \"{}\" \n "massages" : \"{}\" '

logging.config.fileConfig(CONSOLE_LOG_CONFIG_FILE_PATH)
JSON_logger = logging.getLogger(JSON_LOGGER_NAME)
cons_logger = logging.getLogger(CONSOLE_LOGGER_NAME)


class DirOp:
    def __init__(self, dir_content, time_interval, old_dir_content):
        self.dir_content = dir_content
        self.time_interval = time_interval
        self.old_dir_content = old_dir_content
        self.current_time = time.time()

    def new_file_in_dir(self):
        for i in self.dir_content:
            if os.path.isfile(i) & (self.current_time - os.path.getctime(i) < self.time_interval):  # check if its file and if it was craeted in less than intervsl time
                cons_logger.info(" new file: {}".format(i))
                JSON_logger.info(JSON_FORMAT_STR.format("file creation", "file {} was created".format(i)))

    def new_subdir_in_dir(self):
        for i in self.dir_content:
            if os.path.isdir(i) & (self.current_time - os.path.getctime(i) < self.time_interval):  # check if its dir and if it was craeted in less than intervsl time
                cons_logger.info("new dir: {}".format(i))
                JSON_logger.info(JSON_FORMAT_STR.format("dir creation", " folder {} was created".format(i)))

    def deleted_files(self):
        if self.dir_content < self.old_dir_content:
            deleted_files = set(self.old_dir_content) - set(self.dir_content)
            for i in deleted_files:
                cons_logger.info("file is deleted: {}".format(i))
                JSON_logger.info(JSON_FORMAT_STR.format("file delete", " file {} was deleted".format(i)))
