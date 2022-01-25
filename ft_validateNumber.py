# This script is a keylogger for educational purposes only.
# Author: adrihamel

'''
This function validates one character by keyboard. If it is a integer, return that number
Otherwise, throw an exception
'''

def validateNumber():
    try:
        return int(input("Enter an integer: "))
    except ValueError:
        print("Error, enter an integer:\n")
