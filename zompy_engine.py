from engine import *
from zombie import *
from player import *
from bullet_manager import *
from gameworld import *
from zombie_spawner import *
from item_manager import *
from example_item import *
from navgrid import *
from zombie_gridwalker import *

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
    
        # create a zombie spawner
        zs = ZombieSpawner(x=100,y=100)
        super().add_game_object(zs)

        # create a nav grid
        ng = NavGrid(resolution=20)
        super().add_game_object(ng)
        gGlobals.navGrid = ng

        # create a gridwalker
        gw = ZombieGridwalker(x=50,y=50)
        super().add_game_object(gw)

        for i in range(10):
            it = ExampleItem(x=200,y=200+(i*10))
            super().add_game_object(it)

        
        
        pl = Player(x=300,y=300)
        gGlobals.player = pl
        
        super().add_game_object(zs)

        super().add_game_object(pl)
