import numpy as np
import itertools
import math
from grid import *
from constants import *
from shortest_path import *

obstacles = [[5,6],[12,9],[19,6],[19,17],[3,15]] #Test Obstacles


current_pos = [18,2] #Starting/Current Position AND Direction it is facing


maze = Maze()
maze.setObstacles(obstacles)

#All Possible Permutations for hamilton path
perms = list(itertools.permutations(obstacles))

def calc_distance(path):
    # Create all target points, including the start.
    targets = [[18,2]]
    for obstacle in path:
        targets.append(obstacle)

    dist = 0
    for i in range(len(targets) - 1):
        dist += math.sqrt(((targets[i][0] - targets[i + 1][0]) ** 2) + ((targets[i][1] - targets[i + 1][1]) ** 2))
    return dist

#Finds the Simplest hamilton path
simple = min(perms,key = calc_distance)
print("Found a simple hamiltonian path:")
for ob in simple:
    print(f"\t{ob}")

print(simple[0])
#maze.setWayPoints(obstacles)
maze.draw()
for ob in simple:
   path = astar(maze.grid,current_pos,ob)
   current_pos = ob
   for item in path:
        maze.grid[item[0]][item[1]] = 'O'
   maze.draw()









