# This script is a keylogger for educational purposes only.
# Author: adrihamel

'''
Function to read the credentials.txt file in read mode and display its content
If it exists, it returns the content. If not, throw an exception and return to the menu
'''
import os

def readCredentials():
    value = False
    try:
        value = os.path.exists("credentials.txt")
        if value == True:
            with open("credentials.txt","r") as file:
                for line in file:
                    print(line)
        else:
            print("Error, the file does not exist\n")
    except FileNotFoundError:
        menu()

'''
Function to read the keylog.txt file in read mode and display its content
If it exists, it returns the content. If not, throw an exception and return to the menu
'''

def readLogs():
    value = False
    try:
        value = os.path.exists("keylog.txt")
        if value == True:
            with open("keylog.txt","r") as file:
                for line in file:
                    print(line)
        else:
            print("Error, the file does not exist\n")
    except FileNotFoundError:
        menu()

