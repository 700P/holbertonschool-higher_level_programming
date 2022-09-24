#!/usr/bin/python3
""" unittest square """
import unittest
from models.base import Base
from models.square import Square

class Basictest(unittest.TestCase):
    """ generic setup and close """
    def setUp(self):
        """ imports modules """
        self.basictest = basictest

    def tearDown(self):
        """ cleans up after test """
        self.basictest.dispose()
        
