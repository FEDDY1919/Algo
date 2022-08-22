import numpy as np
import itertools
import math
from grid import *
from constants import *
from shortest_path import *
from collections import deque

def calc_distance(path):
    # Create all target points, including the start.
    targets = [[18,2]]
    for obstacle in path:
         targets.append(obstacle)

    dist = 0
    for i in range(len(targets) - 1):
        dist += math.sqrt(((targets[i][0] - targets[i + 1][0]) ** 2) + ((targets[i][1] - targets[i + 1][1]) ** 2))
    return dist

def closest_waypoint(waypoints,start):
    dist = 0
    dist += math.sqrt((waypoints[0]-start[0])**2 + (waypoints[1]-start[1])**2)
    return dist

if __name__ == "__main__":

    obstacles = [[5,6],[12,9],[19,6],[19,17],[3,15]] #Test Obstacles


    current_pos = [18,2] #Starting/Current Position


    maze = Maze()
    maze.setObstacles(obstacles)

    #All Possible Permutations for hamilton path
    perms = list(itertools.permutations(obstacles))


    #Finds the Simplest hamilton path
    simple = min(perms,key = calc_distance)
    print("Found a simple hamiltonian path:")
    for ob in simple:
        print(f"\t{ob}")


    #maze.setWayPoints(obstacles)
    maze.draw()

    #loop through obstacles in the simplest hamiltonian path
    for ob in simple:

        #get the target position we would want to be in for the obstacles, N S E W
        waypoints = maze.getWayPoints(ob)
        #find the closest waypoint for the obstacle
        target = min(waypoints,key = lambda waypoints : closest_waypoint(waypoints,current_pos))

        index = waypoints.index(target)
        #change the array to queue
        #if it is not the first item within the array, we shift it such that it is
        waypoints = deque(waypoints)
        if index != 0:
            waypoints.rotate(-index)

        #A star pathfinding to all the waypoints available
        while len(waypoints)>0:
            wp = waypoints.popleft()
            path = astar(maze,current_pos,wp)
            for item in path:
                if item[0]!=current_pos[0]:
                    if item[0]-current_pos[0] > 0: #This indicates straight line movement along the x axis
                        maze.grid[current_pos[0]][current_pos[1]] = 'S'
                    else:
                        maze.grid[current_pos[0]][current_pos[1]] = 'N'
                else:
                    if item[1]-current_pos[1] > 0:# This indicates movement along the y-axis
                        maze.grid[current_pos[0]][current_pos[1]] = 'E'
                    else:
                        maze.grid[current_pos[0]][current_pos[1]] = 'W'
                current_pos = item
        maze.draw()


#    path = astar(maze,current_pos,ob)
#    current_pos = ob
#    for item in path:
#         maze.grid[item[0]][item[1]] = 'O'
#    maze.draw()



'''
Things to Consider:
1. Size of the robot, the path created would only work if the robot is 10cm x 10cm
2. Points at which the robot should stop, it should not be directly on the obstacle, but near it (done)
3. Include in the heuristic turn penalties and such, making a left or right turn would cause more movement than travelling a straight line
4. Include current orientation within the current_node to help in point 3
5. ....

[r][c] row of the grid, column of the grid

[c+1] a right movement, => EAST
[c-1] a left movement , <= WEST
[r+1] a downward movement, v SOUTH
[r-1] an upward movement, ^ NORTH

[r+1][c+1] a SOUTHEAST movement
[r-1][c-1] a NORTHWEST movement
[r+1][c-1] a SOUTHWEST movement
[r-1][c+1] a NORTHEAST movement

PseudoCode for if image is found:
    while scanning:
        if img_id == bullseye_id:
            path = astar(maze,current_pos,wp)
            travel through path
        else:
            save id
            break and continue to next obstacle

'''






