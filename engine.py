import time
import queue
from mainwindow import *
from gameobject import *



class GameGlobals (object):
    frameNum = None
    realTime = None
    engine = None

    def __init__(self,gameEngine):
        engine = gameEngine


class GameEngine(object):

    rootTk = None
    mainWindow = None

    gGlobals = None
    deltaTime = int(1000/30)
    startupTime = None

    aliveObjects = []
    addQueue = queue.Queue()
    removeQueue = queue.Queue()
    objectsToRemove = []

    def __init__(self):
        self.rootTk = Tk()
        self.rootTk.geometry("500x500")
        self.mainWindow = MainWindow(self.rootTk)

    def start_game(self):
        # create the globals
        self.gGlobals = self.make_globals()
        # tick... tock...
        self.startupTime = time.clock()
        self.gGlobals.frameNum = 0
        # setup the game
        self.setup_game(self.gGlobals)
        # RUN!!!!
        self.rootTk.after(self.deltaTime,self.run_game)
        self.rootTk.mainloop()

    def run_game(self):

        #self.killpython(self.now)
        #self.why?
        self.gGlobals.frameNum += 1
        self.gGlobals.realTime = time.clock() - self.startupTime

        while(not self.addQueue.empty()):
            obj = self.addQueue.get()
            obj.setup_gfx(self.mainWindow.canvas)
            obj.on_start(self.gGlobals)
            self.aliveObjects.append(obj)
        
        while(not self.removeQueue.empty()):
            obj = self.removeQueue.get()
            obj.remove_gfx(self.mainWindow.canvas)
            obj.on_remove(self.gGlobals)
            self.aliveObjects.remove(obj)
        
        for go in self.aliveObjects:
            go.update(self.gGlobals)

        for go in self.aliveObjects:
            go.draw(self.mainWindow.canvas)
        
        
        self.rootTk.after(self.deltaTime,self.run_game)     

    def add_game_object(self,gameObject):
        self.addQueue.put(gameObject)
        

    def remove_game_object(self,gameObject):
        self.removeQueue.put(gameObject)

    def setup_game(self,gGlobals):
        # do nothing
        pass

    def make_globals(self):
        return GameGlobals(self)
