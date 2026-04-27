produto1=float(input("Produto 1: "))
produto2=float(input("Produto 2: "))
produto3=float(input("Produto 3: "))
produto4=float(input("Produto 4: "))
produto5=float(input("Produto 5: "))
total= produto1+produto2+produto3+produto4+produto5
desconto_avista=total*0.10
final_avista=total-desconto_avista
desconto_cartao=total*0.05
final_cartao=total-desconto_cartao
desconto_parcelado=0
final_parecelado=total
print("\nTotal:", total)
print("\nà vista:")
print("Desconto", desconto_avista)
print("final:",final_avista)
print("\nCartão:")
print("Desconto:",desconto_cartao)
print("Final:",final_cartao)
print("\nParcelado:")
print("Desconto:",desconto_parcelado)
print("Final:",final_parecelado)
