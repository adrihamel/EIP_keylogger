# This script is a keylogger for educational purposes only.
# Author: adrihamel

'''
This function validates one character by keyboard. If it is a integer, return that number
Otherwise, throw an exception
'''

def validateNumber():
    try:
        num = input("Enter an integer: ")
        if (num == "\x1b1"):
            num = 1
        if (num == "\x1b2"):
            num = 2
        if (num == "\x1b3"):
            num = 3
        if (num == "\x1b4"):
            num = 4
        if (num == "\x1b5"):
            num = 5
        if (num == "\x1b6"):
            num = 6
        return int(num)
    except ValueError:
        print("Error, enter an integer:\n")
        return 0
