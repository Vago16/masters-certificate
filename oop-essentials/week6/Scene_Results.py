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

    def draw(self):
        self.window.fill(BLACK)