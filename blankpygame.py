import pygame, sys
from pygmae.locals import *

pygame.init()
DISPLAYSURF = pygmae.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
        pygame.display.update()
s
