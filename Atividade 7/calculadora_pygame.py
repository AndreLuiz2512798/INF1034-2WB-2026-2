from pygame import *

def calcular(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro!"
    else:
        return "Operação inválida"

init()
screen = display.set_mode((800, 600))

resultado = 0
operacoes = ["+", "-", "*", "/"]


font = font.Font(None, 36)
numeros = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["0", "."]
]
x_inicial = 210
y_inicial = 260
largura_tecla = 100
altura_tecla = 50
espaco = 10

numero1 = None
numero2 = None
operacao = None

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONUP:
            mouse_x, mouse_y = ev.pos
            for i, linha in enumerate(numeros):
                for j, numero in enumerate(linha):
                    x = x_inicial + j * (largura_tecla + espaco)
                    y = y_inicial + i * (altura_tecla + espaco)

                    if x <= mouse_x <= x + largura_tecla and y <= mouse_y <= y + altura_tecla:
                        valor_clicado = numero

            for i, op in enumerate(operacoes):
                op_x = 540
                op_y = 260 + i * (altura_tecla + espaco)
                if op_x <= mouse_x <= op_x + 50 and op_y <= mouse_y <= op_y + 50:
                    valor_clicado = op

        if valor_clicado:
            if valor_clicado in operacoes:
                if numero1 is not None:
                    operacao = valor_clicado
            elif valor_clicado == ".":
                if operacao is None:
                    if numero1 is None:
                        numero1 = "0."
                    elif "." not in numero1:
                        numero1 += "."
                else:
                    if numero2 is None:
                        numero2 = "0."
                    elif "." not in numero2:
                        numero2 += "."
            else: 
                if operacao is None:
                    if numero1 is None:
                        numero1 = valor_clicado
                    else:
                        numero1 += valor_clicado  
                else:  
                    if numero2 is None:
                        numero2 = valor_clicado
                    else:
                        numero2 += valor_clicado

            if numero1 is not None and numero2 is not None and operacao is not None:
                try:
                    resultado = calcular(float(numero1), float(numero2), operacao)
                    numero1 = str(resultado)
                    numero2 = None
                    operacao = None
                except ValueError:
                    numero1 = None
                    numero2 = None
                    operacao = None

            valor_clicado = None

    screen.fill("#FFFFFF")

    #Desenhos
    draw.rect(screen, "#4D4453", (200, 100, 400, 400))
    draw.rect(screen, "#D5E2E2", (210, 110, 380, 100))

    #Teclas
    draw.rect(screen, "#28262F", (210, 260, 100, 50))
    draw.rect(screen, "#28262F", (320, 260, 100, 50))
    draw.rect(screen, "#28262F", (430, 260, 100, 50))

    draw.rect(screen, "#28262F", (210, 320, 100, 50))
    draw.rect(screen, "#28262F", (320, 320, 100, 50))
    draw.rect(screen, "#28262F", (430, 320, 100, 50))

    draw.rect(screen, "#28262F", (210, 380, 100, 50))
    draw.rect(screen, "#28262F", (320, 380, 100, 50))
    draw.rect(screen, "#28262F", (430, 380, 100, 50))

    draw.rect(screen, "#28262F", (210, 440, 100, 50))
    draw.rect(screen, "#28262F", (320, 440, 100, 50))
    draw.rect(screen, "#28262F", (430, 440, 100, 50))

    ##Operações
    draw.rect(screen, "#A65F6D", (540, 260, 50, 50))
    draw.rect(screen, "#A65F6D", (540, 320, 50, 50))
    draw.rect(screen, "#A65F6D", (540, 380, 50, 50))
    draw.rect(screen, "#A65F6D", (540, 440, 50, 50))

    #Divisão
    draw.line(screen, "#FFFFFF", (550, 285), (580, 285), 2)
    draw.circle(screen, "#FFFFFF", (565, 277), 3)
    draw.circle(screen, "#FFFFFF", (565, 295), 3)

    #Multiplicação
    draw.line(screen, "#FFFFFF", (550, 360), (580, 330), 2)
    draw.line(screen, "#FFFFFF", (550, 330), (580, 360), 2)

    #Subtração
    draw.line(screen, "#FFFFFF", (550, 405), (580, 405), 2)

    #Adição
    draw.line(screen, "#FFFFFF", (565, 450), (565, 480), 2)
    draw.line(screen, "#FFFFFF", (550, 465), (580, 465), 2)

    #Virgula
    draw.circle(screen, "#FFFFFF", (370, 470), 5)

    #Resultado
    draw.line(screen, "#FFFFFF", (460, 460), (500, 460), 4)
    draw.line(screen, "#FFFFFF", (460, 470), (500, 470), 4)


    for i, linha in enumerate(numeros):
        for j, numero in enumerate(linha):
            x = x_inicial + j * (largura_tecla + espaco)
            y = y_inicial + i * (altura_tecla + espaco)

            texto = font.render(numero, True, "#FFFFFF")  # Cor do texto: branco
            texto_rect = texto.get_rect(center=(x + largura_tecla // 2, y + altura_tecla // 2))

            screen.blit(texto, texto_rect)

    # digito1 = input("")

    # if digito1 in operacoes:
    #     digito2 = input("")
    #     try:
    #         numero1 = float(resultado)
    #         numero2 = float(digito2)
    #         resultado = calcular(numero1, numero2, digito1)
    #     except ValueError:
    #         print("Entrada inválida. Digite apenas números.")
    # else:
    #     digito2 = input("")
    #         break
    #     digito3 = input("")
    #         break

    #     try:
    #         numero1 = float(digito1)
    #         numero2 = float(digito3)
    #         operacao = digito2
    #         resultado = calcular(numero1, numero2, operacao)
    #     except ValueError:
    #         print("Entrada inválida. Digite apenas números.")

    # print(f"Resultado: {resultado}\n")

    display.update()