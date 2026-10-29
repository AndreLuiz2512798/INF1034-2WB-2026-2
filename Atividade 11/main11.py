import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

idel_spritesheet = pygame.image.load("Atividade 11/Idel.png")
jump_spritesheet = pygame.image.load("Atividade 11/Jump.png")
run_spritesheet = pygame.image.load("Atividade 11/Run.png")

idel_animation = True
jump_animation = False
run_animation = False

curr_frame = 0
anim_time = 0
curr_frame_mm = 0
anim_time_mm = 0

hero_x = 200
hero_y = 468

olhando_direita = True

velocidade_y = 0
gravidade = 0.0012
forca_pulo = -0.45

pygame.init()
screen = pygame.display.set_mode((800, 600))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_animation = True
                curr_frame_mm = 0
                anim_time_mm = 0
                velocidade_y = forca_pulo

    # Desenho dos elementos na tela
    screen.fill("#97D1FA")
    pygame.draw.rect(screen, "#489D25", (0, 500, 800, 100))

    clock.tick(60)
    dt = clock.get_time()

    anim_time = anim_time + dt
    anim_time_sec = anim_time/1000

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        idel_animation = False
        run_animation = True
        olhando_direita = True
        hero_x += 0.10 * dt
    elif keys[pygame.K_LEFT]:
        idel_animation = False
        run_animation = True
        olhando_direita = False
        hero_x += -0.10 * dt
    else:
        run_animation = False
        idel_animation = True

    if jump_animation:
        hero_y += velocidade_y * dt
        velocidade_y += gravidade * dt

        if hero_y >= 468:
            hero_y = 468
            velocidade_y = 0
            jump_animation = False

        frame = jump_spritesheet.subsurface((32*curr_frame_mm, 0, 32, 32))

        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (hero_x, hero_y))

        anim_time_mm = anim_time_mm + dt
        anim_time_mm_sec = anim_time_mm / 1000

        if anim_time_mm_sec > 0.5:
            curr_frame_mm = curr_frame_mm + 1
            anim_time_mm = 0

            if curr_frame_mm > 3:
                curr_frame_mm = 0
                jump_animation = False
    elif run_animation:
        anim_time_mm = anim_time_mm + dt
        anim_time_mm_sec = anim_time_mm/1000

        if anim_time_mm_sec > 0.1:
            curr_frame_mm = curr_frame_mm + 1
            if curr_frame_mm > 7:
                curr_frame_mm = 0
            anim_time_mm = 0

        frame = run_spritesheet.subsurface((32*curr_frame_mm, 0, 32, 32))
            
        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (hero_x, hero_y))
    
    elif idel_animation:
        if curr_frame_mm > 3:
            curr_frame_mm = 0
            
        anim_time_mm = anim_time_mm + dt
        anim_time_mm_sec = anim_time_mm/1000
    
        if anim_time_mm_sec > 0.1:
            curr_frame_mm = curr_frame_mm + 1
            if curr_frame_mm > 3:
                curr_frame_mm = 0
            anim_time_mm = 0

        frame = idel_spritesheet.subsurface((32*curr_frame_mm, 0, 32, 32))
                    
        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (hero_x, hero_y))


    pygame.display.update()