# This script is a keylogger for educational purposes only.
# Author: adrihamel

'''
This function validates one character by keyboard. If it is a integer, return that number
Otherwise, throw an exception
'''

def validateNumber():
    ok = False
    num = 0
    while (not ok):
        try:
            num = int(input("Enter an integer: "))
            ok = True
        except ValueError:
            print("Error, enter an integer:\n")
    return num