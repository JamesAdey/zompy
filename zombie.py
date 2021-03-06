from gameobject import *
import player

class Zombie(GameObject):

    startX = 0
    startY = 0

    # zombie stats
    health = 10
    speed = 0.5
    damage = 1

    radius = 10
    colour = "#2f9909"
    char = 'z'

    m_ovalId = None
    m_textId = None

    def __init__(self,x=0,y=0,colour="#2f9909",char='z'):
        super().__init__()
        self.x = x
        self.y = y
        self.colour = colour
        self.char= char

    def on_start(self,gameGlobals):
        self.startX = self.x
        self.startY = self.y
        # register ourselves with the game world as an obstacle
        gameGlobals.gameWorld.add_obstacle(self)
        # register ourselves with the gameWorld as an item
        # this means we can detect collisions
        gameGlobals.itemManager.add_item(self)

    def on_remove(self, gameGlobals):
        # remove ourselves from the list of obstacles
        gameGlobals.gameWorld.remove_obstacle(self)
        # remove ourselves from the list of items
        gameGlobals.itemManager.remove_item(self)

    def setup_gfx(self, tkCanvas):
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius

        # ONLY MAKE, NO MOVE
        self.m_ovalId = tkCanvas.create_oval(x0,y0,x1,y1,fill=self.colour)
        self.m_textId = tkCanvas.create_text(self.x,self.y,text=self.char)

    def remove_gfx(self,tkCanvas):
        tkCanvas.delete(self.m_ovalId)
        tkCanvas.delete(self.m_textId)

    def draw(self, tkCanvas):
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius

        # ONLY MOVE, NO MAKE
        tkCanvas.coords(self.m_ovalId,x0,y0,x1,y1)
        tkCanvas.coords(self.m_textId,self.x,self.y)

    def update(self, gameGlobals):

        # move towards the player
        (playerX,playerY) = gameGlobals.player.get_position()

        moveX = 0
        moveY = 0
        
        if(playerX < self.x):
            moveX = -self.speed
        elif(playerX > self.x):
            moveX = self.speed

        
        if(playerY < self.y):
            moveY = -self.speed
        elif(playerY > self.y):
            moveY = self.speed
        
        
        self.x = self.x + moveX
        self.y = self.y + moveY

        if(self.health <= 0):
            self.dead(gameGlobals)

    def dead(self,gameGlobals):
        # notify the game manager that we've died
        gameGlobals.gameManager.zombie_killed(self)
        # remove ourselves from the game
        gameGlobals.engine.remove_game_object(self)

    def take_damage(self,damage):
        self.health -= damage

    def get_collision_radius(self):
        return self.radius

    def on_collision(self, gameGlobals, other):
        if(isinstance(other, player.Player)):
            other.take_damage(self.damage)

    def set_stats(self,speed=0.5,radius=10,health=10,damage=1):
        self.speed = speed
        self.radius = radius
        self.health = health
        self.damage = damage
