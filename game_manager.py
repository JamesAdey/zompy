from gameobject import *

class GameManager(GameObject):

    zombiesKilled = 0

    scoreGUI = None
    healthGUI = None

    def __init__(self,x=0,y=0):
        super().__init__()
        self.x = x
        self.y = y

    def on_start(self,gameGlobals):
        pass

    def on_remove(self, gameGlobals):
        pass

    def setup_gfx(self, tkCanvas):
        # game manager has no graphics
        pass

    def remove_gfx(self,tkCanvas):
        pass

    def update(self, gameGlobals):
        '''
        You could do some game round logic in here...
        Like checking the number of zombies killed and then spawning more
        '''
        pass

    def zombie_killed(self,zombie):
        '''
        You could do something here depending on what zombie was killed...
        ''' 
        # increase the number of zombies killed
        self.zombiesKilled += 1
        # update the gui text
        self.scoreGUI.set_text(str(self.zombiesKilled))

    def set_score_gui(self, newScoreGUI):
        self.scoreGUI = newScoreGUI

    def update_player_health(self,health):
        self.healthGUI.set_text(str(health))

    def set_health_gui(self,newHealthGUI):
        self.healthGUI = newHealthGUI
        
