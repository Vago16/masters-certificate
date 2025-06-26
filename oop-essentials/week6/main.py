import pygame
import pygwidgets
import pyghelpers
import sys
from Constants import *

from Scene_Main_Menu import Scene_Main_Menu
from Scene_Play import Scene_Play
from Scene_Results import Scene_Results

# 2 - Initialize the world
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
font = pygame.font.SysFont("None", 30)
pygame.display.set_caption("Pong Game")

#instantiate all scenes and store them into a list
scenesList = [Scene_Main_Menu(window),
              Scene_Play(window),
              Scene_Results(window)]

#create the scene manager class and pass in the list of all the scenes to be run, along with frames per second
oSceneManager = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

#tell the scene manager to start running
oSceneManager.run()

while True:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Update the window
    pygame.display.update()

    #Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait