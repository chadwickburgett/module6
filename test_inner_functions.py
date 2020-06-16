"""
Program: test_inner_functions.py
Author: Chadwick Burgett
Last date modified: 06/15/2020

This unittest tests the measurements function in the inner_functions_assignment
program.
"""
import unittest
from more_functions import inner_functions_assignment as ifa

class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self): #This tests for two inputs
        self.assertEqual("Perimeter = 11.0 Area = 7.14", ifa.measurements([2.1, 3.4]))

    def test_measurements_square(self): #This tests for one input
        self.assertEqual("Perimeter = 14.0 Area = 12.25", ifa.measurements([3.5]))


if __name__ == '__main__':
    unittest.main()
