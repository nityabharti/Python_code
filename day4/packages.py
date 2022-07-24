def ping(n):
    if (n%2==0):
        return True
    return False    

def printing(num):
    val=ping(num)
    if (val==True):
        print("Number is even")
    else:
        print("Number is odd")    

number = int(input())
printing(number)


       #  PACKAGES  #

import math
print (math.pi) 

from math import *
print(pi)
print(tau)
print(factorial(5))
print(ceil(8.9))
print(floor(8.9))

