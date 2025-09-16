
while True:
    print("\n=== MENU ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Par ou Ímpar")
    print("6 - Número Primo")
    print("7 - Fatorial")
    print("SAIR - Encerrar o programa")

    opcao = input("Escolha uma opção: ").upper()

    if opcao == "SAIR":
        print("Programa encerrado.")
        break

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", n1 + n2)
    elif opcao == "2":
        print("Resultado:", n1 - n2)
    elif opcao == "3":
        print("Resultado:", n1 * n2)
    elif opcao == "4":
        if n2 == 0:
            print("Não pode dividir por zero!")
        else:
            print("Resultado:", n1 / n2)
    elif opcao == "5":
        if n1 % 2 == 0:
            print(n1, "é Par")
        else:
            print(n1, "é Ímpar")
        if n2 % 2 == 0:
            print(n2, "é Par")
        else:
            print(n2, "é Ímpar")
    elif opcao == "6":
        for num in [n1, n2]:
            if num < 2:
                print(num, "não é primo")
            else:
                primo = True
                for i in range(2, num):
                    if num % i == 0:
                        primo = False
                        break
                if primo:
                    print(num, "é primo")
                else:
                    print(num, "não é primo")
    elif opcao == "7":
        for num in [n1, n2]:
            fat = 1
            for i in range(1, num+1):
                fat *= i
            print("Fatorial de", num, "é", fat)
    else:
        print("Opção inválida.")