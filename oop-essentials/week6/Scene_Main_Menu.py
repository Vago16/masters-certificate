import pygame
import pygwidgets
import pyghelpers
import sys
from Constants import *

class Scene_Main_Menu(pyghelpers.Scene):
    #starting menu scene
    def __init__(self, window):
        #initialize the scene
        self.window = window
        self.title = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2 -140, 120), 'PONG', fontSize=120, textColor=GREEN)  #title on main screen
        self.name_label = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2 -100, 400), 'Enter your name:', fontSize=30) #tells user to input name
        self.name_input = pygwidgets.InputText(window, (WINDOW_WIDTH//2 -120, 450), fontSize=30)  #where user is to input name
        self.start_button = pygwidgets.TextButton(window, (WINDOW_WIDTH//2 -75, 500), 'Start!', fontSize=30)
        self.rules1 = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2-150, 240), 'Use the mouse to move the paddle', fontSize=30)
        self.rules2 = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2-150, 280), 'Keep the ball from going past your paddle', fontSize=30)
        self.rules3 = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2-150, 320), 'Score 5 points to win!', fontSize=30)
        
    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.start_button.handleEvent(event):
                name = self.name_input.getText().strip()    #get name from input
                if name:    #only proceed to next scene if name has been entered
                    self.goToScene(SCENE_PLAY, name)
            self.name_input.handleEvent(event)

    def draw(self):
        self.window.fill(LIGHT_GRAY)
        self.title.draw()
        self.name_label.draw()
        self.name_input.draw()
        self.start_button.draw()
        self.rules1.draw()
        self.rules2.draw()
        self.rules3.draw()

    def getSceneKey(self):

        return SCENE_MAIN_MENU