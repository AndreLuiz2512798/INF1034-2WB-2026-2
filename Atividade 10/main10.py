import pygame, sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from random import randint

lista1 = []
num_cat1 = 5
#Adicionando os numeros aleatórios em uma lista
for i in range(50):
    num = randint(0, 500)
    lista1.append(num)
num_min = min(lista1)
num_max = max(lista1)
tam_cat = (num_max - num_min) / num_cat1
lista_total1 = [0] * num_cat1

lista2 = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130
]
num_cat2 = 4
num_min = min(lista2)
num_max = max(lista2)
tam_cat = (num_max - num_min) / num_cat2
lista_total2 = [0] * num_cat2

limites = []
def contabiliza_totais(nums, lista_total, num_cat):
    limites.clear()  # Limpa os limites antes de recalcular
    # Para cada número na minha lista
    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        # Para cada faixa/categoria
        for i_cat in range(num_cat):
            # Obtém os limites inferior e superior
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            
            if len(limites) < num_cat:
                limites.append((lim_inf, lim_sup))
            elif limites[i_cat] != (lim_inf, lim_sup): #Verifica se o valor está correto
                limites[i_cat] = (lim_inf, lim_sup)

            # Checa em qual faixa/categoria o número está com base nesses limites
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total

def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

resultado1 = contabiliza_totais(lista1, lista_total1, num_cat1)
lista_cor_1 = [randomColor(), randomColor(), randomColor(), randomColor(), randomColor()]

resultado2 = contabiliza_totais(lista2, lista_total2, num_cat2)
lista_cor_2 = [randomColor(), randomColor(), randomColor(), randomColor()]


def draw(screen, lista):
    screen_h = screen.get_height()
    font = pygame.font.Font(None, 20)
    for i in range(len(lista)):
        x = 100 + i * 50
        h = 20 * lista[i]
        pygame.draw.rect(screen, lista_cor_2[i], (x, screen_h - h - 80, 25, h))
    
        # Desenhando os numeros nos eixos
        text_surface = font.render(str(lista[i]), True, (255, 255, 255)) 
        text_rect = text_surface.get_rect(center=(80, screen_h - h - 80))
        screen.blit(text_surface, text_rect)

        # Renderiza os limites abaixo do eixo x
        lim_inf, lim_sup = limites[i]
        lim_text = f"{int(lim_inf)}-{int(lim_sup)}"
        lim_surface = font.render(lim_text, True, (255, 255, 255))
        lim_rect = lim_surface.get_rect(center=(x + 12, screen_h - 60))
        screen.blit(lim_surface, lim_rect)

    #Desenhando os eixos x e y
    pygame.draw.line(screen, '#FFFFFF', (90, 80), (90, 220), 2)
    pygame.draw.line(screen, '#FFFFFF', (90, 220), (280, 220), 2)

# Função para desenhar o botão
def draw_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, (0, 128, 255), (x, y, width, height))  # Desenha o botão
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, (255, 255, 255))  # Texto do botão
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Função para mudar o desenhos
def proximoDesenho():
    global desenho
    desenho = (desenho + 1) % 3
    print(f"Desenho atual: {desenho}")

# Inicializa o Pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Gráfico com Botão')

# Variáveis do botão
button_x, button_y, button_width, button_height = 150, 260, 100, 30
desenho = 0

# Loop principal
while True:
    screen.fill((0, 0, 0))  # Limpa a tela
    draw(screen, lista_total2)  # Desenha o gráfico
    draw_button(screen, button_x, button_y, button_width, button_height, "Próximo")  # Desenha o botão

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Verifica se o botão foi clicado
            if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                proximoDesenho()

    pygame.display.update()