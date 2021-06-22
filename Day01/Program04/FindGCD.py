'''
    4.	Program to Find HCF or GCD
'''
import sys

class InputInvalid(Exception):
   pass

try:
    #get input from command line
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    if(num1 <=0 or num2 <= 0):
        raise InputInvalid

    #if first number is less than second, swap
    if(num2 > num1):
        num1,num2 = num2,num1

    #Eucledian Algorithm to find GCD
    while(num2 != 0):
        temp = num1 % num2
        num1 = num2
        num2 = temp
    print("GCD: ", num1)
    
except InputInvalid:
    print("Input is invalid")    
except ZeroDivisionError:
    print("Division By Zero")
except ValueError:
    print("Enter a valid integer")
except IndexError:
    print("Give two numbers")
