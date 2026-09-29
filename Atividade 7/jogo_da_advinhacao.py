from random import randint

def adivinhar_numero(numero, numero_secreto):
    if numero < numero_secreto:
        return 1
    elif numero > numero_secreto:
        return -1
    else:
        return 0


tentativas = 0
menor = 1
maior = 1023
numero_secreto = randint(1, 1023)
running_computador = False
running_jogador = False

resposta = input("Quem irá adivinhar o número secreto? (jogador/computador): ")

if resposta.lower() == "jogador":
    running_jogador = True
elif resposta.lower() == "computador":
    running_computador = True

while running_jogador:
    numero = int(input("Digite um número entre 1 e 1023: "))
    tentativas += 1
    resultado = adivinhar_numero(numero, numero_secreto)

    print(f"Resultado: {resultado}")
    if resultado == 0:
        print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas.")
        running_jogador = False

while running_computador:
    numero = randint(menor, maior)
    tentativas += 1

    fator = int(input(f"O computador escolheu o número {numero}. O número secreto é maior, menor ou igual? (1/0/-1): "))

    if fator == 1:
        menor = numero + 1
    elif fator == -1:
        maior = numero - 1
    else:
        print(f"O computador acertou o número secreto em {tentativas} tentativas.")
        running_computador = False