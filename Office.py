"""
space wight between two partion is 2
space betwwen rows is 1
space between adjacent col is 0

find nearest V -  vacant place near Manager M

"""

""""
	LAZY INTERN  PROBLEM

Deepanshu applied for an internship last month and went through multiple rounds. After all this process, he got selected for the internship and is very excited. He went to the office happily and received the orientation. He got to know that he will be working under the Tech Manager. On the first day at the office, he realized that he has to walk a lot as there are a lot of discussions required and meetings are set every now and then. The manager's cubicle M is located far from where he is seated and he has to take a long path to reach him and he is very lazy for this.
The office is divided into two partitions and is separated by space between them. There are N rows of cubicles with four cubicles in each row of partition. All the vacant cubicles are marked with V and all the occupied cubicles are marked with O. There is a distance of one unit between the two rows of cubicles and there is a distance of two units between the two partitions. Between the cubicles in a row of a partition, there is no space or distance.
A representation of the office is provided below with 8 rows of cubicles.

Deepanshu is very lazy and he wants to cover as minimum as possible distance to reach the Manager's row in the partition where Manager's cubicle M is located. The limitation is that the movement can be only horizontally or vertically. Deepanshu wants to know the minimum distance he has to cover to reach the Manager's row in the partition where Manager's cubicle M is located and he will figure out the vacant cubicle on his own. He is busy with the work and needs your help to determine the minimum distance he has to cover. Can you help him?


Input Format
The first line of input consists of a single integer N, representing the number of rows in the office.
Next N lines contain the representation of the view plan of cubicles in the office.

Note: Space between partitions is represented with space at the location.


Constraints
1<= N <=1000

Output Format
Print the required output in a separate line.

Sample TestCase 1
Input
8
OOOO OOOM
OVOO OOOO
OOVO OOVO
OOOO OOOO
OOOO OOOO
OOOO OOOO
OOOO OOOO
OOOO VOOO
Output
2
Explanation
The office representation is as below:



There are 4 Vacant Cubicles in the office, located at positions [(2,2), (3,3), (3,7) and (7,5)].
The minimum distance Deepanshu has to cover is 2 units which is possible from the vacant cubicle located at position (3, 7). He can move 2 units vertically and make it to the Manager. Thus, the output is 2.
Time Limit(X):
0.50 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:



"""


from typing import List,Dict,DefaultDict
import math

class Node:
    def __init__(self,row,col,elm) -> None:
        self.elm = elm
        self.row = row
        self.col = col

class ShortesSlot:
    class CONSTANT:
        def __init__(self) -> None:
            self.VACANT = "V"
            self.MANAGER = "M"
    def __init__(self) -> None:
        self.CONSTANT =  self.CONSTANT()

    def main(self, *args,**kwargs):
        if args or kwargs:
            nRow = kwargs['nRow']
            _map = kwargs['map'].strip().split('\n')
            _map = [ _m.strip() for _m in _map]
        else:
            nRow = int( input("Enter no of Rows \n") )
            _map = [ list(input()) for _r in range(nRow) ]
        print("No of Rows : ",nRow)    
        print("The graph of Matix PLot : ")
        self.display(_map)    
        vacant,manager = self.computeNodes(_map) 
        print("process to find shortest distance ..")
        check_small = math.inf
        _short_node = []
        for _source in vacant:
            _dist = self._findShortDist( _source,manager[0])
            if _dist < check_small:
                check_small = _dist
                _short_node = [ _source.__dict__ ]
        print("final result is ..")
        if _short_node:
            print(f" min dist : {check_small} \n vacant seat : {_short_node[0]} \n manager seat : {manager[0].__dict__} ")
        else:
            print("Unable to finc vacant place.")

    def _findShortDist( self, start_node, end_node):
        # 0-3 if source and Dest inside now space partion to add else add
        # 5-8 if source and Dest inside now space partion to add else add
        extra_space = 0
        if start_node.col in range(0,3+1) and end_node.col in range(0,3+1):
            pass
        elif start_node.col in range(5,8+1) and end_node.col in range(5,8+1):
            pass
        else:
            extra_space = 2
        _row_space = abs( end_node.row - start_node.row )
        result = extra_space+_row_space
        return result
    
    def computeNodes(self,arry:List):
        _visted = []
        _manager = []
        for _row,_i in enumerate(arry):
            for _col,_sub in enumerate(_i):
                if _sub == self.CONSTANT.VACANT:
                    _visted.append( Node(row=_row,col=_col,elm=_sub) )
                elif _sub == self.CONSTANT.MANAGER:
                    _manager.append( Node(row=_row,col=_col,elm=_sub) )
        return _visted,_manager

    @staticmethod
    def display( arry:List ):
        [ print(" ".join(list(_item))) for _item in arry ]

if __name__=="__main__":
    z= """
        OOOO OOOM
        OVOO OOOO
        OOVO OOVO
        OOOO OOOO
        OOOO OOOO
        OOOO OOOO
        OOOO OOOO
        OOOO VOOO
    """

    N= 8
    data = {"nRow":N, 'map':z}
    ShortesSlot().main(**data)
