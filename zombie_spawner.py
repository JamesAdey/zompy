from gameobject import *
from zombie import *
from zombie_ranged import *

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
            self.spawn_ranged_zombie(gGlobals)

    def spawn_zombie(self,gGlobals):
        zo = Zombie(self.x,self.y)
        gGlobals.engine.add_game_object(zo)

    def spawn_big_zombie(self,gGlobals):
        zo = Zombie(x=self.x, y=self.y, colour="#9fff99", char='Z')
        zo.set_stats(speed=0.35,radius=15,health=30,damage=2)
        gGlobals.engine.add_game_object(zo)

    def spawn_ranged_zombie(self,gGlobals):
        zo = RangedZombie(x=self.x, y=self.y, colour="#DD9900", char='&')
        zo.set_stats(speed=0.6,radius=10,health=20,damage=1)
        gGlobals.engine.add_game_object(zo)


