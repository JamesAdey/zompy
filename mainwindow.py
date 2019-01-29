from tkinter import *
from gameobject import *

class MainWindow(Frame):

    canvas = None

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("ZomPY")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self, width=400, height=400,bg="#a0a080")
        self.canvas.pack()
