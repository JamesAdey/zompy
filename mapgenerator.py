from rockwall import *
import random
import math

def create_random_rocks(gameEngine,width,height,numwalls):
    
    # pad 30 units around the edge
    padding = 30
    
    for i in range(numwalls):

        xPos = random.randint(padding,width-padding)
        yPos = random.randint(padding,height-padding)
        # create a random wall
        wall = RockWall(x=xPos,y=yPos)
        gameEngine.add_game_object(wall)


def create_rock_wall(gameEngine,startX,startY,endX,endY):

    # size of each block is 20
    size = 20
    halfSize = size/2
    
    # work out the difference in X and Y coordinates
    dx = endX - startX
    dy = endY - startY

    # work out how far the wall goes
    distance = math.sqrt((dx*dx)+(dy*dy))

    # work out how many walls we need to spawn
    walls = int(distance/size)

     # work out the "step" to space the walls out with
    stepX = dx/walls
    stepY = dy/walls
    
    for i in range(walls):

        # work out where to build the wall
        xPos = startX + halfSize + (i*stepX)
        yPos = startY + halfSize + (i*stepY)
    

        # create the wall
        wall = RockWall(x=xPos,y=yPos)
        gameEngine.add_game_object(wall)
