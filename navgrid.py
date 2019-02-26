from gameobject import *
from engine import *
import queue
import heapq

class NavCell():

    # initialise data members to invalid values
    x = -1
    y = -1
    center = (-1,-1)
    seen = False
    hasPlayer = False
    parent = None
    goal = None
    fScore = 0
    gScore = 0
    cost = 0

    def is_blocked(self):
        return cost > 0

    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        halfSize = size/2
        self.center = ((x*size)+halfSize,(y*size)+halfSize)

    def __str__(self):
        base = "("+str(self.x)+","+str(self.y)+")"
        if(self.hasPlayer):
            base += " PLAY"
        else:
            base += " NONE"
        return base



class NavGrid (GameObject):

    mode = "done"

    openList = []

    cells = [[]]

    blockers = []

    mapWidth = 0
    mapHeight = 0
    resolution = 0

    def __init__(self,x=0,y=0,resolution=20):
        super().__init__(self)
        self.resolution = resolution

    def on_start(self,gameGlobals):
        pass
        

    def on_remove(self,gameGlobals):
        # do nothing
        pass


    def setup_gfx(self,tkCanvas):
        # initialise the grid
        self.mapWidth = tkCanvas.winfo_width()
        self.mapHeight = tkCanvas.winfo_height()
        cellsX = int(self.mapWidth / self.resolution)
        cellsY = int(self.mapHeight / self.resolution)
        self.mode = "done"
        self.cells = [[NavCell(x,y,self.resolution) for y in range(cellsY)] for x in range(cellsX)]

        
    def remove_gfx(self,tkCanvas):
        pass

    def add_blocker(self,blocker):
        if(blocker not in self.blockers):
            self.blockers.append(blocker)

    def remove_blocker(self,blocker):
        if(blocker in self.blockers):
            self.blockers.remove(blocker)

    def update(self, gameGlobals):
        if(self.mode == "done"):
            # clear the open list
            self.openList.clear()
            # reset the grid
            for column in self.cells:
                for cell in column:
                    cell.goal = cell.parent
                    cell.cost = 0
                    cell.fScore = 9999999999
                    cell.parent = None
                    cell.seen = False
                    cell.hasPlayer = False
            # update the blockers
            for blocker in self.blockers:
                cell = self.closest_cell_to(blocker)
                cell.cost += blocker.get_nav_cost()
            # add the closest cell to the player to the grid
            closest = self.closest_cell_to(gameGlobals.player)
            closest.hasPlayer = True
            closest.fScore = 0
            self.openList.append(closest)
            self.mode = "step"
        
        elif(self.mode == "step"):

            for i in range(self.resolution):
                if(self.openList == []):
                    self.mode = "done"
                    break
            
                # find the closest cell so far
                closest = self.openList[0]
                for cell in self.openList:
                    if(cell.fScore < closest.fScore):
                        closest = cell

                # select this cell
                self.openList.remove(closest)
                closest.hasPlayer = True
                # get neighbours
                self.add_neighbours(closest)

        
    def add_neighbours(self, cell):

        y = cell.y

        
        # check right
        x = cell.x + 1
        if(x < self.resolution):
            newCell = self.cells[x][y]
            if(not newCell.hasPlayer):
                newF = newCell.cost + cell.fScore + 1
                if(newF < newCell.fScore):
                    newCell.fScore = newF
                    newCell.parent = cell
                if(not newCell.seen):
                    newCell.seen = True
                    self.openList.append(newCell)
    

        # check left
        x = cell.x - 1
        if(x >= 0):
            newCell = self.cells[x][y]
            if(not newCell.hasPlayer):
                newF = newCell.cost + cell.fScore + 1
                if(newF < newCell.fScore):
                    newCell.fScore = newF
                    newCell.parent = cell
                if(not newCell.seen):
                    newCell.seen = True
                    self.openList.append(newCell)

        
        x = cell.x

        # check up
        y = cell.y + 1
        if(y < self.resolution):
            newCell = self.cells[x][y]
            if(not newCell.hasPlayer):
                newF = newCell.cost + cell.fScore + 1
                if(newF < newCell.fScore):
                    newCell.fScore = newF
                    newCell.parent = cell
                if(not newCell.seen):
                    newCell.seen = True
                    self.openList.append(newCell)

        # check down
        y = cell.y - 1
        if(y >= 0):
            newCell = self.cells[x][y]
            if(not newCell.hasPlayer):
                newF = newCell.cost + cell.fScore + 1
                if(newF < newCell.fScore):
                    newCell.fScore = newF
                    newCell.parent = cell
                if(not newCell.seen):
                    newCell.seen = True
                    self.openList.append(newCell)  
        return

    
    def clamp_pair(self,pair):
        (x,y) = pair
        if(x < 0):
            x = 0
        elif(x >= self.mapWidth):
            x = self.mapWidth-1

        if(y < 0):
            y = 0
        elif(y >= self.mapHeight):
            y = self.mapHeight-1

        return (x,y)

    def closest_cell_to(self, targetObj):
        (x,y) = targetObj.get_position()
        # work out which cell this belongs in
        (x,y) = self.clamp_pair((x,y))

        cellWidth = self.mapWidth / self.resolution
        cellHeight = self.mapHeight / self.resolution

        cellX = int(x/cellWidth)
        cellY = int(y/cellHeight)

        return self.cells[cellX][cellY]

