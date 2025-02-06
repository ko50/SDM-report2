#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample01 (self):
                self.assertEqual (21, calc(3, 7))
        def test_sample02 (self):
                self.assertEqual (-1, calc(0, 150))
        def test_sample03 (self):
                self.assertEqual (-1, calc('a', 'b'))
        def test_sample04 (self):
                self.assertEqual (-1, calc(0.1, 999))

        def test_sample05 (self):
                self.assertEqual (1, calc(1, 1))
        def test_sample06 (self):
                self.assertEqual (999, calc(999, 1))
        def test_sample07 (self):
                self.assertEqual (999, calc(1, 999))
        def test_sample08 (self):
                self.assertEqual (998001, calc(999, 999))
        
        def test_sample09 (self):
                self.assertEqual (-1, calc(0, 1))
        def test_sample10 (self):
                self.assertEqual (-1, calc(1, 0))
        def test_sample11 (self):
                self.assertEqual (-1, calc(0, 0))
        
        def test_sample12 (self):
                self.assertEqual (-1, calc(1000, 1))
        def test_sample13 (self):
                self.assertEqual (-1, calc(1, 1000))
        def test_sample14 (self):
                self.assertEqual (-1, calc(1000, 1000))
        
        def test_sample15 (self):
                self.assertEqual (-1, calc(1.5, 20))
        def test_sample16 (self):
                self.assertEqual (-1, calc(10, 2.5))
        def test_sample17 (self):
                self.assertEqual (-1, calc(1.5, 2.0))
        
        def test_sample18 (self):
                self.assertEqual (-1, calc("hoge", 20))
        def test_sample19 (self):
                self.assertEqual (-1, calc(10, "hoge"))
        def test_sample20 (self):
                self.assertEqual (-1, calc("hoge", "hoge"))
        
        def test_sample21 (self):
                self.assertEqual (-1, calc(None, 20))
        def test_sample22 (self):
                self.assertEqual (-1, calc(10, None))
        def test_sample23 (self):
                self.assertEqual (-1, calc(None, None))

