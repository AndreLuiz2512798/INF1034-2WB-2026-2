from random import randint

pontuacao = 0
pontuacao_computador = 0
inicio = True

while inicio:
    resposta_computador = randint(1,3)

    print()
    print(f"Sua pontuação: {pontuacao} || Pontuação do computador: {pontuacao_computador} ")
    print("Digite o número referente a escolha.\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura")
    resposta = int(input("Resposta: "))

    if resposta_computador == 1:
        print("\nO computador escolheu: Pedra")
    elif resposta_computador == 2:
        print("\nO computador escolheu: Papel")
    else:
        print("\nO computador escolheu: Tesoura")

    if (resposta == 1 and resposta_computador == 3):
        print("Você ganhou!!")
        pontuacao += 1
    elif (resposta == 3 and resposta_computador == 2):
        print("Você ganhou!!")
        pontuacao += 1
    elif (resposta == 2 and resposta_computador == 1):
        print("Você ganhou!!")
        pontuacao += 1
    elif (resposta == 3 and resposta_computador == 1):
        print("Você perdeu.")
        pontuacao_computador += 1
    elif (resposta == 2 and resposta_computador == 3):
        print("Você perdeu.")
        pontuacao_computador += 1
    elif (resposta == 1 and resposta_computador == 2):
        print("Você perdeu.")
        pontuacao_computador += 1
    else:
        print("Empate.")

    opcao_reiniciar = input("Deseja continuar? (s/n): ")
    if opcao_reiniciar == "n":
        inicio = False