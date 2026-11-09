import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1200, 720))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    pygame.display.update()