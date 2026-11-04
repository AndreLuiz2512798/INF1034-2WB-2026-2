import pygame, sys
from pygame.locals import QUIT, KEYDOWN

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
tile_size_joguinho = 64
tileset = pygame.image.load("Atividade 12/tileset_16x16.png")
collider_caixa = pygame.Rect(0, 0, 0, 0)
can_walk = True

idel_spritesheet = pygame.image.load("Atividade 12/Idel.png")
jump_spritesheet = pygame.image.load("Atividade 12/Jump.png")
run_spritesheet = pygame.image.load("Atividade 12/Run.png")

idel_animation = True
jump_animation = False
run_animation = False

curr_frame = 0
anim_time = 0
curr_frame_mm = 0
anim_time_mm = 0

olhando_direita = True

velocidade_y = 0
gravidade = 0.0012
forca_pulo = -0.45

pos_x = 64
pos_y = 384

velocidade_y = 0
no_chao = True

mapa_joguinho = [
  "XXXXXXXXXXXXXX",
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXBXXXXXXXXX", 
  "LGGGGGRAALGGGR", 
  "TTTTTTTPPTTTTT", 
  "TTTTTTTPPTTTTT",
]

caixa = pygame.Rect(
    4 * tile_size_joguinho,
    6 * tile_size_joguinho,
    tile_size_joguinho,
    tile_size_joguinho
)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_SPACE and no_chao:
                jump_animation = True
                curr_frame_mm = 0
                anim_time_mm = 0
                velocidade_y = forca_pulo
                no_chao = False

    clock.tick(60)
    dt = clock.get_time()

    old_pos_x = pos_x
    old_pos_y = pos_y

    anim_time = anim_time + dt
    anim_time_sec = anim_time/1000

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

    old_bottom = pos_y + 64

    velocidade_y += gravidade * dt
    pos_y += velocidade_y * dt

    collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64)

    no_chao = False

    if (
        velocidade_y > 0
        and old_bottom <= caixa.top
        and collider_jogador.bottom >= caixa.top
        and collider_jogador.right > caixa.left
        and collider_jogador.left < caixa.right
    ):
        pos_y = caixa.top - 64
        velocidade_y = 0
        no_chao = True
        jump_animation = False

    chao_y = 7 * tile_size_joguinho

    if pos_y + 64 >= chao_y:
        pos_y = chao_y - 64
        velocidade_y = 0
        no_chao = True
        jump_animation = False

    screen.fill((152,209,250))

    collider_jogador = pygame.Rect(pos_x, pos_y, 50, 64)

    if collider_jogador.colliderect(collider_caixa):
        pos_x = old_pos_x
        pos_y = old_pos_y

    pygame.draw.rect(screen, (0, 0, 255), collider_jogador, 2)

    for i in range(len(mapa_joguinho)): # Para cada linha
        for j in range(len(mapa_joguinho[i])): # Para cada coluna (letra)
            if mapa_joguinho[i][j] == "L":
                tile = tileset.subsurface((0, 0, 16, 16))
                tile = pygame.transform.scale(tile, (tile_size_joguinho, tile_size_joguinho))
                screen.blit(tile, (j * tile_size_joguinho, i * tile_size_joguinho))
            elif mapa_joguinho[i][j] == "G":
                tile = tileset.subsurface((16, 0, 16, 16))
                tile = pygame.transform.scale(tile, (tile_size_joguinho, tile_size_joguinho))
                screen.blit(tile, (j * tile_size_joguinho, i * tile_size_joguinho))
            elif mapa_joguinho[i][j] == "R":
                tile = tileset.subsurface((32, 0, 16, 16))
                tile = pygame.transform.scale(tile, (tile_size_joguinho, tile_size_joguinho))
                screen.blit(tile, (j * tile_size_joguinho, i * tile_size_joguinho))
            elif mapa_joguinho[i][j] == "T":
                tile = tileset.subsurface((64, 0, 16, 16))
                tile = pygame.transform.scale(tile, (tile_size_joguinho, tile_size_joguinho))
                screen.blit(tile, (j * tile_size_joguinho, i * tile_size_joguinho))
            elif mapa_joguinho[i][j] == "A":
                tile = tileset.subsurface((0, 64, 16, 16))
                tile = pygame.transform.scale(tile, (tile_size_joguinho, tile_size_joguinho))
                screen.blit(tile, (j * tile_size_joguinho, i * tile_size_joguinho))
            elif mapa_joguinho[i][j] == "B":
                tile = tileset.subsurface((112, 48, 16, 16))
                tile = pygame.transform.scale(tile, (tile_size_joguinho, tile_size_joguinho))
                screen.blit(tile, (j * tile_size_joguinho, i * tile_size_joguinho))
                collider_caixa = pygame.Rect(j * tile_size_joguinho, i * tile_size_joguinho, tile_size_joguinho, tile_size_joguinho)
                pygame.draw.rect(screen, (0, 0, 255), collider_caixa, 2)
            elif mapa_joguinho[i][j] == "P":
                tile = tileset.subsurface((16, 64, 16, 16))
                tile = pygame.transform.scale(tile, (tile_size_joguinho, tile_size_joguinho))
                screen.blit(tile, (j * tile_size_joguinho, i * tile_size_joguinho))

    if jump_animation:
        velocidade_y += gravidade * dt
        pos_y += velocidade_y * dt

        chao_y = 7 * tile_size_joguinho

        if pos_y + 64 >= chao_y:
            pos_y = chao_y - 64
            velocidade_y = 0
            no_chao = True
            jump_animation = False
        else:
            no_chao = False

        frame = jump_spritesheet.subsurface((32*curr_frame_mm, 0, 32, 32))

        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        frame = pygame.transform.scale(frame, (64, 64))
        screen.blit(frame, (pos_x, pos_y))

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
        frame = pygame.transform.scale(frame, (64, 64))
        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (pos_x, pos_y))
    
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
        frame = pygame.transform.scale(frame, (64, 64))
        if not olhando_direita:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (pos_x, pos_y))

    pygame.display.update()