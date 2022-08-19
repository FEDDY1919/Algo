import numpy as np
import itertools
import math
grid = [
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    ['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],
    
]
    

obstacles = [[5,6],[12,9],[19,6],[19,17],[3,15]] #Test Obstacles
waypoints = []

current_pos = [18,2] #Starting/Current Position
current_dir = 'N' #Current Direction it is facing

for ob in obstacles: # Set Obstacles

    grid[ob[0]][ob[1]] = 'X'

    # if(ob[0]+3 <18): # Create all waypoints if possible
    #     grid[ob[0]+3][ob[1]] = 'S'
    #     waypoints.append([ob[0]+3,ob[1],'N']) # Waypoint Co-ordinate + Orientation of Car
    # if(ob[1]-3 >= 0):
    #     grid[ob[0]][ob[1]-3] = 'W'
    #     waypoints.append([ob[0],ob[1]-3,'E']) 
    # if(ob[0]-3 >= 0):
    #     grid[ob[0]-3][ob[1]] = 'N'
    #     waypoints.append([ob[0]-3,ob[1],'S'])
    # if(ob[1]+3 <18):
    #     grid[ob[0]][ob[1]+3] = 'E'
    #     waypoints.append([ob[0],ob[1]+3,'W'])
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


#===================================================================================
#2d matrix of the distance between obstacles(including Robot startpoint)
# def get_distance_between_obstacles(obstacles):
#     dist = [[float("inf") for _ in range(len(obstacles)+1)] for _ in range(len(obstacles)+1)]
#     obs = [[18,2]] + obstacles
#     for i in range(len(obs)):
#         for j in range(i, len(obs)):
#             dist[i][j] = abs(obs[i][0]-obs[j][0]) + abs(obs[i][1]-obs[j][1])
#             dist[j][i] = dist[i][j]

#     return dist
# print(np.matrix(grid)) #Prints the grid such that it looks nicer

# for _ in get_distance_between_obstacles(obstacles):
#     print(_)


#====================================================================================
#2d matrix of the distance between waypoints(including Robot startpoint)
# def get_distance_between_waypoints(waypoints):
#     dist = [[float("inf") for _ in range(len(waypoints)+1)] for _ in range(len(waypoints)+1)]
#     wayp = [[18,2]] + waypoints
#     for i in range(len(wayp)):
#         for j in range(i, len(wayp)):
#             dist[i][j] = abs(wayp[i][0]-wayp[j][0]) + abs(wayp[i][1]-wayp[j][1])

#             if dist[i][j] == float("inf") or dist[i][j] == np.NaN: 
#                     dist[i][j] = 1000
                    
#             dist[j][i] = dist[i][j]
#     return dist

# for _ in get_distance_between_waypoints(waypoints):
#     print(_)






