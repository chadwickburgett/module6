"""
Program: inner_functions_assignment.py
Author: Chadwick Burgett
Last date modified: 06/15/2020

This program calls a function and passes a list as a parameter.
That function has two inner functions that calculate the area and
perimeter with the numbers in the list.
"""
def measurements(measure):
    """This function accepts a list of floats and passes them to two inner function that
    calculate the area and perimeter of the floats.
    :param measure: This is a list that contains the floats for calculations
    :return This returns a string that contains the area and perimter calculations"""
    def area(a_list):
        """This function accepts a list of floats and checks the length to see if its one
        or two it then calculates the area based on the length
        :param a_list: This is a list that contains the floats for calculations
        :return This returns a float of the area calculations"""
        length = len(a_list)
        if length == 2:
            return a_list[0] * a_list[1]
        else:
            return a_list[0] * a_list[0]

    def perimeter(a_list):
        """This function accepts a list of floats and checks the length to see if its one
        or two it then calculates the perimeter based on the length
        :param a_list: This is a list that contains the floats for calculations
        :return This returns a float of the perimeter calculations"""
        length = len(a_list)
        if length == 2:
            return (a_list[0]*length) + (a_list[1] * length)
        else:
            return a_list[0] * 4
    a = area(measure) #This calls and sets the area calculations
    p = perimeter(measure) #This calls and sets the perimeter calculations
    return "Perimeter = " + str(p) + " Area = " + str(a) #This is the formatted string return.

if __name__ == '__main__':
    print(measurements([3.5])) #This calls and prints the function
