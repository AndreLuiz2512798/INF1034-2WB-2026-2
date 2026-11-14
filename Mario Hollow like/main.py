import pygame, sys
from pygame.locals import QUIT, KEYDOWN

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 720))

hero_idle = pygame.image.load("Mario Hollow like/hero_idle.png")
hero_jump = pygame.image.load("Mario Hollow like/hero_jump.png")
hero_run = pygame.image.load("Mario Hollow like/hero_run.png")

idel_animation = True
jump_animation = False
run_animation = False

curr_frame_idle = 0
anim_time_idle = 0

curr_frame_run = 0
anim_time_run = 0

curr_frame_jump = 0
anim_time_jump = 0

pos_x = 200
pos_y = 556

olhando_direita = True

velocidade_y = 0
gravidade = 0.0008
forca_pulo = -0.40

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE and not jump_animation:
                jump_animation = True
                curr_frame_jump = 0
                anim_time_jump = 0
                velocidade_y = forca_pulo

    screen.fill("#97D1FA")
    pygame.draw.rect(screen, "#489D25", (0, 620, 1200, 100))

    clock.tick(60)
    dt = clock.get_time()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        idel_animation = False
        run_animation = True
        olhando_direita = True
        pos_x += 0.10 * dt
    elif keys[pygame.K_LEFT]:
        idel_animation = False
        run_animation = True
        olhando_direita = False
        pos_x += -0.10 * dt
    else:
        run_animation = False
        idel_animation = True

    if jump_animation:
        pos_y += velocidade_y * dt
        velocidade_y += gravidade * dt

        if pos_y >= 556:
            pos_y = 556
            velocidade_y = 0
            jump_animation = False

        anim_time_jump += dt

        if anim_time_jump >= 150:
            curr_frame_jump += 1
            anim_time_jump = 0

            if curr_frame_jump > 7:
                curr_frame_jump = 7

        frame = hero_jump.subsurface((
            64 * (curr_frame_jump % 4),
            64 * (curr_frame_jump // 4),
            64,
            64
        ))

        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (pos_x, pos_y))

    elif run_animation:
        anim_time_run += dt
        anim_time_run_sec = anim_time_run / 1000

        if anim_time_run_sec > 0.1:
            curr_frame_run += 1
            if curr_frame_run > 7:
                curr_frame_run = 0
            anim_time_run = 0

        frame = hero_run.subsurface((
            64 * (curr_frame_run % 4),
            64 * (curr_frame_run // 4),
            64,
            64
        ))

        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (pos_x, pos_y))

    elif idel_animation:
        if curr_frame_idle > 7:
            curr_frame_idle = 0

        anim_time_idle += dt
        anim_time_idle_sec = anim_time_idle / 1000

        if anim_time_idle_sec > 0.1:
            curr_frame_idle += 1
            if curr_frame_idle > 7:
                curr_frame_idle = 0
            anim_time_idle = 0

        frame = hero_idle.subsurface((
            64 * (curr_frame_idle % 4),
            64 * (curr_frame_idle // 4),
            64,
            64
        ))

        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (pos_x, pos_y))

    pygame.display.update()