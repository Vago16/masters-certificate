import pygwidgets
import pyghelpers
from Constants import *
from Classes import *



class Scene_Summary(pyghelpers.Scene):
    #starting menu scene
    def __init__(self, window):
        #initialize the scene
        self.window = window
        #self.budget = pygwidgets.DisplayText(window, (WINDOW_WIDTH//2 -120, 450), fontSize=30)
        self.next_button = pygwidgets.TextButton(window, (WINDOW_WIDTH//2 -75, 500), 'Go to Simulation!', fontSize=30)
        self.budget_text = pygwidgets.DisplayText(window, (50, 100), 'Budget is: {0}'.format(budget), fontSize=30)
        self.community_text = pygwidgets.DisplayText(window, (50, 150), 'Number of Communities: {0}'.format(num_comm), fontSize=30)

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.next_button.handleEvent(event):
                self.goToScene(SCENE_PLAY, (num_comm, budget))
    
    def draw(self):
        self.window.fill(LIGHT_GRAY)
        self.budget_text.draw()
        self.community_text.draw()
        self.next_button.draw()

    def getSceneKey(self):
        return SCENE_SUMMARY