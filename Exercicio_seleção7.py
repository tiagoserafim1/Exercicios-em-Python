saldo = 1000
saque = float(input("Digite o valor que deseja sacar: "))

if saque <= 0:
    print("Valor inválido.")
elif saque > saldo:
    print("Saldo insuficiente.")
else:
    saldo -= saque
    print("Saque realizado com sucesso.")
    print("Saldo atual:", saldo)
