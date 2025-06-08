# Module 2  Assignment
# Main file
# Evagelos Petropoulos
# U75564437


# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
from classes import *
import sys

# Define constants
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 150
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
font = pygame.font.SysFont("None", 30)

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

group = Group()    #create instance of group class 
current_index = 0       #track the individual in the group that is selected


#create instances of back and next buttons
prev_button = SimpleButton(window, 20, 20, 80, 30, "Back", font)
next_button = SimpleButton(window, 120, 20, 80, 30, "Next", font)

# 6 - Loop forever
while True:
    window.fill(GRAY)

    #draw the buttons
    prev_button.draw()
    next_button.draw()

    individual = group.individuals[current_index]   #get current individual from the group
    #show name of individual
    name_text = "Individual {0}: {1} {2}".format(current_index + 1, 
                                                 individual.name, 
                                                 individual.last_name)
    name_window =font.render(name_text, True, BLACK)
    window.blit(name_window, (200,60))


    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if prev_button.is_clicked(event.pos):
                current_index = (current_index - 1) % len(group.individuals)
            if next_button.is_clicked(event.pos):
                current_index = (current_index + 1) % len(group.individuals)
        
    

    #Update the window
    pygame.display.update()

    #Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
