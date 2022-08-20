import numpy as np
from constants import *

class Maze:
    def __init__(self):
        self.grid = [['.' for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]
        
    def setObstacles(self,obstacles):
        for ob in obstacles: # Set Obstacles
            self.grid[ob[0]][ob[1]] = 'X'
    
    def posIsObstacle(self,r,c):
        try:
            return self.grid[r][c]!='/'
        except IndexError:
            return False
        
    def posIsValid(self,r,c):
        try:
            return self.grid[r][c]
        except IndexError:
            return False
        
    def draw(self):
        print(np.matrix(self.grid))
    
    def setWayPoints(self,obstacles):
        for ob in obstacles:
            if(ob[0]+3 <GRID_ROWS): # Create all waypoints if possible
                self.grid[ob[0]+3][ob[1]] = 'S'
                # waypoints.append([ob[0]+3,ob[1],'N']) # Waypoint Co-ordinate + Orientation of Car
            if(ob[1]-3 >= 0):
                self.grid[ob[0]][ob[1]-3] = 'W'
                # waypoints.append([ob[0],ob[1]-3,'E']) 
            if(ob[0]-3 >= 0):
                self.grid[ob[0]-3][ob[1]] = 'N'
                # waypoints.append([ob[0]-3,ob[1],'S'])
            if(ob[1]+3 <GRID_COLUMNS):
                self.grid[ob[0]][ob[1]+3] = 'E'
                # waypoints.append([ob[0],ob[1]+3,'W'])

    def validateRobotPos(self,robot_centre):
        r_c,c_c = robot_centre
        for r in range(r_c-1,r_c+2):
            for c in range(c_c-1,c_c+2):
                if(not self.posIsValid(r,c)):
                    return False
        return True
