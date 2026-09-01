class Maze:
    def __init__(self, m: int, n : int) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.gridrep = []
        for _ in range(m):
            row = [0 for _ in range(n)]
            self.gridrep.append(row)
    
    def add_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        self.gridrep[x][y] = 1
    def remove_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        self.gridrep[x][y] = 0
    def is_ghost(self, x : int, y: int) -> bool:
        # IMPLEMENT YOUR FUNCTION HERE
        return self.gridrep[x][y] == 1
        # return False
    def print_grid(self) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        m = len(self.gridrep)
        n = len(self.gridrep[0])
        for row in range(m):
            for col in range(n):
                print(self.gridrep[row][col],end = " ")
            print("")
        # return False
