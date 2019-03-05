from player import *
from example_item import *
from zombie_gridwalker import *
# this is not a class currently, but a suite of helper methods
import mapgenerator

def create_level (gameEngine, gameGlobals):

    # create the vertical part of the cross
    mapgenerator.create_rock_wall(gameEngine,200,50,200,150)
    mapgenerator.create_rock_wall(gameEngine,200,250,200,350)

    # create the horizontal part of the cross
    mapgenerator.create_rock_wall(gameEngine,50,200,150,200)
    mapgenerator.create_rock_wall(gameEngine,250,200,350,200)

    it = ExampleItem(x=200,y=200)
    gameEngine.add_game_object(it)

    # create a gridwalker
    gw = ZombieGridwalker(x=50,y=50)
    gameEngine.add_game_object(gw)

    # ALWAYS remember to create the player!
    pl = Player(x=300,y=300)
    gameEngine.add_game_object(pl)
    gameGlobals.player = pl
