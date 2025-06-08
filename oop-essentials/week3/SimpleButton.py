# SimpleButton class
#
# Uses a "state machine" approach
#

# SimpleButton.py
import pygame
from pygame.locals import *

class SimpleButton:
    def __init__(self, window, x, y, w, h, text, font):
        self.window = window
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self):
        pygame.draw.rect(self.window, (180, 180, 180), self.rect)  # button background
        pygame.draw.rect(self.window, (0, 0, 0), self.rect, 2)     # button border
        self.window.blit(self.text_surface, self.text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def handleEvent(self, eventObj):
        # This method will return True if user clicks the button.
        # Normally returns False.

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # The button only cares about mouse-related events
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True  # clicked!

            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    

