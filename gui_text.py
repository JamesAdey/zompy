from gameobject import *
# we need the alignment options from this library
# import tkinter under an alias "tk"
import tkinter as tk

class GUIText(GameObject):

    text = "BLAH"
    baseText = "BASE"
    fullText = "Score:"
    textChanged = False
    
    m_textId = None

    def __init__(self,x=0,y=0,baseText="BASE"):
        super().__init__()
        self.x = x
        self.y = y
        self.baseText = baseText
        # call our set_text method to update the text
        self.set_text(self.text)

    def setup_gfx(self, tkCanvas):
        # create the text offet
        self.m_textId = tkCanvas.create_text(self.x,self.y,text=self.text,anchor=tk.NW)

    def remove_gfx(self,tkCanvas):
        tkCanvas.delete(self.m_textId)

    def draw(self,tkCanvas):

        # only reposition and reconfigure the item if the text has changed
        # this is to minimise the overhead in reconfiguring the text to draw
        if(self.textChanged):
            tkCanvas.coords(self.m_textId,self.x,self.y)
            tkCanvas.itemconfigure(self.m_textId,text=self.fullText)
            self.textChanged = False

    '''
    Helper function to set the text variables
    '''
    def set_text(self,newText):
        self.text = newText
        self.fullText = self.baseText+newText
        self.textChanged= True
