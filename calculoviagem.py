distancia=float(input("Distância: "))
consumo=float(input("Consumo do carro: "))
combustivel=float(input("Preço do combustível: "))
litros=distancia/consumo
custo=litros*combustivel
print("Litros necessários: %.2f"% litros)
print("Custo total da viagem: %.2f"% custo,"R$")