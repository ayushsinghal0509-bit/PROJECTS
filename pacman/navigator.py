from maze import *
from exception import *
from stack import *
from copy import deepcopy
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION 
        self.navigatorgrid = deepcopy(grid.gridrep)
        self.m = len(grid.gridrep)
        self.n = len(grid.gridrep[0]) 
    def base_check(self,start,end):
        startx = start[0] 
        starty = start[1]
        endx =   end[0] 
        endy = end[1]
        if(startx < 0 or starty < 0 or endx >= self.m or endy >= self.n):
            raise PathNotFoundException
        if((self.navigatorgrid[startx][starty] == 1) or (self.navigatorgrid[endx][endy] == 1)):
            raise PathNotFoundException
    def valid_cell(self,x,y):
        if(x < 0 or y < 0 or x >= self.m or y >= self.n):
            return False                        
        if(self.navigatorgrid[x][y] == 0):
            return True 
        else:
            return False
    def find_path(self, start , end) :
        # IMPLEMENT FUNCTION HERE 
        self.base_check(start,end)         
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        s = Stack()
        s.push(start)
        path = []
        while(s):
            cur_cell = s.top()
            s.pop()
            path.append(cur_cell)
            if(cur_cell == end):
                return path
            cur_x = cur_cell[0]
            cur_y = cur_cell[1]
            if(self.navigatorgrid[cur_x][cur_y] == 0):
                any_valid = False
                for dx, dy in directions:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if self.valid_cell(next_x, next_y):
                        s.push((next_x, next_y))
                        any_valid = True
                        
                if not any_valid:
                    self.navigatorgrid[cur_x][cur_y] = -1
                    path.pop()
                else:
                    self.navigatorgrid[cur_x][cur_y] = 1
        raise PathNotFoundException
