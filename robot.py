from constants import Direction

class Robot:
    def __init__(self,r,c,direction:Direction = None,angle = None):
        self.r = r
        self.c = c
        self.direction = direction

    def get_current_pos(self):
        return self.r,self.c

    def get_pos_dir(self):
        return self.r,self.c,self.direction

    def update_current_pos(self,r,c):
        self.r = r
        self.c = c