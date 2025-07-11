import pygwidgets
import pyghelpers
from Constants import *

class Scene_Play(pyghelpers.Scene):
    #starting menu scene
    def __init__(self, window):
        #initialize the scene
        self.window = window

    def handleInputs(self, events, keyPressedList):
        return super().handleInputs(events, keyPressedList)
    
    def draw(self):
        self.window.fill(LIGHT_GRAY)

    def getSceneKey(self):
        return SCENE_PLAY