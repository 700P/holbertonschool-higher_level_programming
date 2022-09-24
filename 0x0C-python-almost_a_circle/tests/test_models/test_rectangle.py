#!/usr/bin/python3
""" unittest for rectanle """

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Basictest(unittest.TestCase):
    """ generic setup and close """
    def setUp(self):
        """ imports modules """
        self.basictest = basictest

    def tearDown(self):
        """ cleans up after test """
        self.basictest.dispose()

