from pty import fork
import numpy as np
from typing import List

a= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b= [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

 
def reverseDiagonals(a:List) -> List:
    result = []
    na = np.array(a)
    l = len(a)-1
    nl = -l
    while l>=nl:
        result.extend( na.diagonal(l) )
        l-=1
    return result 

def revDiag(a:List)->List:
    # without numpy
    # print reverse diagonal matrix , range will be +len(a) to -len(a), since for square matrix digonal will be 
    # .. at equal positiona at both ends
    # find its diagonal values  , using iteration with row=0, col = range
    # no diagonal values above zero row so skip row iter for -ve values
    # diagonal elemnts will be row+1,col+1, till boundary of array is reached
    result = []
    l = len(a)-1
    nl = -l
    counter = 0 
    while l>=nl:
        col,row = l,0
        counter +=1
        if col == len(a)-1:
            result.append( a[row][col] )
        else:
            # to optimse if -ve col values start iter from row= -ve cols, col=0
            if col<0:
                row,col = -col,0
            while col<=len(a)-1 and row<=len(a)-1:
                counter +=1
                result.append( a[row][col] )
                row +=1
                col +=1
        l-=1
    return result,counter

def myfunc(matrix):
    # by pradeep , n*n complexity..
    result = []
    n = len(matrix)
    N=n*n
    counter = 0
    for i in range(1,N):
        # print(">>> ",i)
        counter +=1
        for m,j in enumerate( range(-abs(i),0) ):
            # print(m," == ",j)
            counter+=1
            if j>= -abs(len(matrix)) and m<= len(matrix)-1:
                result.append( matrix[m][j] )
    return counter            

def forwardDiagonal(a:List)->List:
    result = []
    na = np.array( a[::-1] )
    l = len(a)-1
    nl = -l
    while nl<=l:
        result.extend( na.diagonal(nl) )
        nl+=1
    return result   

def forwDiag(a:List)->List:
    result = []
    l = len(a) 
    max_index = l-1
    max_iter = l+l-1
    for rowix in range(max_iter):
        row,col = rowix,0
        if rowix > max_index:
            row,col = max_index,rowix-max_index
        while row>=0 and col<=max_index:
            result.append( a[row][col] )
            row -= 1
            col += 1
    return result

def display(a):
    for x in a:print(x)
        


# revDiag(a)
# forwDiag(a)
forwDiag(b)

