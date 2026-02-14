idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você não pode votar.")
elif idade >= 16 and idade < 18:
    print("Seu voto é opcional.")
elif idade >= 18 and idade < 70:
    print("Seu voto é obrigatório.")
else:
    print("Seu voto é opcional.")
