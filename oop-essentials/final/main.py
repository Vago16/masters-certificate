import pygame
import pyghelpers
import sys
from Constants import *
from Classes import *
from Scene_Main_Menu import *
from Scene_Play import *
from Scene_Summary import *
from Scene_Play import *
from Scene_Add import *
from Scene_Results import *

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
pygame.display.set_caption("Wattville Simulation")

scenesDict = {SCENE_MAIN_MENU : Scene_Main_Menu(window),
              SCENE_SUMMARY : Scene_Summary(window),
              SCENE_PLAY : Scene_Play(window),
              SCENE_ADD : Scene_Add(window),
              SCENE_RESULTS : Scene_Results(window)}

oSceneManager = pyghelpers.SceneMgr(scenesDict, FRAMES_PER_SECOND)

oSceneManager.run()

'''while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(GRAY)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)'''