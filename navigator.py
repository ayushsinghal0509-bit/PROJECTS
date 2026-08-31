from maze import *
from exception import *
from stack import *
from copy import deepcopy
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION 
        self.grid = deepcopy(grid.grid)
        self.m = len(grid)
        self.n = len(grid[0])
    def base_check(self,start,end):
        startx = start[0] ; starty = start[1]
        endx =   end[0]   ; endy = end[1]
        if(startx < 0 or starty < 0 or endx >= self.m or endy >= self.n):
            raise PathNotFoundException
        if((self.grid[startx][starty] == 1) or (self.grid[endx][endy] == 1)):
            raise PathNotFoundException
    def valid_cell(self,x,y):
        if(x < 0 or y < 0 or x >= self.m or y >= self.n):
            return False                        
        if(self.grid[x][y] == 0):
            return True 
        else:
            return False
    def find_path(self, start , end) :
        # IMPLEMENT FUNCTION HERE 
        self.base_check(start,end)         

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
            if(self.grid[cur_x][cur_y] == 0):
                any_valid = False
                if(self.valid_cell(cur_x-1,cur_y)):
                    s.push((cur_x-1,cur_y))
                    any_valid = True   
                if(self.valid_cell(cur_x+1,cur_y)):
                    s.push((cur_x+1,cur_y))
                    any_valid = True   
                if(self.valid_cell(cur_x,cur_y-1)):
                    s.push((cur_x,cur_y-1))
                    any_valid = True   
                if(self.valid_cell(cur_x,cur_y+1)):
                    s.push((cur_x,cur_y+1))
                    any_valid = True
            if(any_valid is False):
                self.grid[cur_x][cur_y] = -1
                path.pop(cur_cell)
            else:
                self.grid[cur_x][cur_y] = 1
            print(cur_x,cur_y,end = ";")
        raise PathNotFoundException
