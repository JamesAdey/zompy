from engine import *
from bullet_manager import *
from gameworld import *
from item_manager import *
from navgrid import *

# these are not a class currently
# but a suite of helper methods
import level_random
import level_cross
import level_test

class ZompyGlobals(GameGlobals):
    zoms = 10
    bulletManager = None
    itemManager = None
    gameWorld = None
    navGrid = None
    player = None

class ZompyEngine(GameEngine):

    def __init__(self):
        super().__init__()

    def make_globals(self):
        return ZompyGlobals(self)

    def setup_game(self,gGlobals):

        # create a gameworld
        gw = GameWorld()
        gGlobals.gameWorld = gw
        
        # create the managers for the game
        bm = BulletManager()
        gGlobals.bulletManager = bm
        super().add_game_object(bm)

        im = ItemManager()
        gGlobals.itemManager = im
        super().add_game_object(im)

        # create a nav grid
        ng = NavGrid(resolution=20)
        super().add_game_object(ng)
        gGlobals.navGrid = ng

        levelName = "random"

        if(levelName == "random"):
            level_random.create_level(super(),gGlobals)
        elif(levelName == "cross"):
            level_cross.create_level(super(),gGlobals)
        elif(levelName ==  "test"):
            level_test.create_level(super(),gGlobals)
        else:
            print("ERROR Could not create level!")
      

