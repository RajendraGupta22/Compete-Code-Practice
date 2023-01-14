"""
In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. 
But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of 
passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, 
but only the Commander knows how to figure out which of several lists contains the access codes. 
You need to find a way to determine which list contains the access codes once you're ready to go in. 

Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the 
access codes are "lucky triples" in order to make it easier to find them in the lists. 
A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). 
With that information, you can figure out which list contains the number of access codes that matches the 
number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, 
you'd need to find a list with 5 "lucky triple" access codes).

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" 
of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 
inclusive.  The elements of l are between 1 and 999999 inclusive.  
The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access 
codes to throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], 
making the solution 3 total.
"""

from itertools import combinations
from typing import List

def solution(l):
    # Your code here
    temp = combinations( enumerate(l),3)
    idx_l = combinations(range(len(l)), 23)
    result = []
    for x in temp:
        if validTriples(x):
            result.append(x)
    return len( list(result) )

def validTriples(arr):
    x,y,z = 0,1,2
    i,j,k = arr[x][0], arr[y][0], arr[z][0]
    if i<j<k:
        return arr[y][1]%arr[x][1]==0 and arr[z][1]%arr[y][1]==0
    return False    

def num_triples(l):
    "this is passed and working "
    total = 0
    for mid_i, mid in enumerate(l):
        num_left = sum(1 for x in l[:mid_i] if mid % x == 0)
        print(" num_left : ",num_left)
        num_right = sum(1 for x in l[mid_i+1:] if x % mid == 0)
        print(" num_right : ",num_right)
        total += num_left * num_right
    return total    

# solution2([6,5,4,3,2,1])
# solution2([6,5,4,3,2,1])
# solution( [1,2,3,4,5,6] )
solution( [1,1,1] )
solution( [1,3,2,6,4,2,3,9] )

def news(l):
    trips=0
    doubs = [0]*len(l) 
    for i in range(1, len(l)):
        for j in range(i):
            if l[i]%l[j]==0:
                doubs[i]+=1
                trips+=doubs[j]
    return trips            
