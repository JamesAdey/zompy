from player import *
from zombie_spawner import *
from example_item import *
from zombie_gridwalker import *
# this is not a class currently, but a suite of helper methods
import mapgenerator


def create_level (gameEngine, gameGlobals):

    # create a bunch of random rocks
    mapgenerator.create_random_rocks(gameEngine,400,400,30)

    it = ExampleItem(x=200,y=200)
    gameEngine.add_game_object(it)

    # create a gridwalker
    gw = ZombieGridwalker(x=50,y=50)
    gameEngine.add_game_object(gw)

    # create a zombie spawner
    zs = ZombieSpawner(x=25,y=25)
    gameEngine.add_game_object(zs)

    # create a zombie spawner
    zs = ZombieSpawner(x=375,y=375)
    gameEngine.add_game_object(zs)

    # ALWAYS remember to create the player!
    pl = Player(x=300,y=300)
    gameEngine.add_game_object(pl)
    gameGlobals.player = pl
