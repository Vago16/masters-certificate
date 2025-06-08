import pygame
from pygame.locals import *

BLACK = (0,0,0)

class TextInputBox:
    def __init__(self, x, y, w, h, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('black')
        self.text = ''
        self.font = font
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:        #if box was clicked
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:     #enables backspace to remove a character
                self.text = self.text[:-1]
            elif event.key != pygame.K_RETURN:      #adds character typed to display
                self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)     
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text