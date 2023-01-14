from itertools import combinations
from typing import List

def compute( a:List, _sum:int )-> List:
	result  = []
	for _range in range(1, len(a)):
		_combination = combinations( a, _range )
		result.extend( filter( lambda x:sum(x)==_sum , _combination ) )
	return result



a = [1,2,3,4,5,6]
_sum = 4
z = compute(a,_sum)
print(z)