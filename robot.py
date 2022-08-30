from constants import Direction
from position import RobotPosition
from constants import Direction

class Robot:

    def __init__(self,grid):
        self.pos = RobotPosition(18,1,Direction.TOP)
        self.grid = grid

        self.path_hist = []
        self.__current_command = 0


    def straight(self):
        print("Travelling Straight...")

    def turn(self):
        print("Turning..")