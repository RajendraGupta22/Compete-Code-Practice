"""
A space station has solar pannels 
u need to find max ouput pwoer of block of panels
block represnt array and panels are its integer elements
panels could be discharing and leaking power as -1.-2
but ur smart and knows by combining two engative power grid can be converted to positive
write a program to calculate the max power of the block

"""



def solution(xs):
    # Your code here

    result = 1
    neg = []
    pos = []
    if not xs:
        return "0"
    if len(xs)==1 and xs[0]<0:
        return str(xs[0])
    for x in xs:
        if isinstance(x,str):
            x=int(x)
        if x>0:
            pos.append(x)
            result = result * x
        elif x<0:
            neg.append(-x)

    neg = sorted(neg)
    if not len(neg)%2==0:
        neg = neg[1:]
    if not pos and not neg:
        return "0"
    for y in neg:
        result = result * y
    return str(result)

print( "1 : ", solution([-3]) )
print( "2 : ", solution([2,0,2,2,0]) )
print( "3 : ",solution([-3,-2,4,-5]) )
print( "4 : ",solution([0,0,0,-1]) )
