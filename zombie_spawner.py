from gameobject import *
from zombie import *

class ZombieSpawner(GameObject):

    zombies = []
    maxZombies = 10

    nextSpawnTime = None
    # spawn delay in seconds
    spawnDelay = 5

    def __init__(self,x=0,y=0,colour="#2f9909",char='z'):
        super().__init__()
        self.x = x
        self.y = y
        self.colour = colour
        self.char = char


    def on_start(self, gGlobals):
        self.nextSpawnTime = 0

    def update(self, gGlobals):

        # exit the function if we've got enough zombies already
        if(len(self.zombies) >= self.maxZombies):
            return

        # check if the next spawn time has elapsed
        if(gGlobals.realTime > self.nextSpawnTime):
            self.nextSpawnTime = gGlobals.realTime + self.spawnDelay
            self.spawn_zombie(gGlobals)


    def spawn_zombie(self,gGlobals):
        zo = Zombie(self.x,self.y)
        zo.set_spawner(self)
        self.zombies.append(zo)
        gGlobals.engine.add_game_object(zo)

    def remove_zombie(self, zom):
        if zom in self.zombies:
            self.zombies.remove(zom)
