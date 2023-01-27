def calculator():
    # Loop infinito para continuar calculando
    while True:
        # Obtenha a operação desejada do usuário
        operation = input("Digite a operação desejada (+, -, *, /): ")
        if operation not in ["+", "-", "*", "/"]:
            print("Operação inválida. Por favor, tente novamente.")
            continue
        # Obtenha os números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realize a operação desejada
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2

        # Mostre o resultado
        print("Resultado:", result)

        # Pergunte se o usuário deseja continuar
        cont = input("Deseja continuar (s/n)? ")
        if cont.lower() != "s":
            break

#Chamada da função
calculator()
