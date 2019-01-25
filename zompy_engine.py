from engine import *
from zombie import *

class ZompyGlobals(GameGlobals):
    zoms = 10

class ZompyEngine(GameEngine):

    def __init__(self):
        super().__init__()

    def make_globals(self):
        return ZompyGlobals(self)

    def setup_game(self,gGlobals):
        z1 = Zombie(x=50,y=50,colour="red",char="R")
        
        z2 = Zombie(x=100,y=100,colour="green",char="G")
        
        z3 = Zombie(x=150,y=150,colour="blue",char="B")

        z4 = Zombie(x=200,y=200)

        print(gGlobals.zoms)
        
        super().add_game_object(z1)
        super().add_game_object(z2)
        super().add_game_object(z3)
        super().add_game_object(z4)
