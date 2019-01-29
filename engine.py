import time
import queue
from mainwindow import *
from gameobject import *



class GameGlobals (object):
    frameNum = None
    realTime = None
    engine = None
    pressedKeys = None
    mouseInputs = None

    mouseX = 0
    mouseY = 0

    def __init__(self,gameEngine):
        self.engine = gameEngine
        self.pressedKeys = {}
        self.mouseInputs = {}

    '''
    This method is to reset the dictionary of pressed inputs
    every frame, so we don't keep holding down keys and mouse
    buttons that aren't pressed
    '''
    def clear_inputs(self):
        # run over the dictionaries and clear them
        for k in self.mouseInputs:
            self.mouseInputs[k] = False

    '''
    This method is to separate the tkinter based key events
    from the main game logic. Providing a common method to
    quickly check if keys are pressed.
    '''
    def is_key_pressed(self, keyChar):
        # check if we have a value for this key...
        if(keyChar in self.pressedKeys):
            return self.pressedKeys[keyChar]
        # otherwise return False, as this key hasn't been pressed
        return False

    '''
    This method is to separate the tkinter based mouse events
    from the main game logic. Providing a common method to
    quickly check if mouse buttons are pressed.
    '''
    def is_mouse_pressed(self, mouseButton):
        if(mouseButton in self.mouseInputs):
            return self.mouseInputs[mouseButton]

        return False

    def set_mouse_position(self,x,y):
        self.mouseX = x
        self.mouseY = y

    
    def get_mouse_position(self):
        return (self.mouseX,self.mouseY)


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
        # bind the listeners for mouse and key events
        self.rootTk.bind("<KeyPress>",self.key_press_callback)
        self.rootTk.bind("<KeyRelease>",self.key_release_callback)
        self.mainWindow.canvas.bind("<ButtonRelease-1>",self.mouse_left_release_callback)

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

        # add any new objects that enter the game
        while(not self.addQueue.empty()):
            obj = self.addQueue.get()
            obj.setup_gfx(self.mainWindow.canvas)
            obj.on_start(self.gGlobals)
            self.aliveObjects.append(obj)

        # clear any objects we need to remove
        while(not self.removeQueue.empty()):
            obj = self.removeQueue.get()
            obj.remove_gfx(self.mainWindow.canvas)
            obj.on_remove(self.gGlobals)
            self.aliveObjects.remove(obj)

        # update ALL of the objects!
        for go in self.aliveObjects:
            go.update(self.gGlobals)

        # draw ALL of the objects!
        for go in self.aliveObjects:
            go.draw(self.mainWindow.canvas)

        # reset the inputs for the next frame
        self.gGlobals.clear_inputs()

        # schedule another game loop
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

    def key_press_callback(self,event):
        if(event.char != ""):
            self.gGlobals.pressedKeys[event.char] = True

    def key_release_callback(self,event):
        if(event.char != ""):
            self.gGlobals.pressedKeys[event.char] = False

    def mouse_left_release_callback(self,event):
        self.gGlobals.mouseInputs["left"] = True
        self.gGlobals.set_mouse_position(event.x,event.y)
        
