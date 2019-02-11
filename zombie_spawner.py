from gameobject import *
from zombie import *

class ZombieSpawner(GameObject):

    nextSpawnTime = None
    # spawn delay in seconds
    spawnDelay = 5

    def __init__(self,x=0,y=0):
        super().__init__()
        self.x = x
        self.y = y

    def on_start(self, gGlobals):
        self.nextSpawnTime = 0

    def update(self, gGlobals):

        # check if the next spawn time has elapsed
        if(gGlobals.realTime > self.nextSpawnTime):
            # delay the next spawn by the given delay
            self.nextSpawnTime = gGlobals.realTime + self.spawnDelay
            # spawn a new zombie
            self.spawn_zombie(gGlobals)


    def spawn_zombie(self,gGlobals):
        zo = Zombie(self.x,self.y)
        gGlobals.engine.add_game_object(zo)
