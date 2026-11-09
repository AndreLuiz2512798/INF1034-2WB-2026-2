import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

hero_idle = pygame.image.load("Mario Hollow like/hero_idle.jpg")

curr_frame = 0
anim_time = 0
curr_frame_mm = 0
anim_time_mm = 0

pos_x = 200
pos_y = 620

pygame.init()
screen = pygame.display.set_mode((1200, 720))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    anim_time = anim_time + dt
    anim_time_sec = anim_time/1000

    screen.fill("#97D1FA")
    pygame.draw.rect(screen, "#489D25", (0, 620, 1200, 100))

    if curr_frame_mm > 3:
        curr_frame_mm = 0
        
    anim_time_mm = anim_time_mm + dt
    anim_time_mm_sec = anim_time_mm/1000

    if anim_time_mm_sec > 0.1:
        curr_frame_mm = curr_frame_mm + 1
        if curr_frame_mm > 3:
            curr_frame_mm = 0
        anim_time_mm = 0

    screen.blit(hero_idle, (pos_x, pos_y), (60 * curr_frame_mm, 0, 60, 60))

    pygame.display.update()