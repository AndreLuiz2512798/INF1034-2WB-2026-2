from pygame import *

init()
screen = display.set_mode((800, 600))

# #Recursos
# batman_img = image.load("batman.png")
# batman_img = transform.scale(batman_img, (200, 200))
# fonte = font.Font("batmfa__.ttf", 30)
# mixer.music.load("batman_1966.mp3")
# mixer.music.play(-1)


running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    #Desenhar os elementos
    screen.fill("#97D1FA")
    #Grama
    draw.rect(screen, "#489D25", (0, 500, 800, 100))
    #Sol
    draw.line(screen, "#FFF251", (40, 40), (160, 160), 10)
    draw.line(screen, "#FFF251", (40, 160), (160, 40), 10)
    draw.line(screen, "#FFF251", (30, 100), (170, 100), 10)
    draw.line(screen, "#FFF251", (100, 30), (100, 170), 10)
    draw.circle(screen, "#FFF251", (100, 100), 40)
    #Base da casa
    draw.rect(screen, "#F2E6D3", (200, 300, 200, 200))
    #Telhado
    draw.polygon(screen, "#F03745", ((200, 300), (400,300), (300, 150)))

    # #Desenhando imagem
    # screen.blit(batman_img, (400, 300))

    # #Escrevendo o texto
    # bat_texto = fonte.render("I am BATMAN!", True, "#000000")
    # screen.blit(bat_texto, (500, 250))


    display.update()