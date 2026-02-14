peso = float(input("Digite o peso dos peixes em quilos: "))
limite = 50
if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00  
    print("Multa a ser paga: R$", multa)
else:
    print("O peso dos peixes está dentro do limite permitido.")