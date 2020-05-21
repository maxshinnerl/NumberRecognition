#  Simple pygame allowing user to draw numbers with their mouse
#  Pixel data will be fed to machine learning (eventually)

import pygame, sys
from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((400, 400))  # window size

pygame.display.set_caption('Draw a Number | Right Click to Refresh')

WHITE = pygame.Color(255,255,255)  # save WHITE RGB code
BLACK = pygame.Color(0,0,0)
surface.fill(WHITE)  # make background white
 
while True: # main game loop

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()

    leftClicking = pygame.mouse.get_pressed()[0]  # func gets data for all mouse buttons
                                                  # [0] gets only left click

    rightClicking = pygame.mouse.get_pressed()[2] # get right click boolean

    mpos = pygame.mouse.get_pos()
    
    if leftClicking == 1:

        # Color 10 pixels in all directions from mouse when clicking
        for x in range(20):
            for y in range(20):
                surface.set_at((mpos[0] + x - 10, mpos[1] + y - 10), BLACK)

        # surface.set_at((mpos), BLACK)
   
    if rightClicking == 1:
        surface.fill(WHITE) 
