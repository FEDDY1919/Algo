import heapq
import math
import itertools
from position import Position
from forward import Forward

class Node:

    def __init__(self, parent = None, position = None,direction = None, move = None):
        self.parent = parent
        self.position = Position(position,direction)
        self.move = move
        self.g = 0
        self.h = 0
        self.f = 0
     # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f
    
    def __eq__(self, other):
        return self.position.get_pos() == other.position.get_pos()

    def __str__(self):
        return f"{self.position},{self.move}"

def check_valid_command(command,pos:Position):
    p = pos.copy()

    command.apply_on_pos(p)
    if p.validate_position():
        return [p.get_r(),p.get_c()]

    return False

def astar(maze,start,end):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    open_list = []
    closed_list = []
    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)
    #What squares to use
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))

    
    while len(open_list) > 0:
        #get current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)
        #reached the end, return the path
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        #Generate child nodes for the current node
        children = []

        neighbors = []
        commands = [Forward(10),Forward(-10)]

        for c in commands:
            p = check_valid_command(c,current_node.position)
            if p:
                print(maze.validateRobotPos(p))
                if maze.validateRobotPos(p.get_pos()):
                    neighbor_node = Node(current_node,p,current_node.position.get_dir(),c)
                    neighbors.append(neighbor_node)



        for n in neighbors:
            print(n)
        turn_commands = ['FL','FR','BL','BR']
        for new_position in adjacent_squares: # Adjacent squares

            # Get node position, used
   
       
            node_position = [current_node.position.get_r() + new_position[0], current_node.position.get_c() + new_position[1]]

            # Make sure within range
            if node_position[0] > (len(maze.grid) - 1) or node_position[0] < 0 or node_position[1] > (len(maze.grid[len(maze.grid)-1]) -1) or node_position[1] < 0:
                continue
            # Make sure walkable terrain
            if maze.grid[node_position[0]][node_position[1]] == 'X':
                continue
                
            if not maze.validateRobotPos(node_position):
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child in closed_list:
                continue


            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = math.sqrt(((current_node.position.get_r() - end_node.position.get_r()) ** 2) + ((current_node.position.get_c() - end_node.position.get_c()) ** 2))
            child.f = child.g + child.h

            # Child is already in the open list
            if child in open_list:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)


    
