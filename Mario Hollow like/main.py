import pygame, sys
from pygame.locals import QUIT, KEYDOWN

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 720))

hero_idle = pygame.image.load("Mario Hollow like/assets/hero/hero_idle.png")
hero_jump = pygame.image.load("Mario Hollow like/assets/hero/hero_jump.png")
hero_run = pygame.image.load("Mario Hollow like/assets/hero/hero_run.png")
hero_attack = pygame.image.load("Mario Hollow like/assets/hero/hero_attack.png")

enemy_idle = pygame.image.load("Mario Hollow like/assets/enemy/enemy_idle.png")
enemy_run = pygame.image.load("Mario Hollow like/assets/enemy/enemy_run.png")

idel_animation = True
jump_animation = False
run_animation = False
attack_animation = False

curr_frame_idle = 0
anim_time_idle = 0

curr_frame_run = 0
anim_time_run = 0

curr_frame_jump = 0
anim_time_jump = 0

curr_frame_attack = 0
anim_time_attack = 0

pos_x = 200
pos_y = 556

olhando_direita = True

velocidade_y = 0
gravidade = 0.0008
forca_pulo = -0.40

enemy_x = 850
enemy_y = 556

enemy_direction = 1
enemy_state = "idle"
enemy_state_time = 0

enemy_curr_frame_idle = 0
enemy_anim_time_idle = 0

enemy_curr_frame_run = 0
enemy_anim_time_run = 0

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

            if event.key == pygame.K_f and not attack_animation:
                attack_animation = True
                curr_frame_attack = 0
                anim_time_attack = 0

    screen.fill("#97D1FA")
    pygame.draw.rect(screen, "#489D25", (0, 620, 1200, 100))

    clock.tick(60)
    dt = clock.get_time()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        idel_animation = False
        run_animation = True
        olhando_direita = True
        pos_x += 0.10 * dt
    elif keys[pygame.K_a]:
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

    if attack_animation:
        anim_time_attack += dt

        if anim_time_attack >= 100:
            curr_frame_attack += 1
            anim_time_attack = 0

            if curr_frame_attack > 7:
                curr_frame_attack = 0
                attack_animation = False

    if attack_animation:
        frame = hero_attack.subsurface((
            64 * (curr_frame_attack % 4),
            64 * (curr_frame_attack // 4),
            64,
            64
        ))

    elif jump_animation:
        frame = hero_jump.subsurface((
            64 * (curr_frame_jump % 4),
            64 * (curr_frame_jump // 4),
            64,
            64
        ))

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

    elif idel_animation:
        if curr_frame_idle > 7:
            curr_frame_idle = 0

        anim_time_idle += dt
        anim_time_idle_sec = anim_time_idle / 1000

        if anim_time_idle_sec > 0.5:
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

    enemy_state_time += dt

    if enemy_state == "idle":
        if enemy_state_time >= 2000:
            enemy_state = "run"
            enemy_state_time = 0
            enemy_curr_frame_run = 0
            enemy_anim_time_run = 0

    elif enemy_state == "run":
        enemy_x += 0.06 * dt * enemy_direction

        if enemy_x <= 100:
            enemy_x = 100
            enemy_direction = 1
            enemy_state = "idle"
            enemy_state_time = 0

        elif enemy_x >= 1100:
            enemy_x = 1100
            enemy_direction = -1
            enemy_state = "idle"
            enemy_state_time = 0

        elif enemy_state_time >= 2500:
            enemy_direction *= -1
            enemy_state = "idle"
            enemy_state_time = 0

    if enemy_state == "idle":
        enemy_anim_time_idle += dt

        if enemy_anim_time_idle >= 100:
            enemy_curr_frame_idle = (enemy_curr_frame_idle + 1) % 8
            enemy_anim_time_idle = 0

        enemy_frame = enemy_idle.subsurface((
            64 * (enemy_curr_frame_idle % 4),
            64 * (enemy_curr_frame_idle // 4),
            64,
            64
        ))

    elif enemy_state == "run":
        enemy_anim_time_run += dt

        if enemy_anim_time_run >= 100:
            enemy_curr_frame_run = (enemy_curr_frame_run + 1) % 8
            enemy_anim_time_run = 0

        enemy_frame = enemy_run.subsurface((
            64 * (enemy_curr_frame_run % 4),
            64 * (enemy_curr_frame_run // 4),
            64,
            64
        ))

    if enemy_direction == -1:
        enemy_frame = pygame.transform.flip(enemy_frame, True, False)

    screen.blit(enemy_frame, (enemy_x, enemy_y))

    pygame.display.update()
