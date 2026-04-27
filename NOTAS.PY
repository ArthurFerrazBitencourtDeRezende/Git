n1=float(input("Digite a N1: "))
n2=float(input("Digite a N2: "))
n3=float(input("Digite a N3: "))
n4=float(input("Digite a N4: "))

media=(n1+n2+n3+n4) / 4

if media >= 5:
    print(f"MÉDIA: {media} ->>> Aprovado")
elif media < 6 and media >= 4.0:
    print(f"MÉDIA: {media} ->>> Exame")
else:
    print(f"MÉDIA: {media} ->>> Reprovado")
