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

resultado = 0
operacoes = ["+", "-", "*", "/"]

while True:
    print("Digite 'sair' para encerrar o programa.")

    digito1 = input("")
    if digito1.lower() == "sair":
        break

    if digito1 in operacoes:
        digito2 = input("")
        if digito2.lower() == "sair":
            break

        try:
            numero1 = float(resultado)
            numero2 = float(digito2)
            resultado = calcular(numero1, numero2, digito1)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
    else:
        digito2 = input("")
        if digito2.lower() == "sair":
            break
        digito3 = input("")
        if digito3.lower() == "sair":
            break

        try:
            numero1 = float(digito1)
            numero2 = float(digito3)
            operacao = digito2
            resultado = calcular(numero1, numero2, operacao)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    print(f"Resultado: {resultado}\n")