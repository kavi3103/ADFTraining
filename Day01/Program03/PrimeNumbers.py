'''
    3.	Program to Print all Prime Numbers in an Interval of 5 seconds
'''


import math
import time
def isPrime(num):
    '''
    input: number
    output: true or false
    '''
    if(num != 2 and num % 2 == 0):
        return False
    sqrt = int(math.sqrt(num))
    for i in range(3,sqrt+1,2):
        if(num%i == 0):
            return False
    return True

for i in range(2,100):
    if(isPrime(i)):
        print(i)  # prints prime numbers
        time.sleep(5) # interval of 5 seconds






