# Module 3 Assignment
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
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
font = pygame.font.SysFont("None", 30)

#3 define functions
def save_data(individual):
    #save input data into attributes
    individual.name = input_name.get_text()
    individual.last_name = input_last_name.get_text()
    individual.address = input_address.get_text()

def add_ind():
    #add button appends a new individual to the list, ready to put in data
    new_ind = Individual(len(group.individuals), '', '', '')
    group.individuals.append(new_ind)
    input_name.set_text('')
    input_last_name.set_text('')
    input_address.set_text('')

def toggle_to_text(val):
    #change binary to yes/no
    if val:
        return "Yes"
    else:
        return "No"
    
def turns_green(i):
    #turns circle green if individual has all three vaccines and no symptoms
    #the variable i in this function stands for individual
    if (i.vac_a == True and i.vac_b == True and i.vac_c == True) and (i.sympt_a != True and i.sympt_b != True and i.sympt_c != True):
        return True
    return False

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

group = Group()    #create instance of group class 
current_index = 0       #track the individual in the group that is selected

#create instances of back and next buttons
prev_button = SimpleButton(window, 20, 20, 80, 30, "Back", font)
next_button = SimpleButton(window, 120, 20, 80, 30, "Next", font)

#create instance of save button
save_button = SimpleButton(window, 220, 20, 80, 30, "Save", font)

#create instance of add button for new individuals
add_button = SimpleButton(window, 320, 20, 100, 30, "Add New", font)

#create instance of report vacc status button
report_vacc_status_button = SimpleButton(window, 40, 350, 200, 20, "r– report vacc data", font)

#create instance of report vacc totals button
report_vacc_total_button = SimpleButton(window, 40, 400, 200, 20, "v– report vacc total", font)

#create instance of report symptom button
report_sympt_button = SimpleButton(window, 40, 450, 200, 20, "s–report sympt total", font)

#create instance of reset button
reset_button = SimpleButton(window, 40, 500, 200, 20, "r– resets statuses", font)

#create instance of quit button
quit_button = SimpleButton(window, 40, 550, 200, 20, "q- quit program", font)

#create instances of vaccine buttons to toggle status
vac_a_button = SimpleButton(window, 360, 80, 20, 20, None, font)
vac_b_button = SimpleButton(window, 360, 100, 20, 20, None, font)
vac_c_button = SimpleButton(window, 360, 120, 20, 20, None, font)

#create instances of symptom buttons to toggle status
sympt_a_button = SimpleButton(window, 680, 80, 20, 20, None, font)
sympt_b_button = SimpleButton(window, 680, 100, 20, 20, None, font)
sympt_c_button = SimpleButton(window, 680, 120, 20, 20, None, font)


#creat instances of textboxes
input_name = TextBox(150, 300, 140, 30, font)
input_last_name = TextBox(350, 300, 140, 30, font)
input_address = TextBox(550, 300, 200, 30, font)

#list of TextBox instances
input_boxes = [input_name, input_last_name, input_address]

#puts the info from textboxes into the attributes
individual = group.individuals[current_index]
input_name.set_text("First Name")
input_last_name.set_text("Last Name")
input_address.set_text("Address")

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
    add_button.draw()
    save_button.draw()
    vac_a_button.draw()
    vac_b_button.draw()
    vac_c_button.draw()
    sympt_a_button.draw()
    sympt_b_button.draw()
    sympt_c_button.draw()

    report_vacc_status_button.draw()
    report_vacc_total_button.draw()
    report_sympt_button.draw()
    reset_button.draw()
    quit_button.draw()

    individual = group.individuals[current_index]   #get current individual from the group
    #show name of individual
    name_text = "Individual {0}: {1} {2}".format(current_index + 1, 
                                                 individual.name, 
                                                 individual.last_name)
    name_window =font.render(name_text, True, BLACK)    #render name
    window.blit(name_window, (200,60))      #show name on window

    #show vaccine statuses of individual(added names to vaccine to make easier to differentiate(also in alphabetical order))
    vac_a_text = "Vaccine A (Johnson): {}".format(toggle_to_text(individual.vac_a))
    vac_b_text = "Vaccine B (Moderna): {}".format(toggle_to_text(individual.vac_b))
    vac_c_text = "Vaccine C (Pfizer): {}".format(toggle_to_text(individual.vac_c))

    vac_a_window = font.render(vac_a_text, True, BLACK)
    vac_b_window = font.render(vac_b_text, True, BLACK)
    vac_c_window = font.render(vac_c_text, True, BLACK)

    window.blit(vac_a_window, (100, 80))
    window.blit(vac_b_window, (100, 100))
    window.blit(vac_c_window, (100, 120))

    #show symptom statuses of individual(added names to symptoms to make easier to differentiate(also in alphabetical order)
    sympt_a_text = "Symptom A (Coughing): {}".format(toggle_to_text(individual.sympt_a))
    sympt_b_text = "Symptom B (Fever): {}".format(toggle_to_text(individual.sympt_b))
    sympt_c_text = "Symptom C (Nausea): {}".format(toggle_to_text(individual.sympt_c))

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

            if vac_a_button.is_clicked(event.pos):      #toggle vaccine status
                individual.vac_a = 1 - individual.vac_a  # Flip between 0 and 1
            if vac_b_button.is_clicked(event.pos):
                individual.vac_b = 1 - individual.vac_b
            if vac_c_button.is_clicked(event.pos):
                individual.vac_c = 1 - individual.vac_c

            if sympt_a_button.is_clicked(event.pos):    #toggle symptom status
                individual.sympt_a = 1 - individual.sympt_a
            if sympt_b_button.is_clicked(event.pos):
                individual.sympt_b = 1 - individual.sympt_b
            if sympt_c_button.is_clicked(event.pos):
                individual.sympt_c = 1 - individual.sympt_c

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

            if save_button.is_clicked(event.pos):   #save button saves input
                save_data(individual)

            if add_button.is_clicked(event.pos):    #add button adds a new indiviudal    
                add_ind()

            if reset_button.is_clicked(event.pos):
                group.reset()

            if quit_button.is_clicked(event.pos):   #q button quits the window
                pygame.quit()
                sys.exit()

        #handle events in boxes
        for box in input_boxes:
            box.handle_event(event)
        
    #check if circle should be green, and draw accordingly
    if turns_green(individual) == True:
        pygame.draw.circle(window, GREEN, (180, 70), 10)
    else:
        pygame.draw.circle(window, RED, (180, 70), 10)

    #Update the window
    pygame.display.update()

    #Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
