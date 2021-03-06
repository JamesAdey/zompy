from gameobject import *
import zombie

class Player(GameObject):

    playerNum = None
    upKey = "w"
    downKey = "s"
    leftKey = "a"
    rightKey = "d"

    health = 100
    radius = 10
    hurt = True
    
    colour = "#DDDDFF"
    char = '@'

    m_ovalId = None
    m_textId = None
    
    def __init__(self,x=0,y=0,colour="#DDDDFF",char='@'):
        super().__init__()
        self.x = x
        self.y = y
        self.colour = colour
        self.char = char

    def on_start(self,gameGlobals):
        self.startX = self.x
        self.startY = self.y

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

        # get the inputs from the keyboard
        (xMove,yMove,shoot) = self.do_inputs(gameGlobals)

        # do the movement
        self.x = self.x + xMove
        self.y = self.y + yMove

        # do the shooting
        if(shoot):
            # get the mouse position as the end of our bullet
            (endX,endY) = gameGlobals.get_mouse_position()
            # trace the physics line against the zombies
            hit = gameGlobals.gameWorld.traceline(self.x,self.y,endX,endY)
            if(isinstance(hit,zombie.Zombie)):
                hit.take_damage(10)
            # draw the bullet effects
            gameGlobals.bulletManager.fire_bullet(self.x,self.y,endX,endY)

        # update our status in the GUI
        if(self.hurt):
            gameGlobals.gameManager.update_player_health(self.playerNum, self.health)
            self.hurt = False

    def do_inputs(self, gameGlobals):
        xMove = 0
        yMove = 0
        shoot = False
        
        if(gameGlobals.is_key_pressed(self.leftKey)):
            xMove -=1
        
        if(gameGlobals.is_key_pressed(self.rightKey)):
            xMove +=1
            
        if(gameGlobals.is_key_pressed(self.upKey)):
            yMove -=1
        
        if(gameGlobals.is_key_pressed(self.downKey)):
            yMove +=1

        if(gameGlobals.is_mouse_pressed("left")):
            shoot = True

        return (xMove,yMove,shoot)

    def on_collision(self, gameGlobals, other):
        print("Player collided with "+str(other))

    def get_collision_radius(self):
        return self.radius

    def take_damage(self, damage):
        self.health -= damage
        self.hurt = True

    def set_player_info(self,num,upKey,downKey,leftKey,rightKey):
        self.playerNum = num
        self.upKey = upKey
        self.downKey = downKey
        self.leftKey = leftKey
        self.rightKey = rightKey
                    
