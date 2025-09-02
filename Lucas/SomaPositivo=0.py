SomaPositivo=0
contNeg=0
for i in range(20):
    valor=int(input("Digite um valor:  "))
    if valor >= 0:
        SomaPositivo=SomaPositivo + valor
    else:
        contNeg=contNeg+1
        print("A soma dos valores positivo é :",SomaPositivo)
        print("a quantidade de valores negativo é :",contNeg)

