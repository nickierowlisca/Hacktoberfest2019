from __future__ import print_function #for  python version 2. users
import numpy as np 

# function printcheckboard to print Checkerboard pattern 

def printcheckboard(num):
    print("Checkerboard pattern: ")
   
   # create a n * n matrix using np .zeros
    x = np.zeros((n, n), dtype = int)

    # fill with 1 the alternate rows and columns
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1

    # print the pattern line by line
    for i in range(num):
        for j in range(num):
        	print(x[i][j],end=' ')
        print()
# driver code
n=input("Enter an iteger value :")
printcheckboard(n)
