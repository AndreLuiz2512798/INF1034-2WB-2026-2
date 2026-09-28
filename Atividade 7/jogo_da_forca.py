from random import choice

lista = ["banana", "morango", "laranja", "maca", "kiwi", "abacaxi"]

palavra_aleatoria = choice(lista)
palavra_oculta = "_ " * len(palavra_aleatoria)

vidas = 6
resposta = True

while resposta:
    if vidas == 0:
        print("Você perdeu")
        resposta = False
    else:
        if palavra_oculta == palavra_aleatoria:
            print(palavra_oculta)
            print("Parabéns!!")
            resposta = False
        else:
            if "_ " in palavra_oculta:
                print('Vidas:', vidas)
                print(palavra_oculta)
                letra = input("Digite uma letra da palavra: ")
                print("\n\n")
                if letra in "0123456789":
                    print("Digite somente letras")
                else:
                    if letra in palavra_aleatoria:
                        palavra_aux = ""
                        for i in range(len(palavra_aleatoria)):
                            if letra == palavra_aleatoria[i]:
                                palavra_aux += letra + " "
                            else:
                                palavra_aux += palavra_oculta[2*i] + " "
                        
                        palavra_oculta = palavra_aux
                    else:
                        print("Errou")
                        vidas -= 1
            else:
                palavra_oculta = palavra_aleatoria