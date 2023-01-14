import sys
import numpy as np

class Node:
	def __init__(self, x, y, dist=0):
		self.x = x
		self.y = y
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

def isValid(x, y, N):
	return not (x < 0 or y < 0 or x >= N or y >= N)

def findShortestDistance(src, dest, N):
    knightMoves = [
            Knight(2,-1), Knight(2,1), Knight(-2,1),Knight(-2,-1),
            Knight(1,2),Knight(1,-2),Knight(-1,2),Knight(-1,-2),
    ]
    visited = set()
    # q = deque()
    q= []
    q.append(src)
    while q:
        # node = q.popleft()
        node = q[0]
        q.pop(0)
        x = node.x
        y = node.y
        dist = node.dist
        if x == dest.x and y == dest.y:
            return dist
        if node not in visited:
            visited.add(node)
            for i in knightMoves:
                x1 = x + i.row
                y1 = y + i.col
                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))
    return sys.maxsize



def solution(strt_int,end_int):
    data_graph = generateGraph()
    N= len(data_graph)
    np_graph = np.array( data_graph )
    start_src = np.argwhere( np_graph == strt_int )[0]
    start_src = start_src[0],start_src[1]
    # destn and end point of src 
    end_src = np.argwhere( np_graph == end_int )[0]
    end_src = end_src[0],end_src[1]

    src = Node(*start_src)	# source coordinates
    dest = Node(*end_src) 

    print("The minimum number of steps required is",
		  findShortestDistance( src, dest, N))