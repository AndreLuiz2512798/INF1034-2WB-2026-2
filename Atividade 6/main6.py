from pygame import *

init()
screen = display.set_mode((800, 600))
clock = time.Clock()

#Recursos
rick_morty_img = image.load("Atividade 6/rick_morty.png")
rick_morty_img = transform.scale(rick_morty_img, (100, 130))
fonte = font.Font("Atividade 6/get_schwifty.ttf", 30)
mixer.music.load("Atividade 6/lv_0_20260919140841.mp3")
mixer.music.play(-1)

#Variáveis
nuvem_x = 0
velocidade = 100
sol_x = 100
sol_y = 100
controle_teclado = False
ultimo_mouse_x = 100
ultimo_mouse_y = 100

running = True
while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        #Ação instantanea
        #if ev.type == KEYDOWN:


    ##Seção para movimentação e interação
    #Estrutura de movimentação no teclado
    keys = key.get_pressed()

    #Sol
    if keys[K_RIGHT] or keys[K_LEFT] or keys[K_UP] or keys[K_DOWN]:
        controle_teclado = True
  
    if controle_teclado:
        if keys[K_RIGHT]:
            sol_x += 100 * dt
        if keys[K_LEFT]:
            sol_x += -100 * dt
        if keys[K_UP]:
            sol_y += -100 * dt
        if keys[K_DOWN]:
            sol_y += 100 * dt


    #Estrutura de movimentação no mouse
    mouse_x, mouse_y = mouse.get_pos()

    if mouse_x != ultimo_mouse_x or mouse_y != ultimo_mouse_y:
        sol_x = mouse_x
        sol_y = mouse_y
        controle_teclado = False

    ultimo_mouse_x = mouse_x
    ultimo_mouse_y = mouse_y

    #Nuvem
    dt = clock.get_time()/1000
    nuvem_x += velocidade * dt

    if nuvem_x > 70:
        velocidade = -100
    elif nuvem_x < -560:
        velocidade = 100


    ##Seção para desenhar os elementos
    #Tela
    if sol_y > 400:
        screen.fill("#0D1664")
    elif sol_y > 200:
        screen.fill("#F3D355")
    elif sol_y > 0:
        screen.fill("#97D1FA")
    #Grama
    draw.rect(screen, "#489D25", (0, 500, 800, 100))
    #Base da casa
    draw.rect(screen, "#D1CFC0", (200, 300, 200, 200))
    #Telhado
    draw.polygon(screen, "#503621", ((200, 300), (400,300), (300, 150)))
    #Janela
    draw.rect(screen, "#C7DEE9", (220, 360, 60, 80))
    #Porta
    draw.rect(screen, "#786154", (320, 370, 60, 130))
    #Maçaneta
    draw.circle(screen, "#67574C", (330, 435), 5)
    #Árvore
    draw.rect(screen, "#503621", (600, 300, 40, 200))
    draw.circle(screen, "#489D25", (620, 300), 100)
    #Sol
    draw.line(screen, "#FFF251", (sol_x - 60, sol_y - 60), (sol_x + 60, sol_y + 60), 10)
    draw.line(screen, "#FFF251", (sol_x - 60, sol_y + 60), (sol_x + 60, sol_y - 60), 10)
    draw.line(screen, "#FFF251", (sol_x - 70, sol_y), (sol_x + 70, sol_y), 10)
    draw.line(screen, "#FFF251", (sol_x, sol_y - 70), (sol_x, sol_y + 70), 10)
    draw.circle(screen, "#FFF251", (sol_x, sol_y), 40)
    #Nuvem
    draw.circle(screen, "#FFFFFF", (600 + nuvem_x, 100), 40)
    draw.circle(screen, "#FFFFFF", (630 + nuvem_x, 100), 40)
    draw.circle(screen, "#FFFFFF", (660 + nuvem_x, 100), 40)
    draw.circle(screen, "#FFFFFF", (690 + nuvem_x, 100), 40)

    #Desenhando imagem
    screen.blit(rick_morty_img, (420, 380))

    #Escrevendo o texto
    rick_texto = fonte.render("Vamos Morty", True, "#329400")
    screen.blit(rick_texto, (400, 350))


    display.update()