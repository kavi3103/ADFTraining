'''
   5.	Program to Convert Decimal to Binary, Octal and Hexadecimal
'''

import sys

class InputInvalid(Exception):
   pass

def convert_to_Base(num,base):
    '''
       input : decimal number and base(2,8,16)
       output: converted string
    '''

    output=""
    while(num != 0):
        rem = num % base
        # if rem > 9 convert to 'A' ,'B', 'C', 'D', 'E', 'F' for  Hexadecimal
        if(rem > 9):
           output = chr(rem+55) + output
        else:
            output = str(rem) + output
        num //= base
    return output

#main
try:
    num = int(sys.argv[1])
    if(num < 0):
         raise InputInvalid 
    print("Binary: ", convert_to_Base(num, 2))  #Binary Conversion
    print("Octal: ", convert_to_Base(num, 8))   #Octal Conversion
    print("HexaDecimal: ",convert_to_Base(num,16))   #HexaDecimal Conversion
except InputInvalid:
    print("Input is invalid")
except IndexError:
    print("Enter a number as command line argument")
except ValueError:
    print("Enter a valid Decimal Number")

