from engine import *
from bullet_manager import *
from gameworld import *
from item_manager import *
from navgrid import *
from game_manager import *
from gui_text import *

# these are not a class currently
# but a suite of helper methods
import level_random
import level_cross
import level_test

class ZompyGlobals(GameGlobals):
    zoms = 10
    bulletManager = None
    gameManager = None
    itemManager = None
    gameWorld = None
    navGrid = None
    # list of players
    players = []

class ZompyEngine(GameEngine):

    def __init__(self):
        super().__init__()

    def make_globals(self):
        return ZompyGlobals(self)

    def setup_game(self,gGlobals):

        # create a gameworld
        gw = GameWorld()
        gGlobals.gameWorld = gw
        
        # create the managers for the game
        bm = BulletManager()
        gGlobals.bulletManager = bm
        super().add_game_object(bm)

        im = ItemManager()
        gGlobals.itemManager = im
        super().add_game_object(im)

        gm = GameManager()
        gGlobals.gameManager = gm
        super().add_game_object(gm)

        # create a nav grid
        ng = NavGrid(resolution=20)
        super().add_game_object(ng)
        gGlobals.navGrid = ng

        # configure the Graphical User Interface
        self.setup_ui(gGlobals)

        # Now decide which level to create and start it
        levelName = "test"

        if(levelName == "random"):
            level_random.create_level(super(),gGlobals)
        elif(levelName == "cross"):
            level_cross.create_level(super(),gGlobals)
        elif(levelName ==  "test"):
            level_test.create_level(super(),gGlobals)
        else:
            print("ERROR Could not create level!")
            
    def setup_ui(self,gGlobals):
        # create a score gui and link it to the game manager
        scoreText = GUIText(x=10,y=10,baseText="Score: ")
        gGlobals.gameManager.set_score_gui(scoreText)
        scoreText.set_text("0")
        super().add_game_object(scoreText)

        # create a health gui and link it to the game manager
        healthText = GUIText(x=10,y=30,baseText="P1 HP: ")
        gGlobals.gameManager.set_health_gui(1, healthText)
        healthText.set_text("100")
        super().add_game_object(healthText)

        healthText = GUIText(x=10,y=50,baseText="P2 HP: ")
        gGlobals.gameManager.set_health_gui(2, healthText)
        healthText.set_text("100")
        super().add_game_object(healthText)
