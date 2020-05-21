import pygame, sys  # importing

from pygame.locals import *

pygame.init()  # initialize game

DISPLAYSURF = pygame.display.set_mode((400, 300))  # game window bounds

pygame.display.set_caption('Hello World!')  # set name of game (top of window)

# NOTE: Variations of the above should be included at the beginning of each pygame file
# NOTE: Top left of grid is 0, 0

while True: # main game loop

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()  # displays DISPLAYSURF variable
