### media dos numeros digitados pelo usuario!!!
quantidade=0
soma=0
num=int(input("Digite um número: "))
while num != 0:
    soma+=num
    quantidade += 1
    num=int(input("Digite um número: "))
    print("Valor atual da soma: ",soma,"qtde: ",quantidade)
media=soma/quantidade
print("%.2f"%media)