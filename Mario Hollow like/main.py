import pygame, sys
from pygame.locals import QUIT, KEYDOWN

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
TILE_SIZE = 64

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 32)
game_over_font = pygame.font.SysFont("Arial", 70)

hero_idle = pygame.image.load("Mario Hollow like/assets/hero/hero_idle.png").convert_alpha()
hero_jump = pygame.image.load("Mario Hollow like/assets/hero/hero_jump.png").convert_alpha()
hero_run = pygame.image.load("Mario Hollow like/assets/hero/hero_run.png").convert_alpha()
hero_attack = pygame.image.load("Mario Hollow like/assets/hero/hero_attack.png").convert_alpha()

enemy_idle = pygame.image.load("Mario Hollow like/assets/enemy/enemy_idle.png").convert_alpha()
enemy_run = pygame.image.load("Mario Hollow like/assets/enemy/enemy_run.png").convert_alpha()

mapa = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "DDDDDDDEEDDDDDDDDDDDDEEDDDDDDDDDDDDDDDDD",
    "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
    "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
]

map_width = len(mapa[0]) * TILE_SIZE
map_height = len(mapa) * TILE_SIZE

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
pos_y = 512

olhando_direita = True

velocidade_y = 0
gravidade = 0.0006
forca_pulo = -0.45
on_ground = False
tempo_no_chao = 0

enemy_x = 850
enemy_y = 512

enemy_direction = 1
enemy_state = "idle"
enemy_state_time = 0

enemy_curr_frame_idle = 0
enemy_anim_time_idle = 0

enemy_curr_frame_run = 0
enemy_anim_time_run = 0

vidas = 3
invulnerability_timer = 0
enemy_attack_cooldown = 0
game_over = False

camera_x = 0


def obter_blocos(rect):
    blocos = []

    inicio_coluna = max(0, rect.left // TILE_SIZE)
    fim_coluna = min(len(mapa[0]) - 1, rect.right // TILE_SIZE)

    inicio_linha = max(0, rect.top // TILE_SIZE)
    fim_linha = min(len(mapa) - 1, rect.bottom // TILE_SIZE)

    for linha in range(inicio_linha, fim_linha + 1):
        for coluna in range(inicio_coluna, fim_coluna + 1):
            if mapa[linha][coluna] in ("D", "T"):
                bloco = pygame.Rect(
                    coluna * TILE_SIZE,
                    linha * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )

                blocos.append(bloco)

    return blocos


def desenhar_mapa():
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            bloco = mapa[linha][coluna]

            x = coluna * TILE_SIZE - camera_x
            y = linha * TILE_SIZE

            if x + TILE_SIZE < 0 or x > SCREEN_WIDTH:
                continue

            if bloco == "D":
                pygame.draw.rect(screen, "#489D25", (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, "#34751C", (x, y, TILE_SIZE, 8))

            elif bloco == "T":
                pygame.draw.rect(screen, "#79502D", (x, y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, "#634024", (x, y, TILE_SIZE, 4))

            elif bloco == "E":
                pygame.draw.rect(screen, "#79502D", (x, y, TILE_SIZE, TILE_SIZE))

                pygame.draw.polygon(
                    screen,
                    "#777777",
                    [
                        (x, y + TILE_SIZE),
                        (x + TILE_SIZE // 2, y + 12),
                        (x + TILE_SIZE, y + TILE_SIZE)
                    ]
                )

                pygame.draw.polygon(
                    screen,
                    "#AAAAAA",
                    [
                        (x + 16, y + TILE_SIZE),
                        (x + TILE_SIZE // 2, y + 12),
                        (x + TILE_SIZE // 2 + 16, y + TILE_SIZE)
                    ]
                )


def verificar_espinhos(rect):
    inicio_coluna = max(0, rect.left // TILE_SIZE)
    fim_coluna = min(len(mapa[0]) - 1, rect.right // TILE_SIZE)

    inicio_linha = max(0, rect.top // TILE_SIZE)
    fim_linha = min(len(mapa) - 1, rect.bottom // TILE_SIZE)

    for linha in range(inicio_linha, fim_linha + 1):
        for coluna in range(inicio_coluna, fim_coluna + 1):
            if mapa[linha][coluna] == "E":
                espinho = pygame.Rect(
                    coluna * TILE_SIZE,
                    linha * TILE_SIZE + 16,
                    TILE_SIZE,
                    TILE_SIZE
                )

                if rect.colliderect(espinho):
                    return True

    return False


def receber_dano():
    global vidas, invulnerability_timer

    if invulnerability_timer <= 0:
        vidas -= 1
        invulnerability_timer = 1000

        if vidas <= 0:
            vidas = 0
            return True

    return False


def reiniciar_jogo():
    global pos_x, pos_y, velocidade_y, on_ground, tempo_no_chao
    global vidas, invulnerability_timer, enemy_attack_cooldown
    global enemy_x, enemy_y, enemy_direction, enemy_state, enemy_state_time
    global curr_frame_idle, curr_frame_run, curr_frame_jump, curr_frame_attack
    global anim_time_idle, anim_time_run, anim_time_jump, anim_time_attack
    global jump_animation, run_animation, idel_animation, attack_animation
    global game_over, camera_x

    pos_x = 200
    pos_y = 512
    velocidade_y = 0
    on_ground = False
    tempo_no_chao = 0

    vidas = 3
    invulnerability_timer = 0
    enemy_attack_cooldown = 0

    enemy_x = 850
    enemy_y = 512
    enemy_direction = 1
    enemy_state = "idle"
    enemy_state_time = 0

    curr_frame_idle = 0
    curr_frame_run = 0
    curr_frame_jump = 0
    curr_frame_attack = 0

    anim_time_idle = 0
    anim_time_run = 0
    anim_time_jump = 0
    anim_time_attack = 0

    jump_animation = False
    run_animation = False
    idel_animation = True
    attack_animation = False

    camera_x = 0
    game_over = False


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    reiniciar_jogo()

            else:
                if event.key == pygame.K_SPACE and tempo_no_chao > 0 and not attack_animation:
                    jump_animation = True
                    curr_frame_jump = 0
                    anim_time_jump = 0
                    velocidade_y = forca_pulo
                    on_ground = False
                    tempo_no_chao = 0

                if event.key == pygame.K_f and not attack_animation:
                    attack_animation = True
                    curr_frame_attack = 0
                    anim_time_attack = 0

    dt = clock.tick(60)

    screen.fill("#97D1FA")

    if not game_over:

        if invulnerability_timer > 0:
            invulnerability_timer -= dt

        if enemy_attack_cooldown > 0:
            enemy_attack_cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            idel_animation = False
            run_animation = True
            olhando_direita = True

            pos_x += 0.10 * dt

            rect = pygame.Rect(pos_x, pos_y, 64, 64)

            for bloco in obter_blocos(rect):
                if rect.colliderect(bloco):
                    pos_x = bloco.left - 64
                    rect.x = pos_x

        elif keys[pygame.K_a]:
            idel_animation = False
            run_animation = True
            olhando_direita = False

            pos_x -= 0.10 * dt

            rect = pygame.Rect(pos_x, pos_y, 64, 64)

            for bloco in obter_blocos(rect):
                if rect.colliderect(bloco):
                    pos_x = bloco.right
                    rect.x = pos_x

        else:
            run_animation = False
            idel_animation = True

        pos_x = max(0, min(pos_x, map_width - 64))

        velocidade_y += gravidade * dt
        pos_y += velocidade_y * dt

        on_ground = False

        rect = pygame.Rect(pos_x, pos_y, 64, 64)

        for bloco in obter_blocos(rect):
            if rect.colliderect(bloco):
                if velocidade_y > 0:
                    pos_y = bloco.top - 64
                    velocidade_y = 0
                    on_ground = True
                    jump_animation = False

                elif velocidade_y < 0:
                    pos_y = bloco.bottom
                    velocidade_y = 0

                rect.y = pos_y

        if on_ground:
            tempo_no_chao = 120
        else:
            tempo_no_chao -= dt

        tempo_no_chao = max(0, tempo_no_chao)

        rect = pygame.Rect(pos_x, pos_y, 64, 64)

        if verificar_espinhos(rect):
            if receber_dano():
                game_over = True
            else:
                pos_x = 200
                pos_y = 512
                velocidade_y = 0
                on_ground = False
                tempo_no_chao = 0
                jump_animation = False

        if pos_y > map_height:
            if receber_dano():
                game_over = True
            else:
                pos_x = 200
                pos_y = 512
                velocidade_y = 0
                on_ground = False
                tempo_no_chao = 0
                jump_animation = False

        if jump_animation:
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

            if anim_time_run >= 100:
                curr_frame_run = (curr_frame_run + 1) % 8
                anim_time_run = 0

            frame = hero_run.subsurface((
                64 * (curr_frame_run % 4),
                64 * (curr_frame_run // 4),
                64,
                64
            ))

        else:
            anim_time_idle += dt

            if anim_time_idle >= 500:
                curr_frame_idle = (curr_frame_idle + 1) % 8
                anim_time_idle = 0

            frame = hero_idle.subsurface((
                64 * (curr_frame_idle % 4),
                64 * (curr_frame_idle // 4),
                64,
                64
            ))

        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        camera_x = max(
            0,
            min(pos_x - SCREEN_WIDTH // 2, map_width - SCREEN_WIDTH)
        )

        desenhar_mapa()

        if invulnerability_timer <= 0 or (invulnerability_timer // 100) % 2 == 0:
            screen.blit(frame, (pos_x - camera_x, pos_y))

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

            elif enemy_x >= map_width - 100:
                enemy_x = map_width - 100
                enemy_direction = -1
                enemy_state = "idle"
                enemy_state_time = 0

            elif enemy_state_time >= 2500:
                enemy_direction *= -1
                enemy_state = "idle"
                enemy_state_time = 0

        player_rect = pygame.Rect(pos_x + 8, pos_y + 5, 48, 54)
        enemy_rect = pygame.Rect(enemy_x + 8, enemy_y + 5, 48, 54)

        if player_rect.colliderect(enemy_rect):
            if enemy_attack_cooldown <= 0:
                if receber_dano():
                    game_over = True

                enemy_attack_cooldown = 1200

            if pos_x < enemy_x:
                pos_x = enemy_x - 48
            else:
                pos_x = enemy_x + 48

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

        screen.blit(enemy_frame, (enemy_x - camera_x, enemy_y))

        texto_vidas = font.render(f"Vidas: {vidas}", True, "#FFFFFF")
        screen.blit(texto_vidas, (20, 20))

    else:
        texto_game_over = game_over_font.render("GAME OVER", True, "#FF0000")
        texto_reiniciar = font.render("Pressione R para reiniciar", True, "#FFFFFF")

        screen.blit(
            texto_game_over,
            (
                SCREEN_WIDTH // 2 - texto_game_over.get_width() // 2,
                SCREEN_HEIGHT // 2 - 70
            )
        )

        screen.blit(
            texto_reiniciar,
            (
                SCREEN_WIDTH // 2 - texto_reiniciar.get_width() // 2,
                SCREEN_HEIGHT // 2 + 30
            )
        )

    pygame.display.update()
