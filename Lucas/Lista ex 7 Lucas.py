thanos=float(input("Digite a altura do thanos"))
miranha=float(input("Digite a altura do miranha : "))
for i in range(999):
    if miranha>thanos:
        break
    thanos += 0.2
    miranha += 0.3
    print("O miranha vai ser maior que o thanos em",i, "anos")
    