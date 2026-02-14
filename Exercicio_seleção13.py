valor = float(input("Digite o valor da compra: "))

if valor >= 200:
    print("Frete grátis")
elif valor >= 100:
    print("Frete custa R$ 15")
else:
    print("Frete custa R$ 30")
