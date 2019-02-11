from gameobject import *

class ExampleItem(GameObject):

    radius = 10
    colour = "#FFFF00"
    char = 'i'

    m_ovalId = None
    m_textId = None

    def __init__(self,x=0,y=0,colour="#FFFF00",char='i'):
        super().__init__()
        self.x = x
        self.y = y
        self.colour = colour
        self.char = char

    def on_start(self,gameGlobals):
        # register ourselves with the gameWorld as an item
        gameGlobals.itemManager.add_item(self)

    def on_remove(self, gameGlobals):
        # remove ourselves from the list of items
        gameGlobals.itemManager.remove_item(self)

    def setup_gfx(self, tkCanvas):
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius

        # ONLY MAKE, NO MOVE
        self.m_ovalId = tkCanvas.create_oval(x0,y0,x1,y1,fill=self.colour)
        self.m_textId = tkCanvas.create_text(self.x,self.y,text=self.char)

    def remove_gfx(self,tkCanvas):
        tkCanvas.delete(self.m_ovalId)
        tkCanvas.delete(self.m_textId)

    '''
        Note no draw or update functions in this object.
        These functions are defined in our parent class (gameobject).
        But we don't need to actually do anything every frame.
    '''

    def on_collision(self, gameGlobals, other):
        print("Item collided with "+str(other))
        # remove this item after being picked up
        gameGlobals.engine.remove_game_object(self)

    def get_collision_radius(self):
        return self.radius
