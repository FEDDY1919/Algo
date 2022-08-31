import math
from constants import Direction

from position import RobotPosition
from collections import deque
from straight import StraightCommand
from grid import Grid

class Mod_A_Star:

    def __init__(self,grid,start:RobotPosition,end:RobotPosition):
        self.start = start
        self.end = end
        self.grid = grid

        self.commands = deque() #return the commands needed for the mod A star


    def check_valid_command(self,command,pos:RobotPosition):
        p = pos.copy() #copy original position

        command.apply_on_pos(p) #apply command on the position

        if(self.grid.posIsValid(p)):
            return p

        return None

    def heuristic(self,pos:RobotPosition):
        dx = abs(self.end.c - pos.c)
        dy = abs(self.end.r - pos.r)
        return math.sqrt(dx**2 + dy**2)

    def get_neighbors(self,pos:RobotPosition):

        neighbors = []

        dist = 1

        straightMovement = [
            StraightCommand(dist),
            StraightCommand(-dist)
        ]

        for c in straightMovement:
            after = self.check_valid_command(c,pos)
            if after: 
                neighbors.append((after,dist,c))

        print(neighbors)
        return neighbors

grid = Grid()
test = Mod_A_Star(grid,RobotPosition(18,2,Direction.TOP,90),RobotPosition(4,2,Direction.TOP,90))
pos = RobotPosition(18,2,Direction.TOP,90)
test.get_neighbors(pos)