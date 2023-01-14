
from typing import List
import json

class Color:
    black =0
    white =1


def flood_fill(buf, start_x: int, start_y: int, fill_color: Color=None):
    # print(start_x," : ",start_y, " : ",len(buf[0]), " : ",len(buf))
    try:
        if not ( start_x < len(buf) ):
            ed=start_y
            if start_y>len(buf[0]):
                ed = len(buf[0]) - start_y
            flood_fill( buf, len(buf)-start_x, ed )
        if not ( start_y<len(buf[0]) ):
            ex=start_x
            ed = len(buf[0]) - start_y
            if start_x>len(buf):
                ex = len(buf)-start_x
            flood_fill( buf, ex, ed)
        if buf[start_x][start_y] == "x":
            return
        buf[start_x][start_y]='x'
        #checking most recent negbours
        cordinate = [start_x]
        # while cor?
        flood_fill(buf, start_x-1, start_y,)
        flood_fill(buf, start_x+1, start_y)
        flood_fill(buf, start_x, start_y-1)
        flood_fill(buf, start_x, start_y+1)
    except Exception as e:
        return    
        




a= [
# 1   2   3   4   5   6   7   8   9   10 
['.','.','.','x','x','x','x','.','.','.',], #0
['.','x','x','.','.','.','.','x','x','.',], #1
['.','x','x','.','.','.','.','x','x','.',], #2
['.','.','.','x','x','x','x','.','.','.',], #3
] 

def display(d):
    for x in d:print(x)

print('input : \n', display(a))
flood_fill(a,1,4)
# flood_fill(a,0,8)
#flood_fill(a,0,2)

print('out : \n', display(a))

class FloodFill:
    def __init__(self) -> None:
        print("test called .. ")
    def floodFillUtil(self,screen, x, y, prevC, newC):
        M = len( screen )
        N = len(screen[0])
        if x>= M:
            Mx = x-M
            x=Mx
            if Mx >=M:
                return
        if y>=N:
            My = y-N
            y=My
            if My>=N:
                return        
        # Base cases
        if (x < 0-M or y < 0-N or
            screen[x][y] != prevC or
            screen[x][y] == newC):
            return
        # Replace the color at (x, y)
        screen[x][y] = newC

        # Recur for north, east, south and west
        self.floodFillUtil(screen, x + 1, y, prevC, newC)
        self.floodFillUtil(screen, x - 1, y, prevC, newC)
        self.floodFillUtil(screen, x, y + 1, prevC, newC)
        self.floodFillUtil(screen, x, y - 1, prevC, newC)

    # It mainly finds the previous color on (x, y) and
    # calls floodFillUtil()
    def floodFill( self, screen, x, y, newC ):
        prevC = screen[x][y]
        if(prevC==newC):
            return
        self.floodFillUtil(screen, x, y, prevC, newC)


data = [
# 1   2   3   4   5   6   7   8   9   10 
['.','.','.','x','x','x','x','.','.','.',], #0
['.','x','x','.','.','.','.','x','x','.',], #1
['.','x','x','.','.','.','.','x','x','.',], #2
['.','.','.','x','x','x','x','.','.','.',], #3
] 

print("before : \n")
display(data)
print("\n")
print("After : \n")
FloodFill().floodFill( data,0,8,"x" )
display(data)
#flood_fill(a,1,4)
#flood_fill(a,0,8)
#flood_fill(a,0,2)
    
