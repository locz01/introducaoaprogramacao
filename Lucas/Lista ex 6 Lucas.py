menormed=10
maiorméd=0
qntdaprov=0
qntdreprov=0
for i in range(10):
    nota1=float(input("Digite a nota 1:  "))
    nota2=float(input("Digite a   nota 2:  "))
    nota3=float(input("Digite a  nota 3:  "))
    media=(nota1+nota2+nota3)/3
if media>maiorméd:
    maiorméd=media

if media<menormed:
    menormed=media

    if media>=6:
        qntdaprov+=1
    else:
        qntdreprov+=1
print("A maior média é :",maiorméd)
print("A menor média é :",menormed)
print("A quantidade de aprovados é :",qntdaprov)
print("A quantidade de reprovados é :",qntdreprov)
