cor = input("Digite a cor do sinal (verde, amarelo, vermelho): ")

if cor == "verde":
    print("Pode passar.")
elif cor == "amarelo":
    print("Atenção.")
elif cor == "vermelho":
    print("Pare.")
else:
    print("Cor inválida.")
