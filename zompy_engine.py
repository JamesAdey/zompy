from engine import *
from zombie import *
from player import *
from bullet_manager import *
from gameworld import *
from zombie_spawner import *
from item_manager import *
from example_item import *

class ZompyGlobals(GameGlobals):
    zoms = 10
    bulletManager = None
    itemManager = None
    gameWorld = None
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

        zs = ZombieSpawner(x=100,y=100)
        super().add_game_object(zs)

        it = ExampleItem(x=200,y=200)
        super().add_game_object(it)
        
        pl = Player(x=300,y=300)
        gGlobals.player = pl
        
        super().add_game_object(zs)

        super().add_game_object(pl)
