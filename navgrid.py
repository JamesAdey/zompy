from gameobject import *
from engine import *
import queue
import heapq

class NavCell():

    # initialise data members to invalid values
    x = -1
    y = -1
    center = (-1,-1)
    hasPlayer = False
    parent = None
    goal = None

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
    openQueue = queue.Queue()
    newCells = queue.Queue()
    
    cells = [[]]

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


    def update(self, gameGlobals):
        if(self.mode == "done"):
            # clear the open queue
            self.openQueue.queue.clear()
            self.newCells.queue.clear()
            # reset the grid
            for column in self.cells:
                for cell in column:
                    cell.goal = cell.parent
                    cell.parent = None
                    cell.hasPlayer = False
            # add the closest cell to the player to the grid
            closest = self.closest_cell_to(gameGlobals.player)
            closest.hasPlayer = True
            self.openQueue.put(closest)
            self.mode = "step"
        
        elif(self.mode == "step"):

            if(self.openQueue.empty()):
                print("done")
                self.mode = "done"
        
            # add the closest cell to the player to the grid
            while(not self.openQueue.empty()):
                cell = self.openQueue.get()
                # get neighbours
                self.add_neighbours(cell)

            # refill the open queue
            while(not self.newCells.empty()):
                #print(self.newCells.qsize())
                cell = self.newCells.get()
                self.openQueue.put(cell)

        
    def add_neighbours(self, cell):

        y = cell.y

        
        # check right
        x = cell.x + 1
        if(x < self.resolution):
            newCell = self.cells[x][y]
            if(newCell.hasPlayer == False):
                newCell.hasPlayer = True
                newCell.parent = cell
                self.newCells.put(newCell)
    

        # check left
        x = cell.x - 1
        if(x >= 0):
            newCell = self.cells[x][y]
            if(newCell.hasPlayer == False):
                newCell.hasPlayer = True
                newCell.parent = cell
                self.newCells.put(newCell)

        
        x = cell.x

        # check up
        y = cell.y + 1
        if(y < self.resolution):
            newCell = self.cells[x][y]
            if(newCell.hasPlayer == False):
                newCell.hasPlayer = True
                newCell.parent = cell
                self.newCells.put(newCell)

        # check down
        y = cell.y - 1
        if(y >= 0):
            newCell = self.cells[x][y]
            if(newCell.hasPlayer == False):
                newCell.hasPlayer = True
                newCell.parent = cell
                self.newCells.put(newCell)   
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

