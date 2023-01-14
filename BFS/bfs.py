"""
graph  description :
0 --> 1,2
1 --> 2
2 --> 0,3
3 --> 3

"""
from collections import defaultdict,OrderedDict
from typing import List,Dict,Union
from collections import deque
from copy import deepcopy

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visted = OrderedDict()

    def createGraph( self, node:Union[str,int], near_elems:List):
        self.graph[node].extend(near_elems)
        self.visted[node] = False

def bfs( source, graph, visited ):
    
    visited = deepcopy(visited)
    Q = deque()
    Q.append( source )
    visited[ source ] = True
    while Q:
        s = Q.popleft()
        print(s,end=" ")
        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in graph[s]:
            if visited[i] == False:
                Q.append(i)
                visited[i] = True

# g.BFS(2)    
# bfs(2)            
