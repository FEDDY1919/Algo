
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