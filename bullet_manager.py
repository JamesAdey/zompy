import queue
from gameobject import *

'''
Just a data container for holding bullet data
'''
class BulletData(object):
    startX = -1
    startY = -1
    endX = -1
    endY = -1
    m_lineId = None
    colour = "#FFFF00"
    redraw = False
    alive = False
    
    
    
    
class BulletManager(GameObject):

    
    MAX_BULLETS = 10
    BULLET_LIFE_TIME = 0.1

    newBulletQueue = queue.Queue()

    bullets = []

    def setup_gfx(self, tkCanvas):
         for i in range(self.MAX_BULLETS):
            b = BulletData()
            b.m_lineId = tkCanvas.create_line(b.startX,b.startY,b.endX,b.endY,fill=b.colour)
            b.redraw = True
            self.bullets.append(b)

    def update(self, gameGlobals):

        while(not self.newBulletQueue.empty()):
            bul = self.newBulletQueue.get()
            bul.deathTime = gameGlobals.realTime + self.BULLET_LIFE_TIME
        
        for b in self.bullets:
            if(b.alive and gameGlobals.realTime >= b.deathTime):
                # reset this bullet back to the "stash"
                self.kill_bullet(b)
                # mark it for redrawing
                b.redraw = True
                # it's now dead
                b.alive = False
                
    
    def draw(self,tkCanvas):
        # only draw those bullets which have changed
        for b in self.bullets:
            if(b.redraw):
                # move this line onto the screen in the right place
                tkCanvas.coords(b.m_lineId, b.startX, b.startY, b.endX, b.endY)
                tkCanvas.itemconfig(b.m_lineId, fill=b.colour)
                # mark this line as "redrawn"
                b.redraw = False


    def fire_bullet(self,start_x,start_y,end_x,end_y,colour="#FFFF00"):
        # find first dead bullet
        for b in self.bullets:
            if(b.alive):
                continue
            # initialise this bullet
            b.startX = start_x
            b.startY = start_y
            b.endX = end_x
            b.endY = end_y
            b.colour = colour
            b.alive = True
            b.redraw = True
            # add this bullet onto the "new bullet" queue to be processed
            self.newBulletQueue.put(b)
            return
            
    

    '''
    This method is a "helper method", to quickly reset the position
    of a bullet
    '''
    def kill_bullet(self, bullet):
        bullet.startX = -1
        bullet.startY = -1
        bullet.endX = -1
        bullet.endY = -1
        
        
    

    
