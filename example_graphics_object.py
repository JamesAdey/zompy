from gameobject import *

class ExampleGraphicsObject(GameObject):

    startX = 0
    startY = 0
    
    radius = 10
    color = "red"
    char = 'R'

    m_ovalId = None
    m_textId = None

    def __init__(self,x=0,y=0):
        super().__init__(self)
        pass

    def on_start(self,gameGlobals):
        self.startX = self.x
        self.startY = self.y

    def setup_gfx(self, tkCanvas):
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius

        # ONLY MAKE, NO MOVE
        self.m_ovalId = tkCanvas.create_oval(x0,y0,x1,y1,fill=self.color)
        self.m_textId = tkCanvas.create_text(self.x,self.y,text=self.char)

    def on_remove(self,gameGlobals):
        # do nothing
        pass

    def remove_gfx(self,tkCanvas):
        tkCanvas.delete(self.m_ovalId)
        tkCanvas.delete(self.m_textId)

    def draw(self, tkCanvas):
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius

        # ONLY MOVE, NO MAKE
        tkCanvas.coords(self.m_ovalId,x0,y0,x1,y1)
        tkCanvas.coords(self.m_textId,self.x,self.y)

    def update(self, gameGlobals):
        self.x = startX + math.cos(gameGlobals.realTime)*self.radius
        self.y = startY + math.sin(gameGlobals.realTime)*self.radius
