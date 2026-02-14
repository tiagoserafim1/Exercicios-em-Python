idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))

if idade >= 18 and renda >= 2000:
    print("Crédito aprovado.")
elif idade < 18:
    print("Menor de idade. Crédito negado.")
else:
    print("Renda insuficiente.")
