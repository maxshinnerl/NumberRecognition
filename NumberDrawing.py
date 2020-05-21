import pygame, sys
from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((400, 400))  # window size

pygame.display.set_caption('Draw a Number')

WHITE = pygame.Color(255,255,255)  # save WHITE RGB code
BLACK = pygame.Color(0,0,0)
surface.fill(WHITE)  # make background white
 
while True: # main game loop

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()

    clicking = pygame.mouse.get_pressed()[0]  # func gets data for all mouse buttons
                                              # [0] gets only left click
    mpos = pygame.mouse.get_pos()
    #  surface.set_at((mpos), BLACK)

    if clicking == 1:

        surface.set_at((mpos), BLACK)
        #  print (mpos)
