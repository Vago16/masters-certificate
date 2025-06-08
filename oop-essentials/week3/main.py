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

#create instance of save button
save_button = SimpleButton(window, 220, 20, 80, 30, "Save", font)

#creat instances of textboxes
input_name = TextBox(150, 300, 140, 30, font)
input_last_name = TextBox(350, 300, 140, 30, font)
input_address = TextBox(550, 300, 200, 30, font)

#list of TextBox instances
input_boxes = [input_name, input_last_name, input_address]

#puts the info from textboxes into the attributes
individual = group.individuals[current_index]
input_name.set_text(individual.name)
input_last_name.set_text(individual.last_name)
input_address.set_text(individual.address)

#labels for TextBox instances
name_label = font.render("Name:", True, BLACK)
last_name_label = font.render("Last Name:", True, BLACK)
address_label = font.render("Address:", True, BLACK)

# 6 - Loop forever
while True:
    window.fill(GRAY)

    #draw the buttons
    prev_button.draw()
    next_button.draw()
    save_button.draw()

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

    vac_a_window = font.render(vac_a_text, True, BLACK)
    vac_b_window = font.render(vac_b_text, True, BLACK)
    vac_c_window = font.render(vac_c_text, True, BLACK)

    window.blit(vac_a_window, (100, 80))
    window.blit(vac_b_window, (100, 100))
    window.blit(vac_c_window, (100, 120))

    #show symptom statuses of individual(added names to symptoms to make easier to differentiate(also in alphabetical order)
    sympt_a_text = "Symptom A (Coughing): {}".format(individual.sympt_a)
    sympt_b_text = "Symptom B (Fever): {}".format(individual.sympt_b)
    sympt_c_text = "Symptom C (Nausea): {}".format(individual.sympt_c)

    sympt_a_window = font.render(sympt_a_text, True, BLACK)
    sympt_b_window = font.render(sympt_b_text, True, BLACK)
    sympt_c_window = font.render(sympt_c_text, True, BLACK)

    window.blit(sympt_a_window, (400, 80))
    window.blit(sympt_b_window, (400, 100))
    window.blit(sympt_c_window, (400, 120))

    #add labels
    window.blit(name_label, (150, 255))
    window.blit(last_name_label, (350, 255))
    window.blit(address_label, (550, 255))

    #draw textboxes
    for box in input_boxes:
        box.draw(window)

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if save_button.is_clicked(event.pos):
                individual.name = input_name.get_text()
                individual.last_name = input_last_name.get_text()
                individual.address = input_address.get_text()

            if prev_button.is_clicked(event.pos):   #go to previous individual, if at index 0, goes to index 14
                current_index = (current_index - 1) % len(group.individuals)
                individual = group.individuals[current_index]
                input_name.set_text(individual.name)
                input_last_name.set_text(individual.last_name)
                input_address.set_text(individual.address)

            if next_button.is_clicked(event.pos):   #go to next individual, if at index 14, goes to index 0
                current_index = (current_index + 1) % len(group.individuals)
                individual = group.individuals[current_index]
                input_name.set_text(individual.name)
                input_last_name.set_text(individual.last_name)
                input_address.set_text(individual.address)
        #handle events in boxes
        for box in input_boxes:
            box.handle_event(event)
        

    #Update the window
    pygame.display.update()

    #Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
