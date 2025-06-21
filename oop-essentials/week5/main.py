# Module 5 Assignment
# Main file
# Added Timer and Animation along with previous specifications
# Evagelos Petropoulos
# U75564437


# 1 - Import packages
import pygame
import pygwidgets
from pygame.locals import *
from classes import *
from TextBox import *
import sys

# Define constants
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 1150
WINDOW_HEIGHT = 800
FRAMES_PER_SECOND = 30 
NO_ACTIVITY = 5000 #5 seconds or 5000 milliseconds

# 2 - Initialize the world
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
font = pygame.font.SysFont("None", 30)

#3 define functions
def save_data(individual):
    #save input data into attributes using setters
    individual.set_name(input_name.get_text())
    individual.set_last_name(input_last_name.get_text())
    individual.set_address(input_address.get_text())

def add_ind():
    #add button appends a new individual to the list, ready to put in data
    new_ind = Individual(len(group.get_individuals()), '', '', '')
    group.add_individual(new_ind)
    input_name.set_text('') #pygwidgets
    input_last_name.set_text('')
    input_address.set_text('')

def button_handle():
    #gets individual's information when pressing respective button for prev/next
    input_name.set_text(individual.get_name())
    input_last_name.set_text(individual.get_last_name())
    input_address.set_text(individual.get_address())


def toggle_to_text(val):
    #change binary to yes/no
    if val:
        return "Yes"
    else:
        return "No"
    
def turns_green(i):
    #turns circle green if individual has all three vaccines and no symptoms
    #the variable i in this function stands for individual
    if (i.get_vac_a() == True and i.get_vac_b() == True and i.get_vac_c() == True) and \
       (i.get_sympt_a() != True and i.get_sympt_b() != True and i.get_sympt_c() != True):
        return True
    return False

def hide_other_fields():
        #turn flags off for other output fields(ie make them invisible)
        global v_active
        global r_active
        global report_vacc_status_is_visible
        global report_sympt_is_visible

        v_active = False
        r_active = False
        report_vacc_status_is_visible = False
        report_sympt_is_visible = False

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

group = Group()    #create instance of group class 
current_index = 0       #track the individual in the group that is selected

#create variables for -v button (initially hidden)
v_input_box = TextBox(500, 400, 200, 30, font)
v_active = False
report_vacc_status_is_visible = False
report_vacc_status_surfaces = []

#create variables -r first button(initially hidden)
r_input_box = TextBox(500, 350, 200, 30, font)  
r_active = False
r_output_surfaces = []

#create variables -s first button(initially hidden)
report_sympt_surfaces = []
report_sympt_is_visible = False

#create instances of back and next buttons
prev_button = pygwidgets.TextButton(window, (20, 20), "Back", width=80, height=30)
next_button = pygwidgets.TextButton(window, (120, 20), "Next", width=80, height=30)

#create instance of save button
save_button = pygwidgets.TextButton(window, (220, 20), "Save", width=80, height=30)

#create instance of add button for new individuals; after pressing, have to select next button to navigate to instance of individual created
add_button = pygwidgets.TextButton(window, (320, 20), "Add New", width=100, height=30)

#create instance of report vacc status button
report_vacc_status_button = pygwidgets.TextButton(window, (40, 350), "r– report vacc data", width=200, height=20)

#create instance of report vacc totals button
report_vacc_total_button = pygwidgets.TextButton(window, (40, 400), "v– report vacc total", width=200, height=20)

#create instance of report symptom button
report_sympt_button = pygwidgets.TextButton(window, (40, 450), "s–report sympt total", width=200, height=20)

#create instance of reset button
reset_button = pygwidgets.TextButton(window, (40, 500), "r– resets statuses", width=200, height=20)

#create instance of quit button
quit_button = pygwidgets.TextButton(window, (40, 550), "q- quit program", width=200, height=20)

#create instances of vaccine buttons to toggle status
vac_a_button = pygwidgets.TextButton(window, (360, 80), "", width=20, height=20)
vac_b_button = pygwidgets.TextButton(window, (360, 100), "", width=20, height=20)
vac_c_button = pygwidgets.TextButton(window, (360, 120), "", width=20, height=20)

#create instances of symptom buttons to toggle status
sympt_a_button = pygwidgets.TextButton(window, (680, 80), "", width=20, height=20)
sympt_b_button = pygwidgets.TextButton(window, (680, 100), "", width=20, height=20)
sympt_c_button = pygwidgets.TextButton(window, (680, 120), "", width=20, height=20)

#create instances of textboxes for input
input_name = TextBox(150, 300, 140, 30, font)
input_last_name = TextBox(350, 300, 140, 30, font)
input_address = TextBox(550, 300, 200, 30, font)

#list of TextBox instances
input_boxes = [input_name, input_last_name, input_address]

#puts the info from textboxes into the attributes (use getters)
individual = group.get_individual(current_index)
input_name.set_text("First Name")
input_last_name.set_text("Last Name")
input_address.set_text("Address")

#labels for TextBox instances
name_label = font.render("Name:", True, BLACK)
last_name_label = font.render("Last Name:", True, BLACK)
address_label = font.render("Address:", True, BLACK)

#create variables for TIMER
last_activity_time = pygame.time.get_ticks()
show_message = False

#ANIMATION with images
fireworkAnimation = pygwidgets.SpriteSheetAnimation(window, (700, 45), 'images/fireworks.png',
                                         35, 192, 192, .1, autoStart=False, loop=False)


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

    individual = group.get_individual(current_index)   #get current individual from the group
    #show name of individual using getters
    name_text = "Individual {0}: {1} {2}".format(current_index + 1, 
                                                 individual.get_name(), 
                                                 individual.get_last_name())
    name_window =font.render(name_text, True, BLACK)    #render name
    window.blit(name_window, (200,60))      #show name on window

    #show vaccine statuses of individual(added names to vaccine to make easier to differentiate(also in alphabetical order)) using getters
    vac_a_text = "Vaccine A (Johnson): {}".format(toggle_to_text(individual.get_vac_a()))
    vac_b_text = "Vaccine B (Moderna): {}".format(toggle_to_text(individual.get_vac_b()))
    vac_c_text = "Vaccine C (Pfizer): {}".format(toggle_to_text(individual.get_vac_c()))

    vac_a_window = font.render(vac_a_text, True, BLACK)
    vac_b_window = font.render(vac_b_text, True, BLACK)
    vac_c_window = font.render(vac_c_text, True, BLACK)

    window.blit(vac_a_window, (100, 80))
    window.blit(vac_b_window, (100, 100))
    window.blit(vac_c_window, (100, 120))

    #show symptom statuses of individual(added names to symptoms to make easier to differentiate(also in alphabetical order)) using getters
    sympt_a_text = "Symptom A (Coughing): {}".format(toggle_to_text(individual.get_sympt_a()))
    sympt_b_text = "Symptom B (Fever): {}".format(toggle_to_text(individual.get_sympt_b()))
    sympt_c_text = "Symptom C (Nausea): {}".format(toggle_to_text(individual.get_sympt_c()))

    sympt_a_window = font.render(sympt_a_text, True, BLACK)
    sympt_b_window = font.render(sympt_b_text, True, BLACK)
    sympt_c_window = font.render(sympt_c_text, True, BLACK)

    window.blit(sympt_a_window, (400, 80))
    window.blit(sympt_b_window, (400, 100))
    window.blit(sympt_c_window, (400, 120))

    #add labels for input
    window.blit(name_label, (150, 255))
    window.blit(last_name_label, (350, 255))
    window.blit(address_label, (550, 255))

    #draw textboxes
    for box in input_boxes:
        box.draw(window)

    #if inacivity is longer than 5 seconds, display message
    if show_message == True:
        inactivity_message = font.render("Please Enter Data - no input detected", True, RED)
        window.blit(inactivity_message, (600, 30))

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:    #registers key being pressed
            if event.key == pygame.K_v:
                v_active = not v_active  #show the textbox for -v key
            if event.key == pygame.K_r:
                r_active = not r_active  # Toggle display of the r_input_box

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:    #registers key or mouse being pressed
            last_activity_time = pygame.time.get_ticks()
            show_message = False

        #buttons to toggle vaccines
        if vac_a_button.handleEvent(event):        #toggle vaccine status using getters/setters
            individual.set_vac_a(1 - individual.get_vac_a())  #flip between 0 and 1
        if vac_b_button.handleEvent(event):  
            individual.set_vac_b(1 - individual.get_vac_b())
        if vac_c_button.handleEvent(event):  
            individual.set_vac_c(1 - individual.get_vac_c())
        #buttons to toggle symptom
        if sympt_a_button.handleEvent(event):      #toggle symptom status using getters/setters
            individual.set_sympt_a(1 - individual.get_sympt_a())
        if sympt_b_button.handleEvent(event):  
            individual.set_sympt_b(1 - individual.get_sympt_b())
        if sympt_c_button.handleEvent(event):  
            individual.set_sympt_c(1 - individual.get_sympt_c())  

        #top line of GUI buttons
        if prev_button.handleEvent(event):   #go to previous individual, wraps around
            current_index = (current_index - 1) % len(group.get_individuals())
            individual = group.get_individual(current_index)
            button_handle() #refactored code into function to improve readability

        if next_button.handleEvent(event):   #go to next individual, wraps around
            current_index = (current_index + 1) % len(group.get_individuals())
            individual = group.get_individual(current_index)
            button_handle()

        if save_button.handleEvent(event):   #save button saves input
            save_data(individual)

        if add_button.handleEvent(event):    #add button adds a new indiviudal    
            add_ind()

        #left column of function buttons
        if report_vacc_status_button.handleEvent(event):
            hide_other_fields() #makes other fields invisible
            r_active = True     #makes textbox visible
            r_output_surfaces = []  #clear input

            try:
                num = int(r_input_box.get_text())
                if 1 <= num <= len(group.get_individuals()):
                    indiv = group.get_individual(num - 1)
                    r_output_text = indiv.report_individual_vacc()
                    r_output_lines = r_output_text.split('\n')
                    for line in r_output_lines:     #write to GUI
                        surface = font.render(line, True, BLACK)
                        r_output_surfaces.append(surface)
                else:
                    r_output_surfaces = [font.render("Number inputted is out of range", True, RED)]
            except ValueError:
                r_output_surfaces = [font.render("Click the button again to generate report of a valid individual.", True, RED)]

        if report_vacc_total_button.handleEvent(event):
            report_vacc_status_lines = group.report_total_vacc()
            hide_other_fields() #makes other fields invisible
            report_vacc_status_surfaces = []
            for line in report_vacc_status_lines:   #goes thru each elemetn in report_total_vacc list
                now_rendered = font.render(line, True, BLACK)
                report_vacc_status_surfaces.append(now_rendered)
            report_vacc_status_is_visible = True  #sets it so text can be written later 

        if report_sympt_button.handleEvent(event):  
            hide_other_fields() #makes other fields invisible  
            report_sympt_lines = group.report_symptoms_per_vacc()
            report_sympt_surfaces = []
            for line in report_sympt_lines:
                line_surface = font.render(line, True, BLACK)
                report_sympt_surfaces.append(line_surface)
            report_sympt_is_visible = True

        if reset_button.handleEvent(event):
            group.reset()

        if quit_button.handleEvent(event):   #q button quits the window
            pygame.quit()
            sys.exit()

        #handle events in boxes
        for box in input_boxes:
            box.handle_event(event)

        if r_active:        # allows r textbox to handle input
            r_input_box.handle_event(event)  

        if v_active:        #allows v textbox to handle input
            v_input_box.handle_event(event)  


    if report_vacc_status_is_visible == True:
        y = 400
        for i in report_vacc_status_surfaces:     #iterates through and prints output to GUI, each line down by a set amount
            window.blit(i, (500, y))
            y += 30

        
    #check if circle should be green, and draw accordingly
    if turns_green(individual) == True:
        pygame.draw.circle(window, GREEN, (180, 70), 10)
        fireworkAnimation.start()
        fireworkAnimation.update()       #added in firework ANIMATION when all vaccines are filled in
        fireworkAnimation.draw()
    else:
        pygame.draw.circle(window, RED, (180, 70), 10)
        fireworkAnimation.stop()     #stops animation

    if v_active == True:    #draws the textbox if its corresponding button has been pressed
        v_input_box.draw(window)

    if r_active:
        r_input_box.draw(window)
        generate_report = font.render('Click the button again to generate report', True, BLACK)
        y = 400  # Adjust vertical position
        for line_surface in r_output_surfaces:
            window.blit(line_surface, (500, y))  #draw and go down by 30 for each iterable
            y += 30

    if report_sympt_is_visible:
        y = 400
        for surface in report_sympt_surfaces:
            window.blit(surface, (750, y))  #draw and go down by 30 for each iterable
            y += 30

    #checking if inactivity has passed the threshold for message to appear
    curr_time = pygame.time.get_ticks()
    if curr_time - last_activity_time > NO_ACTIVITY:    
        #if the difference of the ticks in current time and the last time any 
        #activity(click or button press) was registered is greater than 5000 milliseconds, show message
        show_message = True

    #Update the window
    pygame.display.update()

    #Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

