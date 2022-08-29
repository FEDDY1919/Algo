import numpy as np
from constants import *
from position import Position,RobotPosition


class Maze:
    def __init__(self):
        self.grid = self.generate_grid()
  
    
    def generate_grid(self):
        grid = []
        for r in range(GRID_ROWS):
            arr = []
            for c in range(GRID_COLUMNS):
                arr.append(Position(r,c))
            grid.append(arr)
        return grid

        
    def setObstacles(self,obstacles):
        for ob in obstacles: # Set Obstacles
            self.grid[ob[0]][ob[1]].isObstacle = True
    
    def posIsObstacle(self,r,c):
        try:
            return self.grid[r][c].isObstacle
        except IndexError:
            return self.grid[r][c].isObstacle
        
    def posIsValid(self,r,c):
        try:
            return self.grid[r][c]
        except IndexError:
            return False
        
    def draw(self):
        print(np.matrix(self.grid))
    
    def get_target_pos(self,ob):
        waypoints = []

        for o in ob:
            if o[2] == Direction.TOP and o[0] - 3 > 0:
                waypoints.append(RobotPosition(o[0]-3,o[1],Direction.BOTTOM)) 
            elif o[2] == Direction.BOTTOM and o[0] + 3 < GRID_ROWS:
                waypoints.append(RobotPosition(o[0]+3,o[1],Direction.TOP)) 
            elif o[2] == Direction.LEFT and o[1] - 3 > 0:
                waypoints.append(RobotPosition(o[0]-3,o[1],Direction.RIGHT)) 
            elif o[2] == Direction.RIGHT and o[1] + 3 < GRID_ROWS:
                waypoints.append(RobotPosition(o[0]-3,o[1],Direction.LEFT)) 

        return waypoints



