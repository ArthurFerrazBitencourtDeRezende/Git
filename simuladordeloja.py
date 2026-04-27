produto1=float(input("Produto 1:"))
produto2=float(input("Produto 2:"))
produto3=float(input("Produto 3:"))
produto4=float(input("Produto 4:"))
produto5=float(input("Produto 5:"))
total= produto1+produto2+produto3+produto4+produto5
print("Total:", total)
forma=input("Pagamento:")
if forma=="avista":
    print(total-total*0.10)
elif forma=="cartão":
    print(total-total*0.05)
else:
    print(total)




