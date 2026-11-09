import pygame, sys
from pygame.locals import QUIT

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 720))

hero_idle = pygame.image.load("Mario Hollow like/hero_idle.png")

curr_frame_mm = 0
anim_time_mm = 0

pos_x = 200
pos_y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(60)

    anim_time_mm += dt

    if anim_time_mm >= 150:
        curr_frame_mm = (curr_frame_mm + 1) % 6
        anim_time_mm = 0

    screen.fill("#97D1FA")
    pygame.draw.rect(screen, "#489D25", (0, 620, 1200, 100))

    screen.blit(
        hero_idle,
        (pos_x, pos_y),
        (224 * curr_frame_mm, 0, 224, 768))

    pygame.display.update()