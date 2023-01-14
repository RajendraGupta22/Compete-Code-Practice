from itertools import combinations

def solution2(l):
    # Your code here
    l =sorted(l)
    temp = combinations(l,3)
    result = []
    for x in temp:
        if validTriples(x):
            result.append(x)
    return len( list(result) )

def validTriples(arr):
    x,y,z = 0,1,2
    return arr[y]%arr[x]==0 and arr[z]%arr[y]==0    

def rtriple(iterable):
    return set((x,y,z)
        for x,y,z in combinations(sorted(iterable),3) if y%x==0 and z%y==0
        )
    