from winreg import DisableReflectionKey

from constants import GRID_COLUMNS, GRID_ROWS


class Position:

    def __init__(self,pos,direction = None):
        self.r = pos[0]
        self.c = pos[1]
        try:
            self.direction = pos[2]
        except:
            self.direction = direction


    def __str__(self):
        return f"{self.r},{self.c},{self.direction}"

    def get_r(self):
        return self.r
    
    def get_c(self):
        return self.c

    def get_pos(self):
        return self.r,self.c

    def get_dir(self):
        return self.direction

    def get_all(self):
        return self.r,self.c,self.direction
    
    def validate_position(self):
        if self.r > GRID_ROWS or self.r<0 or self.c>GRID_COLUMNS or self.c<0:
            return False
        return True
    
    def copy(self):
        return Position([self.r,self.c],self.direction)