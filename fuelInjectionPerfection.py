"""
Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the 
LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in 
a bit of sabotage while you're at it -- so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP 
each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. 
You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter 
pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number 
of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display 
a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP 
each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. 
You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter 
pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of 
operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a 
number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

-- Java cases --
Input:
Solution.solution('4')
Output:
    2

Input:
Solution.solution('15')
Output:
    5
"""
class Node:
    def __init__(self,n,count=0) -> None:
        self.no = n
        self.count = count

def solution_optimise(n):
    n=int(n)
    x =0
    count = 0
    while n>1:
        count+=1
        print(count," > ",n)
        if (n&1)==0:
            n >>= 1
        elif (n&3) ==1 or n==3:
            n-=1
        else:
            n+=1
        x+=1
    return x     

    

def solution3(n):
    """
        not optimal fails for integer larger than 19 or more digits
    """
    n = int(n)
    if n<=0:return 0
    if n<=2:return n-1
    # q = queue.deque()
    q = []
    node = Node(n)
    q.append(node)
    min = None
    count = 0
    while q:
        N = q[0]
        q.pop(0)
        val = N.no
        count +=1
        print(count," => ",val," count : ",N.count)
        if val == 1:
            if min is None:
                min = N.count
            return min
        elif val%2 == 0:
            q.append( Node( val//2,N.count+1 ) )
        else:
            cc = N.count+1
            max_no = val+1 # since intial was odd , this will be even
            min_no = val-1 # since intial as odd this will bbe even with -1
            if (min_no//2)%2==0 or val==3:
                q.append( Node( val-1,cc) )
            else:        
                q.append( Node( val+1,cc) )
    return min    




def sol(n:int)->int:
    if not  isinstance(n,int):
        raise Exception("Integer Value required.")
    count = 0
    while n>1:
        if n%2==0:
            n = n//2
        else:
            # means no is odd, convert it to even , ways addone OR minusOne
            add_no = n+1
            sub_no = n-1   
            if ((sub_no//2)%2 ==0) or n==3:
                n = sub_no
            else:
                n =add_no    
        count+=1    
    return count    