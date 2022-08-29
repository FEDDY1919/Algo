from constants import Direction
class Forward:

    def __init__(self,dist):
        self.dist = dist

    def __str__(self):
        return f"Forward {self.dist}"

    def apply_on_pos(self,curr_pos):

        if curr_pos.direction == Direction.RIGHT:
            curr_pos.c += self.dist
        elif curr_pos.direction == Direction.TOP:
            curr_pos.r += self.dist
        elif curr_pos.direction == Direction.BOTTOM:
            curr_pos.r -= self.dist
        else:
            curr_pos.c -= self.dist

        return self
