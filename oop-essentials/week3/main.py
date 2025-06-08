# Module 2  Assignment
# Main file
# Evagelos Petropoulos
# U75564437


# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
from classes import *
from TextBox import *
import sys

# Define constants
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
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
    name_window =font.render(name_text, True, BLACK)    #render name
    window.blit(name_window, (200,60))      #show name on window

    #show vaccine statuses of individual(added names to vaccine to make easier to differentiate(also in alphabetical order))
    vac_a_text = "Vaccine A (Johnson): {}".format(individual.vac_a)
    vac_b_text = "Vaccine B (Moderna): {}".format(individual.vac_b)
    vac_c_text = "Vaccine C (Pfizer): {}".format(individual.vac_c)

    vac_a_window =font.render(vac_a_text, True, BLACK)
    vac_b_window =font.render(vac_b_text, True, BLACK)
    vac_c_window =font.render(vac_c_text, True, BLACK)

    window.blit(vac_a_window, (100, 80))
    window.blit(vac_b_window, (100, 100))
    window.blit(vac_c_window, (100, 120))

    sympt_a_text = "Symptom A (Coughing): {}".format(individual.sympt_a)
    sympt_b_text = "Symptom B (Fever): {}".format(individual.sympt_b)
    sympt_c_text = "Symptom C (Nausea): {}".format(individual.sympt_c)

    sympt_a_window =font.render(sympt_a_text, True, BLACK)
    sympt_b_window =font.render(sympt_b_text, True, BLACK)
    sympt_c_window =font.render(sympt_c_text, True, BLACK)

    window.blit(sympt_a_window, (400, 80))
    window.blit(sympt_b_window, (400, 100))
    window.blit(sympt_c_window, (400, 120))

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
