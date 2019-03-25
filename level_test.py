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

    # ALWAYS remember to create the players!
    p1 = Player(x=300,y=300,char='1',colour="#0099FF")
    p1.set_player_info(1,"w","s","a","d")
    gameEngine.add_game_object(p1)
    gameGlobals.players.append(p1)

    p2 = Player(x=100,y=300,char='2',colour="#FF4444")
    p2.set_player_info(2,"Up","Down","Left","Right")
    gameEngine.add_game_object(p2)
    gameGlobals.players.append(p2)
