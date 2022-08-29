from enum import Enum

GRID_COLUMNS = 18
GRID_ROWS = 20

class Direction(Enum):
    LEFT = 180
    TOP = 90
    BOTTOM = -90
    RIGHT = 0