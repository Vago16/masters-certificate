import pygame
import pygwidgets
import sys

#add in importing of classes

# Constants
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
FPS = 30

class Individual:
    def __init__(self, idx):
        self.id = idx
        self.name = ''
        self.last_name = ''
        self.address = ''
        self.vac_a = 0
        self.vac_b = 0
        self.vac_c = 0
        self.sympt_a = 0
        self.sympt_b = 0
        self.sympt_c = 0

    def fully_vaccinated_no_symptoms(self):
        return (self.vac_a and self.vac_b and self.vac_c) and not (self.sympt_a or self.sympt_b or self.sympt_c)

class Group:
    def __init__(self):
        self.individuals = [Individual(i) for i in range(3)]  # start with 3 individuals

    def add_individual(self):
        new_id = len(self.individuals)
        self.individuals.append(Individual(new_id))

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Vaccination Tracker with pygwidgets")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Data
group = Group()
current_index = 0

# Buttons using pygwidgets
btn_back = pygwidgets.TextButton(window, (20, 20), 'Back')
btn_next = pygwidgets.TextButton(window, (120, 20), 'Next')
btn_add = pygwidgets.TextButton(window, (220, 20), 'Add New')
btn_save = pygwidgets.TextButton(window, (320, 20), 'Save')
btn_reset = pygwidgets.TextButton(window, (420, 20), 'Reset')
btn_report = pygwidgets.TextButton(window, (520, 20), 'Report')
btn_quit = pygwidgets.TextButton(window, (620, 20), 'Quit')

# Input fields
input_name = pygwidgets.InputText(window, (150, 100), width=180)
input_last_name = pygwidgets.InputText(window, (400, 100), width=180)
input_address = pygwidgets.InputText(window, (150, 150), width=430)

# Toggle rectangles for vaccines and symptoms
vac_a_rect = pygame.Rect(150, 220, 30, 30)
vac_b_rect = pygame.Rect(190, 220, 30, 30)
vac_c_rect = pygame.Rect(230, 220, 30, 30)

sympt_a_rect = pygame.Rect(150, 270, 30, 30)
sympt_b_rect = pygame.Rect(190, 270, 30, 30)
sympt_c_rect = pygame.Rect(230, 270, 30, 30)

def draw_toggle_rect(rect, is_on):
    color = GREEN if is_on else RED
    pygame.draw.rect(window, color, rect)

def update_inputs(individual):
    input_name.setValue(individual.name)
    input_last_name.setValue(individual.last_name)
    input_address.setValue(individual.address)

def reset_inputs():
    input_name.setValue('')
    input_last_name.setValue('')
    input_address.setValue('')

def generate_report(group):
    report_lines = []
    for ind in group.individuals:
        status = "Fully vaccinated, no symptoms" if ind.fully_vaccinated_no_symptoms() else "Incomplete or symptoms"
        line = f"ID {ind.id+1}: {ind.name} {ind.last_name} | {status}"
        report_lines.append(line)
    return report_lines

update_inputs(group.individuals[current_index])

running = True
while running:
    window.fill(GRAY)

    # Draw all buttons
    btn_back.draw()
    btn_next.draw()
    btn_add.draw()
    btn_save.draw()
    btn_reset.draw()
    btn_report.draw()
    btn_quit.draw()

    # Draw labels
    window.blit(font.render("First Name:", True, BLACK), (50, 105))
    window.blit(font.render("Last Name:", True, BLACK), (320, 105))
    window.blit(font.render("Address:", True, BLACK), (50, 155))

    window.blit(font.render("Vaccines (A, B, C):", True, BLACK), (50, 230))
    window.blit(font.render("Symptoms (A, B, C):", True, BLACK), (50, 280))

    # Draw inputs
    input_name.draw()
    input_last_name.draw()
    input_address.draw()

    # Draw current individual info
    individual = group.individuals[current_index]
    title = f"Individual {current_index + 1} of {len(group.individuals)}"
    title_surf = font.render(title, True, BLACK)
    window.blit(title_surf, (50, 60))

    # Draw vaccine toggles
    draw_toggle_rect(vac_a_rect, individual.vac_a)
    draw_toggle_rect(vac_b_rect, individual.vac_b)
    draw_toggle_rect(vac_c_rect, individual.vac_c)

    # Draw symptom toggles
    draw_toggle_rect(sympt_a_rect, individual.sympt_a)
    draw_toggle_rect(sympt_b_rect, individual.sympt_b)
    draw_toggle_rect(sympt_c_rect, individual.sympt_c)

    # Draw vaccination indicator circle (green if fully vaccinated & no symptoms, else red)
    indicator_color = GREEN if individual.fully_vaccinated_no_symptoms() else RED
    pygame.draw.circle(window, indicator_color, (700, 60), 20)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Buttons
        if btn_back.handleEvent(event):
            current_index = (current_index - 1) % len(group.individuals)
            update_inputs(group.individuals[current_index])

        if btn_next.handleEvent(event):
            current_index = (current_index + 1) % len(group.individuals)
            update_inputs(group.individuals[current_index])

        if btn_add.handleEvent(event):
            group.add_individual()
            current_index = len(group.individuals) - 1
            update_inputs(group.individuals[current_index])

        if btn_save.handleEvent(event):
            # Save input to individual
            individual.name = input_name.getValue()
            individual.last_name = input_last_name.getValue()
            individual.address = input_address.getValue()

        if btn_reset.handleEvent(event):
            reset_inputs()
            individual = group.individuals[current_index]
            individual.name = ''
            individual.last_name = ''
            individual.address = ''
            individual.vac_a = 0
            individual.vac_b = 0
            individual.vac_c = 0
            individual.sympt_a = 0
            individual.sympt_b = 0
            individual.sympt_c = 0

        if btn_report.handleEvent(event):
            # Show report in console for now
            print("----- Vaccination Report -----")
            for line in generate_report(group):
                print(line)
            print("------------------------------")

        if btn_quit.handleEvent(event):
            running = False

        # Inputs
        input_name.handleEvent(event)
        input_last_name.handleEvent(event)
        input_address.handleEvent(event)

        # Toggle clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if vac_a_rect.collidepoint(pos):
                individual.vac_a = 1 - individual.vac_a
            elif vac_b_rect.collidepoint(pos):
                individual.vac_b = 1 - individual.vac_b
            elif vac_c_rect.collidepoint(pos):
                individual.vac_c = 1 - individual.vac_c
            elif sympt_a_rect.collidepoint(pos):
                individual.sympt_a = 1 - individual.sympt_a
            elif sympt_b_rect.collidepoint(pos):
                individual.sympt_b = 1 - individual.sympt_b
            elif sympt_c_rect.collidepoint(pos):
                individual.sympt_c = 1 - individual.sympt_c

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()