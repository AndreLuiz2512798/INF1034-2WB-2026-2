from random import choice

lista = ["banana", "morango", "laranja", "maca", "kiwi", "abacaxi"]
inicio = True

while inicio:
    palavra_aleatoria = choice(lista)
    palavra_oculta = "_ " * len(palavra_aleatoria)

    vidas = 6
    resposta = True

    while resposta:
        if vidas == 0:
            print("Você perdeu")
            opcao_reiniciar = input("Deseja reiniciar? (s/n): ")
            if opcao_reiniciar == "n":
                inicio = False
                resposta = False
            elif opcao_reiniciar == "s":
                resposta = False
            else:
                print("Opção inválida\n")
        else:
            if palavra_oculta == palavra_aleatoria:
                print(palavra_oculta)
                print("Parabéns!!")
                opcao_reiniciar = input("Deseja reiniciar? (s/n): ")
                if opcao_reiniciar == "n":
                    inicio = False
                    resposta = False
                elif opcao_reiniciar == "s":
                    resposta = False
                else:
                    print("Opção inválida\n")
            else:
                if "_ " in palavra_oculta:
                    print('\nVidas:', vidas)
                    print(palavra_oculta)
                    opcao_chute = input("Deseja chutar a palavra? (s/n): ")
                    if opcao_chute == "s":
                        chute = input("Digite a palavra: ")
                        if chute == palavra_aleatoria:
                            palavra_oculta = chute
                            print()
                            print(chute)
                            print("Parabéns!!")
                            opcao_reiniciar = input("Deseja reiniciar? (s/n): ")
                            if opcao_reiniciar == "n":
                                inicio = False
                                resposta = False
                            elif opcao_reiniciar == "s":
                                resposta = False
                            else:
                                print("Opção inválida\n")
                        else:
                            print("Errou\n")
                            vidas -= 1
                    elif opcao_chute == "n":
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
                        print("Opção inválida\n")
                else:
                    palavra_oculta = palavra_aleatoria