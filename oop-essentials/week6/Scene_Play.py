import pygame
import pygwidgets
import pyghelpers
import sys
from Constants import *

class Scene_Play(pyghelpers.Scene):
    #starting the game
    #initialize constants for ball and paddle
    PADDLE_WIDTH = 20
    PADDLE_HEIGHT = 120
    BALL_RADIUS = 12
    PADDLE_SPEED = 15   #pixels per frame when the CPU goes after the ball
    BALL_SPEED = 10

    def __init__(self, window):
        #initialize the scene
        self.window = window
        self._create_objects()
    
    def handleInputs(self, events, keyPressedList):
        mouseX, mouseY = pygame.mouse.get_pos() #x and y coordinates of mouse
        self.playerPaddle.centery = mouseY

        for event in events:
            if event.type == pygame.MOUSEMOTION:
                pass   #handled above with get_pos
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #press escape to stop playing and got to scores
                self.goToScene(SCENE_RESULTS, self.scores)
    
    def update(self):
        #ball mechanics
        self.ball.move_ip(self.ballDirX * self.BALL_SPEED,
                          self.ballDirY * self.BALL_SPEED)

        #makes it so ball bounces upon hitting top or bottom of window
        if self.ball.top <= 0 or self.ball.bottom >= WINDOW_HEIGHT:
            self.ballDirY *= -1

        #makes it so ball bounces upon colliding with paddles
        if self.ball.colliderect(self.playerPaddle) and self.ballDirX < 0:
            self.ballDirX *= -1
        if self.ball.colliderect(self.cpuPaddle) and self.ballDirX > 0:
            self.ballDirX *= -1

        #controls CPU paddle
        if self.cpuPaddle.centery < self.ball.centery:
            self.cpuPaddle.centery += min(self.PADDLE_SPEED,
                                         self.ball.centery - self.cpuPaddle.centery)
        else:
            self.cpuPaddle.centery -= min(self.PADDLE_SPEED,
                                         self.cpuPaddle.centery - self.ball.centery)

        #score checking
        if self.ball.right < 0:
            self.scores['CPU'] += 1
            self._reset_round()
        elif self.ball.left > WINDOW_WIDTH:
            self.scores[self.playerName] += 1
            self._reset_round()

        #Ends game when score reaches the specified value, in this case 5
        if max(self.scores.values()) >= 5:
            self.goToScene(SCENE_RESULTS, self.scores)

        
    def draw(self):
        self.window.fill(BLACK)
        pygame.draw.rect(self.window, WHITE, self.playerPaddle)
        pygame.draw.rect(self.window, WHITE, self.cpuPaddle)
        pygame.draw.circle(self.window, WHITE, self.ball.center, self.BALL_RADIUS)

        #draw center line
        for y in range(0, WINDOW_HEIGHT, 40):
            pygame.draw.line(self.window, GRAY, (WINDOW_WIDTH//2, y))

        #draw score
        font = pygame.font.SysFont(None, 36)
        scoreText = "{0}: {1}   CPU: {2}".format(self.playerName, self.scores[self.playerName], self.scores['CPU'])
        textSurf = font.render(scoreText, True, GREEN)
        self.window.blit(textSurf, (WINDOW_WIDTH//2 - textSurf.get_width()//2, 30))

    def _create_objects(self):
        #instantiate the objects(ball and paddles) to be drawn along with their specifications
        self.playerPaddle = pygame.Rect(40, WINDOW_HEIGHT//2 - self.PADDLE_HEIGHT//2,
                                        self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        
        self.cpuPaddle = pygame.Rect(WINDOW_WIDTH - 60,
                                    WINDOW_HEIGHT//2 - self.PADDLE_HEIGHT//2,
                                    self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        
        self.ball = pygame.Rect(WINDOW_WIDTH//2 - self.BALL_RADIUS,
                                WINDOW_HEIGHT//2 - self.BALL_RADIUS,
                                self.BALL_RADIUS*2, self.BALL_RADIUS*2)
        
        self.ballDirX, self.ballDirY = 1, 1
        self.scores = {'CPU': 0, 'Player': 0}

    def _reset_round(self):
        self.ball.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.ballDirX *= -1                      # send ball in opposite direction of last course(ie towards last person who scored)
        self.ballDirY *= -1