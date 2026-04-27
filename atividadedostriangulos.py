lado1=float(input("Digite o primeiro lado: "))
lado2=float(input("Digite o segundo lado: "))
lado3=float(input("Digite o terceiro lado: "))

if lado1+lado2>lado3 and lado1+lado3 and lado2+lado3>lado1:
    print("É um triângulo!!!")
    if lado1==lado2 and lado2==lado3:
        print("Equilátero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("Isósceles")
elif lado1!=lado2 and lado1!=lado3 and lado2!=lado3:
        print("Escaleno")
else:
    print("Não é um triângulo")