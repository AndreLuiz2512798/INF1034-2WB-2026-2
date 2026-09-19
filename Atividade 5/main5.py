from pygame import *

init()
screen = display.set_mode((800, 600))

#Recursos
rick_morty_img = image.load("Atividade 5/rick_morty.png")
rick_morty_img = transform.scale(rick_morty_img, (100, 130))
fonte = font.Font("Atividade 5/get_schwifty.ttf", 30)
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
    #Nuvem
    draw.circle(screen, "#FFFFFF", (600, 100), 40)
    draw.circle(screen, "#FFFFFF", (630, 100), 40)
    draw.circle(screen, "#FFFFFF", (660, 100), 40)
    draw.circle(screen, "#FFFFFF", (690, 100), 40)

    # #Desenhando imagem
    screen.blit(rick_morty_img, (420, 380))

    #Escrevendo o texto
    rick_texto = fonte.render("Vamos Morty", True, "#329400")
    screen.blit(rick_texto, (400, 350))


    display.update()