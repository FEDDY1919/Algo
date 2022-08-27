import numpy as np
from constants import *
from robot import Robot

class Maze:
    def __init__(self):
        self.grid = [['.' for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]
        self.robot = Robot(18,2,Direction.TOP)
        
    def setObstacles(self,obstacles):
        for ob in obstacles: # Set Obstacles
            self.grid[ob[0]][ob[1]] = 'X'
    
    def posIsObstacle(self,r,c):
        try:
            return self.grid[r][c] == 'X'
        except IndexError:
            return False
        
    def posIsValid(self,r,c):
        try:
            return self.grid[r][c]
        except IndexError:
            return False
        
    def draw(self):
        print(np.matrix(self.grid))
    
    def setWayPoints(self,ob):
        if(ob[0]-3 <GRID_ROWS and ob[2] == Direction.TOP): # Create all waypoints if possible
            self.grid[ob[0]-3][ob[1]] = 'v'
            return [ob[0]-3,ob[1],Direction.BOTTOM] # Waypoint Co-ordinate + Orientation of Car

        if(ob[1]+3 >= 0 and ob[2] ==  Direction.RIGHT):
            self.grid[ob[0]][ob[1]+3] = '<'
            return [ob[0],ob[1]+3,Direction.LEFT]

        if(ob[0]+3 >= 0 and ob[2] == Direction.BOTTOM):
            self.grid[ob[0]+3][ob[1]] = '^'
            return [ob[0]+3,ob[1],Direction.TOP]

        if(ob[1]-3 <GRID_COLUMNS and ob[2] == Direction.LEFT):
            self.grid[ob[0]][ob[1]-3] = '>'
            return [ob[0],ob[1]-3,Direction.RIGHT]

    def validateRobotPos(self,robot_centre):
        r_c,c_c = robot_centre
        for r in range(r_c-1,r_c+2):
            for c in range(c_c-1,c_c+2):
                if(not self.posIsValid(r,c) or self.posIsObstacle(r,c)):
                    return False
        return True
