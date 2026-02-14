velocidade = int(input("Digite a velocidade do carro: "))

if velocidade <= 80:
    print("Dentro do limite.")
elif velocidade <= 100:
    print("Multa leve.")
elif velocidade <= 120:
    print("Multa grave.")
else:
    print("Multa gravíssima + suspensão da carteira.")
