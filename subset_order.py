
from itertools import combinations

def subSort(z):
    z=list(z)
    z = sorted(z,key=lambda x:(sum(x),-len(x)))
    return z


def subset(a):
    result = []
    for x in range(len(a)+1):
        c = list(combinations(a,x))
        for _i in c:
            result.append( list(_i) )
    return result

a = [1,2,3]
d = subset(a)
r = subSort(d)
print("subsort : ",r)
print("suset :",d)
