# Module 6 Assignment
# Main file
# Pong Game
# Evagelos Petropoulos
# U75564437


import pygame
import pyghelpers
from Constants import *

from Scene_Main_Menu import Scene_Main_Menu
from Scene_Play import Scene_Play
from Scene_Results import Scene_Results

# 2 - Initialize the world
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
pygame.display.set_caption("Pong Game")

#instantiate all scenes and store them into a list
scenesDict = {SCENE_MAIN_MENU : Scene_Main_Menu(window),
              SCENE_PLAY: Scene_Play(window),
              SCENE_RESULTS: Scene_Results(window)}

#create the scene manager class and pass in the list of all the scenes to be run, along with frames per second
oSceneManager = pyghelpers.SceneMgr(scenesDict, FRAMES_PER_SECOND)

#tell the scene manager to start running
oSceneManager.run()
