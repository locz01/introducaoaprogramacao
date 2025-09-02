a=0
neg=0
sompostv=0
while a<20:
    valor=int(input("Digite um número: "))
    if valor >=0:
        sompostv+=valor
    else:
        neg+=1

    a+=1
print("A soma dos números positivos é:", sompostv)
print("A quantidade de números negativos é: ",neg)

        
        
