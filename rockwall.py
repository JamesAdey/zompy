from gameobject import *

class RockWall(GameObject):

    radius = 10
    colour = "#FFFF00"

    navCost = 30

    m_rectId = None

    def __init__(self,x=0,y=0,colour="#444444"):
        super().__init__()
        self.x = x
        self.y = y
        self.colour = colour

    def on_start(self,gameGlobals):
        # register ourselves with the gameWorld as an "item" for collision
        gameGlobals.itemManager.add_item(self)
        # register ourselves as a navigation blocker to stop the zombies
        gameGlobals.navGrid.add_blocker(self)
        # register ourselves as an obstacle for shooting purposes
        gameGlobals.gameWorld.add_obstacle(self)

    def on_remove(self, gameGlobals):
        # remove ourselves from the list of items
        gameGlobals.itemManager.remove_item(self)
        gameGlobals.navGrid.remove_blocker(self)
        gameGlobals.gameWorld.remove_obstacle(self)

    def setup_gfx(self, tkCanvas):
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius

        # ONLY MAKE, NO MOVE
        self.m_rectId = tkCanvas.create_rectangle(x0,y0,x1,y1,fill=self.colour)

    def remove_gfx(self,tkCanvas):
        tkCanvas.delete(self.m_rectId)

    '''
        Note no draw or update functions in this object.
        These functions are defined in our parent class (gameobject).
        But we don't need to actually do anything every frame.
    '''

    def on_collision(self, gameGlobals, other):
        # do nothing on collision
        pass

    def get_collision_radius(self):
        return self.radius

    def get_nav_cost(self):
        return self.navCost
