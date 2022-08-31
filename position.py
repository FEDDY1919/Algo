from constants import Direction

class Position:

    def __init__(self,r,c,direction:Direction = None):
        self.r = r
        self.c = c
        self.direction = direction
        self.isObstacle = False

    def __str__(self):
        if self.isObstacle: return f"X"
        return f"{self.r}-{self.c}-{self.direction}"

    __repr__ = __str__

    def rc(self):
        return self.r,self.c

    def rc_dir(self):
        return self.r,self.c,self.direction

    def copy(self):
        return Position(self.r,self.c,self.direction)


class RobotPosition(Position):

    def __init__(self,r,c,direction:Direction = None,angle = None):
        super().__init__(r,c,direction)
        self.angle = angle
        if direction is not None:
            self.angle = direction.value
    
    
    def copy(self):
        return RobotPosition(self.r,self.c,self.direction,self.angle)


    