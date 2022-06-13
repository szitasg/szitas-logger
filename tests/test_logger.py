# !/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'gabor.szitas.work@gmail.com'

import random
import time
import unittest

from szitas_logger.logger import Logger


class TestLogger(unittest.TestCase):

    LOG_FILE = '.tox/logger.log'

    @classmethod
    def setUpClass(cls):
        Logger(log_file=TestLogger.LOG_FILE)

    def setUp(self):
        self.log = Logger.get_logger()
        self.message = None

        self._generate_message()

    def _generate_message(self):
        self.message = str(random.getrandbits(2048))

    def _read_last_word(self):
        with open(TestLogger.LOG_FILE) as input:
            return input.read()

    def test_debug(self):
        self.log.debug(self.message)
        self.assertTrue(self.message in self._read_last_word())

    def test_info(self):
        self.log.info(self.message)
        self.assertTrue(self.message in self._read_last_word())

    def test_warning(self):
        self.log.warning(self.message)
        self.assertTrue(self.message in self._read_last_word())

    def test_error(self):
        self.log.error(self.message)
        self.assertTrue(self.message in self._read_last_word())

    def test_empty_message(self):
        before = self._read_last_word()
        self.log.debug('')
        self.assertTrue(before == self._read_last_word())

    def test_timer(self):
        wait = 1.5

        self.log.timer_start()
        time.sleep(wait)
        self.log.timer_end()

        self.assertTrue(f'Elapsed time 0:00:{wait:05.2f}'
                        in self._read_last_word())


if __name__ == '__main__':
    unittest.main()
