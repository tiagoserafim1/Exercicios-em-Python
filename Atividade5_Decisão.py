valor = float(input("Digite o valor da compra: "))

if valor >= 100:
    desconto = valor * 0.10
    total = valor - desconto
    print("Você ganhou 10% de desconto!")
else:
    total = valor
    print("Sem desconto.")

print("Total a pagar: ", total)
