import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))  # window size

pygame.display.set_caption('Draw a Number')

WHITE = pygame.Color(255,255,255)  # save WHITE RGB code
BLACK = pygame.Color(0,0,0)
DISPLAYSURF.fill(WHITE)  # make background white
 
while True: # main game loop

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()
