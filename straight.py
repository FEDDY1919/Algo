from position import RobotPosition
from constants import Direction

class StraightCommand:

    def __init__(self,distance):
        self.distance = distance

    def __str__(self):
        return f"StraightCommand travelling {self.distance}"
    
    __repr__ = __str__

    def apply_on_pos(self,pos:RobotPosition):
        
        if pos.direction == Direction.RIGHT:
            pos.c += self.distance
        if pos.direction == Direction.LEFT:
            pos.c -= self.distance
        if pos.direction == Direction.TOP:
            pos.r -= self.distance
        else:
            pos.r += self.distance
        