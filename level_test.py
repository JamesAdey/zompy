from player import *
from zombie_spawner import *
from example_item import *
from zombie_gridwalker import *
# this is not a class currently, but a suite of helper methods
import mapgenerator


def create_level (gameEngine, gameGlobals):

    # create a zombie spawner
    zs = ZombieSpawner(x=100,y=100)
    gameEngine.add_game_object(zs)
        
    # create a gridwalker
    gw = ZombieGridwalker(x=50,y=50)
    gameEngine.add_game_object(gw)

    # create a line of items
    for i in range(10):
        it = ExampleItem(x=200,y=200+(i*10))
        gameEngine.add_game_object(it)

    # ALWAYS remember to create the player!
    pl = Player(x=300,y=300)
    gameEngine.add_game_object(pl)
    gameGlobals.player = pl
