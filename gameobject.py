import math

class GameObject(object):

    x = 0
    y = 0

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def setup_gfx(self, tkCanvas):
        pass

    def remove_gfx(self,tkCanvas):
        pass
        
    def draw(self, tkCanvas):
        pass

    def on_start(self, gameGlobals):
        pass

    def on_remove(self, gameGlobals):
        pass

    def update(self, gameGlobals):
        pass

    def get_position(self):
        return(self.x,self.y)

    def get_collision_radius(self):
        return 0
