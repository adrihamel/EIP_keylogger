# This script is a keylogger for educational purposes only.
# Author: adrihamel

'''
Function to delete a file passed by parameter
If the file exists, delete it. If not, throw an exception and return to the menu
'''

from os import remove
import os

def deleteFile(arg):
    value = False
    try:
        value = os.path.exists(arg)
        if value == True:
            remove(arg)
            print("The file has been successfully deleted\n")
        else:
            print("Error, the file does't exist so it cannot be deleted\n")
    except FileNotFoundError:
            menu()
