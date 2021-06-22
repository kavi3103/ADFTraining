'''
    4.	Program to Find HCF or GCD
'''
import sys

try:
    #get input from command line
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    #if first number is less than second, swap
    if(num2 > num1):
        num1,num2 = num2,num1

    #Eucledian Algorithm to find GCD
    while(num2 != 0):
        temp = num1 % num2
        num1 = num2
        num2 = temp
    print("GCD: ", num1)
    
except ZeroDivisionError:
    print("Division By Zero")
except ValueError:
    print("Enter a valid integer")
except IndexError:
    print("Give two numbers")
