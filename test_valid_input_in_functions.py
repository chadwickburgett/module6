"""
Program: test_valid_input_in_functions.py
Author: Chadwick Burgett
Last date modified: 06/15/2020

This unittest tests the score_input function of the validate_input_in_function
program. It passes in a string an int and a string of which only the first is
required. It validates the int(test_score) and returns either the test name
and test score or a error message.
"""
import unittest
from more_functions import validate_input_in_functions as vif


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self): #Verifies that the test name is the only required parameter
        self.assertEqual("Test Name: 0", vif.score_input("Test Name"))

    def test_score_valid(self): #Verifies that a valid test score will have a proper return
        self.assertEqual("Test Name: 100", vif.score_input("Test Name", 100))

    def test_score_below_range(self): #Verifies that a below range score will return the error messge
        self.assertEqual('Invalid test score, try again!', vif.score_input("Test Name", -50))

    def test_score_above_range(self): #Verifies that an above range score will return the error messge
        self.assertEqual('Invalid test score, try again!', vif.score_input("Test Name", 150))

    def test_test_score_non_numeric(self): #Verifies that a non numeric score will return the error messge
        self.assertEqual('Invalid test score, try again!', vif.score_input("Test Name", "NOGOOD"))

    def test_score_input_invalid_message(self): #Verifies that an invalid score will return a submitted error messge
        self.assertEqual('Invalid input: Please try again:', vif.score_input("Test Name", "NOGOOD", "Invalid input: Please try again:"))


if __name__ == '__main__':
    unittest.main()
