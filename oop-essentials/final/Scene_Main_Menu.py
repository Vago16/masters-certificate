import pygwidgets
import pyghelpers
from Constants import *
from Classes import *

class Scene_Main_Menu(pyghelpers.Scene):
    #starting menu scene
    def __init__(self, window):
        #initialize the scene
        self.window = window
        self.parameters1 = pygwidgets.DisplayText(window, (50, 50), 'LightningPower currently has 12 EV charging stations in various communities in the city of Wattville,', fontSize=30)
        self.parameters2 = pygwidgets.DisplayText(window,(50,80), 'and expects the addition of new charging stations with Level 3 capacity. Of the 12 EV charging stations currently active:', fontSize=30)
        self.parameters3 = pygwidgets.DisplayText(window,(50,110), '5 are rated at Level 2 and have capacity limit of 600 kWday (can serve 600 kW in a day),', fontSize=30)
        self.parameters4 = pygwidgets.DisplayText(window,(50,140), '7 are rated at Level 3, charging with capacity for 1,500 kWday   (can serve 1,500 kW in a day).', fontSize=30)
        self.parameters5 = pygwidgets.DisplayText(window,(50,170), 'Each community serves a random number of EVs, between 50 - 500', fontSize=30)
        self.parameters6 = pygwidgets.DisplayText(window,(50,200), 'The cost of each Level 2 charging station is $1,700 U.S. dollars,', fontSize=30)
        self.parameters7 = pygwidgets.DisplayText(window,(50,230), 'and the cost of Level 3 charging station is $42,000 U.S. dollars.', fontSize=30)
        self.community_label = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2 -100, 300), 'How many communities will you be looking at?(max 5, default 3)', fontSize=30)
        self.community_input = pygwidgets.InputText(window, (WINDOW_WIDTH//2 -120, 350), fontSize=30)
        self.budget_label = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2 -100, 400), 'Enter in your budget', fontSize=30)
        self.budget_input = pygwidgets.InputText(window, (WINDOW_WIDTH//2 -120, 450), fontSize=30)
        self.start_button = pygwidgets.TextButton(window, (WINDOW_WIDTH//2 -75, 500), 'Start!', fontSize=30)
        self.community_warning = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2 -100, 100), 'Please enter in a number between 0-5 for number of communities', fontSize=30, textColor=RED)
        self.budget_warning = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2 -100, 200), 'Please enter in a positive budget number', fontSize=30, textColor=RED)
        self.budget_text = pygwidgets.DisplayText(window, (50, 600), 'Budget is: {0}'.format(budget), fontSize=30)
        self.community_text = pygwidgets.DisplayText(window, (50, 700), 'Number of Communities: {0}'.format(num_comm), fontSize=30)

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.start_button.handleEvent(event):
                try:
                    num_comm = int(self.community_input.getValue().strip())  
                    if num_comm < 0 or num_comm > 5:
                        self.community_warning.draw()
                except:
                    num_comm = 3
                try:
                    budget = int(self.budget_input.getValue().strip()) 
                    if budget < 0:
                        self.budget_warning.draw()
                except:
                    self.budget_warning.draw()
                try:
                    if (num_comm > 0 and num_comm <= 5) and budget:   
                        self.budget_text.draw()
                        self.community_text
                        self.goToScene(SCENE_SUMMARY, (num_comm, budget))
                    else:
                        if num_comm < 0 or num_comm > 5 or budget < 0:
                            if num_comm < 0 or num_comm > 5:
                                self.community_warning.draw()
                            if budget < 0:
                                self.budget_warning.draw()
                except:
                    pass
            self.community_input.handleEvent(event)
            self.budget_input.handleEvent(event)
                

    def draw(self):
        self.window.fill(LIGHT_GRAY)
        self.parameters1.draw()
        self.parameters2.draw()
        self.parameters3.draw()
        self.parameters4.draw()
        self.parameters5.draw()
        self.parameters6.draw()
        self.parameters7.draw()
        self.community_label.draw()
        self.community_input.draw()
        self.budget_label.draw()
        self.budget_input.draw()
        self.start_button.draw()

    def getSceneKey(self):
        return SCENE_MAIN_MENU