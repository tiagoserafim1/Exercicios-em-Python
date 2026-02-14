vendas = float(input("Digite o valor das vendas do mês: "))

if vendas >= 10000:
    bonus = vendas * 0.10
    print("Bônus de 10%:", bonus)
elif vendas >= 5000:
    bonus = vendas * 0.05
    print("Bônus de 5%:", bonus)
else:
    print("Sem bônus este mês.")
