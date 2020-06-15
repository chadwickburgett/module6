"""
Program: string_functions.py
Author: Chadwick Burgett
Last date modified: 06/15/2020

This program takes user input of a string and int and
passes it to a function that returns the string the
number of times of the integer that the main then prints
"""
def multiply_string(message,n):
    """This function takes in a string and int and returns the string times the int, ie hi,2 = hihi
    :param message: This is the string that will be returned
    :param n: This is the int that will decide how many times the string is displayed
    :return The string times the integer"""
    return message * n

if __name__ == '__main__':
    phrase = input("Please enter a phrase: ")
    num = int(input("Please enter a number between 1-9: "))
    print(multiply_string(phrase, num)) #Function call and print command
