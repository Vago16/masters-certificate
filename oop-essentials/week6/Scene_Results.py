import pygame
import pygwidgets
import pyghelpers
import sys
from Constants import *

class Scene_Results(pyghelpers.Scene):
    #shows results
    def __init__(self, window):
        #initialize the scene
        self.window = window
        self.message_text = None
        self.play_again_button = pygwidgets.TextButton(window, (WINDOW_WIDTH//2 - 90, 400),'Play Again', fontSize=30)
        self.menu_button = pygwidgets.TextButton(window, (WINDOW_WIDTH//2 - 90, 470), 'Main Menu', fontSize=30)

    def enter(self, scoreDict):
        # scoreDict came from Game scene
        winner = max(scoreDict, key=lambda k: scoreDict[k])
        self.message_text = pygwidgets.DisplayText(
            self.window, (WINDOW_WIDTH//2 - 150, 200),
            '{0} wins!'.format(winner), fontSize=60, textColor=GREEN)

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.play_again_button.handleEvent(event):
                self.goToScene(SCENE_PLAY, 'Player')   # reuse existing name or ask again
            if self.menu_button.handleEvent(event):
                self.goToScene(SCENE_MAIN_MENU)


    def draw(self):
        self.window.fill(BLACK)
        self.message_text.draw()
        self.play_again_button.draw()
        self.menu_button.draw()

    def getSceneKey(self):
        return SCENE_RESULTS