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
        self.title = pygwidgets.DisplayText(window, (600, 120), 'PONG', fontSize=60, textColor=GREEN)  #title on main screen
        self.name_label = pygwidgets.DisplayText(window, (500, 280), 'Enter your name:', fontSize=30) #tells user to input name
        self.name_input = pygwidgets.InputText(window, (650, 330), fontSize=30)  #where user is to input name
        self.start_button = pygwidgets.TextButton(window, (650, 450), 'Start!', fontSize=30)
        
    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.start_button.handleEvent(event):
                name = self.name_input.getText().strip()    #get name from input
                if name == True:    #only proceed to next scene if name has been entered
                    self.goToScene(SCENE_PLAY, name)
            self.name_input.handleEvent(event)

    def draw(self):
        self.window.fill(BLACK)
        self.title.draw()
        self.name_label.draw()
        self.name_input.draw()
        self.start_button.draw()