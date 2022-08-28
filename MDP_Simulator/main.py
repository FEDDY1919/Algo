import pygame
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0,0,255)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

# Car
carImg = pygame.image.load('car2.png')
carX = 10
carY = 690

def car(x,y):
    SCREEN.blit(carImg, (x,y))

# def rotate_car(x,y):
#     rotated_image = pygame.transform.rotate(carImg,180)
#     SCREEN.blit(rotated_image, (x+120,y))

# Obstacle
obsImg = pygame.image.load("obs.png")

def obstacle(x,y,dir):
    rotated_obs = pygame.transform.rotate(obsImg,dir)
    SCREEN.blit(rotated_obs,(x,y))

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    plantObstacles()

    while True:
        drawGrid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        car(carX,carY)
        #rotate_car(carX,carY)
        #obstacle(obsX,obsY)



        pygame.display.update()


def drawGrid():
    blockSize = 40 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

def plantObstacles():
    obsQty = 5 # Number of obstacles
    i = 0
    while i < obsQty:
        obsX = random.randint(0,20) * 40
        obsY = random.randint(0,20) * 40
        dir = random.randint(0,3) * 90
        obstacle(obsX,obsY,dir)
        i += 1
        if i == obsQty:
            break




main()

''' 
Start zone: bottom left corner => 3x3 grid cell
The car moves
'''