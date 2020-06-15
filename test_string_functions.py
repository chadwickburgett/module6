"""
Program: test_string_functions.py
Author: Chadwick Burgett
Last date modified: 06/15/2020

This unittest tests the multiply_string function of the
string_function program. It passes in a string and an int and checks
if the function correctly multiplies them.
"""
import unittest
from more_functions import string_functions as sf

class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual("HIHIHI", sf.multiply_string("HI",3))
        self.assertEqual("PythonPython", sf.multiply_string("Python",2))
        self.assertEqual("ByeByeByeByeByeByeByeByeBye", sf.multiply_string("Bye",9))


if __name__ == '__main__':
    unittest.main()
