import numpy as np
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

    if(ob[0]+3 <18): # Create all waypoints if possible
        grid[ob[0]+3][ob[1]] = 'S'
        waypoints.append([ob[0]+3,ob[1],'N']) # Waypoint Co-ordinate + Orientation of Car
    if(ob[1]-3 >= 0):
        grid[ob[0]][ob[1]-3] = 'W'
        waypoints.append([ob[0],ob[1]-3,'E']) 
    if(ob[0]-3 >= 0):
        grid[ob[0]-3][ob[1]] = 'N'
        waypoints.append([ob[0]-3,ob[1],'S'])
    if(ob[1]+3 <18):
        grid[ob[0]][ob[1]+3] = 'E'
        waypoints.append([ob[0],ob[1]+3,'W'])


#2d matrix of the distance between obstacles(including Robot startpoint)
def get_distance_between_obstacles(obstacles):
    dist = [[float("inf") for _ in range(len(obstacles)+1)] for _ in range(len(obstacles)+1)]
    obs = [[18,2]] + obstacles
    for i in range(len(obs)):
        for j in range(i, len(obs)):
            dist[i][j] = abs(obs[i][0]-obs[j][0]) + abs(obs[i][1]-obs[j][1])
            dist[j][i] = dist[i][j]

    return dist

#2d matrix of the distance between waypoints(including Robot startpoint)
def get_distance_between_waypoints(waypoints):
    dist = [[float("inf") for _ in range(len(waypoints)+1)] for _ in range(len(waypoints)+1)]
    wayp = [[18,2]] + waypoints
    for i in range(len(wayp)):
        for j in range(i, len(wayp)):
            dist[i][j] = abs(wayp[i][0]-wayp[j][0]) + abs(wayp[i][1]-wayp[j][1])

            if dist[i][j] == float("inf") or dist[i][j] == np.NaN: 
                    dist[i][j] = 1000
                    
            dist[j][i] = dist[i][j]
    return dist

print(np.matrix(grid)) #Prints the grid such that it looks nicer

for _ in get_distance_between_obstacles(obstacles):
    print(_)

for _ in get_distance_between_waypoints(waypoints):
    print(_)






