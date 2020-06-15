"""
Program: validate_input_in_functions.py
Author: Chadwick Burgett
Last date modified: 06/15/2020

This program takes user input of a test name, score and error message
passes it to a function and returns the test name and score after
validating it.
"""
def score_input(test_name,test_score = 0, invalid_message = 'Invalid test score, try again!'):
   """This function takes in a test name score and error message with only test name being required
    validates the score and then returns the test name and score
    :param test_name: This is the string test name that will be returned, required.
    :param test_score: This is the int that is the score to be returned with test name
    :param invalid_message: This is the messge that will be returned if score is invalid
    :return The string and the integer"""
   try:
    min, max = 0,100
    if min <= test_score <= max:
        return test_name + ": " + str(test_score)
    else:
        return invalid_message
   except:
       return invalid_message

if __name__ == '__main__':
    try:
        print(score_input("Test Name"))
    except:
        print("There has been an error in main.")
