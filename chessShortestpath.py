import numpy as np
import sys

class Node:
    def __init__(self, row, col, dist=0 ):
        self.row = row
        self.col = col
        self.dist = dist

class Knight:
    def __init__(self, row, col ):
        self.row = row
        self.col = col        
        
def generateGraph():
    count = 0
    result = []
    for row in range(8):
        temp = []
        for col in range(8):
            temp.append(count)
            count+=1
        result.append(temp)
    return result 

def nodeIsValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)

def solution( strt_int, end_int ):
    data_graph = generateGraph()
    N = len( data_graph )
    np_graph = np.array( data_graph )
    start_src = np.argwhere( np_graph == strt_int )[0]
    start_src = start_src[0],start_src[1]
    # destn and end point of src 
    end_src = np.argwhere( np_graph == end_int )[0]
    end_src = end_src[0],end_src[1]
    visitedNodes = set()
    queue = []
    # possible pos knight can walk is 8 as
    knightMoves = [
            Knight(2,-1), Knight(2,1), Knight(-2,1),Knight(-2,-1),
            Knight(1,2),Knight(1,-2),Knight(-1,2),Knight(-1,-2),
    ]
    node = Node(*start_src)
    end_node = Node(*end_src)
    queue.append( node )
    
    while queue:
        obj = queue[0]
        queue.pop(0)
        if obj.row == end_node.row and obj.col == end_node.col:
            return obj.dist
        if obj not in visitedNodes:
            visitedNodes.add( obj )    
            for km in knightMoves:
                nrow = obj.row + km.row
                ncol = obj.col + km.col
                if nodeIsValid( nrow, ncol, N):
                    queue.append( Node( nrow, ncol, obj.dist+1 ) )
    return "infinite"



# z=solution(19,36)
z=solution(0,1)
print("z : ",z)