import pygame, sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from random import randint
import tkinter as tk
from tkinter import simpledialog

lista1 = []
num_cat1 = 5
#Adicionando os numeros aleatórios em uma lista
for i in range(50):
    num = randint(0, 500)
    lista1.append(num)
lista2 = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130
]
num_cat2 = 4
num_cat3 = 6
resultado3 = []
limites3 = []
lista_cor_3 = []

def contabiliza_totais(nums, num_cat):
    num_min = min(nums)
    num_max = max(nums)
    tam_cat = (num_max - num_min) / num_cat
    limites = [
        (num_min + i_cat * tam_cat, num_min + (i_cat + 1) * tam_cat)
        for i_cat in range(num_cat)
    ]
    lista_total = [0] * num_cat

    for num in nums:
        if num == num_max:
            lista_total[-1] += 1
            continue

        for i_cat, (lim_inf, lim_sup) in enumerate(limites):
            if lim_inf <= num < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total, limites

#Escolhe uma cor aleatória
def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

resultado1, limites1 = contabiliza_totais(lista1, num_cat1)
lista_cor_1 = [randomColor(), randomColor(), randomColor(), randomColor(), randomColor()]


resultado2, limites2 = contabiliza_totais(lista2, num_cat2)

resultado2 = []
restante = len(lista2)
#Gera números aleatórias por faixa
for i in range(num_cat2):
    quantidade = randint(0, restante)
    resultado2.append(quantidade)
    restante -= quantidade

lista_cor_2 = [randomColor(), randomColor(), randomColor(), randomColor()]

def draw(screen, lista, lista_cor, limites):
    screen_h = screen.get_height()
    font = pygame.font.Font(None, 20)
    for i in range(len(lista)):
        x = 100 + i * 50
        h = 15 * lista[i]
        pygame.draw.rect(screen, lista_cor[i], (x, screen_h - h - 80, 25, h))

        # Desenhando os numeros nos eixos
        texto_interface = font.render(str(lista[i]), True, (255, 255, 255))
        text_rect = texto_interface.get_rect(center=(80, screen_h - h - 80))
        screen.blit(texto_interface, text_rect)

        # Renderiza os limites abaixo do eixo x
        lim_inf, lim_sup = limites[i]
        lim_text = f"{int(lim_inf)}-{int(lim_sup)}"
        lim_interface = font.render(lim_text, True, (255, 255, 255))
        lim_rect = lim_interface.get_rect(center=(x + 12, screen_h - 60))
        screen.blit(lim_interface, lim_rect)

    #Desenhando os eixos x e y
    pygame.draw.line(screen, '#FFFFFF', (90, 10), (90, 220), 2)
    pygame.draw.line(screen, '#FFFFFF', (90, 220), (380, 220), 2)

# Função para desenhar o botão
def draw_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, (0, 128, 255), (x, y, width, height))  # Desenha o botão
    font = pygame.font.Font(None, 24)
    text_interface = font.render(text, True, (255, 255, 255))  # Texto do botão
    text_rect = text_interface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_interface, text_rect)

# Função para mudar o desenhos
def proximoDesenho():
    global desenho
    desenho = (desenho + 1) % 3
    print(f"Desenho atual: {desenho}")

# Inicializa o Pygame
janela = tk.Tk()
janela.withdraw()
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Gráfico com Botão')

# Variáveis do botão
button_x, button_y, button_width, button_height = 150, 260, 100, 30
desenho = 0

# Loop principal
while True:
    screen.fill((0, 0, 0))  # Limpa a tela
    if desenho == 0:
        draw(screen, resultado1, lista_cor_1, limites1)  # Desenha o gráfico
    elif desenho == 1:
        draw(screen, resultado2, lista_cor_2, limites2)
    elif desenho == 2:
        draw(screen, resultado3, lista_cor_3, limites3)
    draw_button(screen, button_x, button_y, button_width, button_height, "Próximo")  # Desenha o botão

    for event in pygame.event.get():
        if event.type == QUIT:
            janela.destroy()
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Verifica se o botão foi clicado
            if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                proximoDesenho()
                if desenho == 2:
                    numeros = []
                    for i in range(10):
                        #Cria o input
                        numero = simpledialog.askinteger(
                            "Escolha do número",
                            f"Digite o número {i + 1} para adicionar:",
                            parent=janela,
                        )
                        numeros.append(numero)

                    if len(numeros) == 10:
                        resultado3, limites3 = contabiliza_totais(numeros, num_cat3)
                        lista_cor_3 = [randomColor(), randomColor(), randomColor(), randomColor(), randomColor(), randomColor()]
                    else:
                        desenho = 1

    pygame.display.update()