'''
 6.	Program to Find ASCII Value of Character.
'''

import sys
#user defined exception if it is not a character
class NotACharacter(Exception):
    pass

try:
    char = sys.argv[1]
    # if it is not a character raise exception
    if(len(char) != 1):
        raise NotACharacter
    print("Ascii value of ",char," is ",ord(char)) #prints ascii value

except NotACharacter:
    print("Enter a valid Character")

except IndexError:
    print("Enter a character as command line argument")

