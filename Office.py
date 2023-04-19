"""
space wight between two partion is 2
space betwwen rows is 1
space between adjacent col is 0

find nearest V -  vacant place near Manager M

url : https://github.com/RajendraGupta22/Compete-Code-Practice/blob/main/LAZY%20INTERN%20JAVA%20PROBLEM.docx

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
