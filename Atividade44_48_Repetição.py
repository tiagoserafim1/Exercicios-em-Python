###44###
print("Candidatos: \n1 - José\n2 - João\n3 - Maria\n4 - Clara")
print("Digite 0 para sair, 5 para votar nulo ou 6 para votar em branco.")
votos = 0
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
nulos = 0
brancos = 0
while True:
    voto = int(input(f"Digite o voto numero {votos + 1}: "))
    if voto == 0:
        break
    votos += 1
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto inválido!")
        votos -= 1

print(
    "\nResultado da eleição:"
    f"\nJosé teve {candidato_1} votos"
    f"\nJoão teve {candidato_2} votos"
    f"\nMaria teve {candidato_3} votos"
    f"\nClara teve {candidato_4} votos"
    f"\n{nulos} votos foram anulados, um total de {100 * nulos / votos:.2f}%"
    f"\n{brancos} votos foram em branco, "
    f"um total de {100 * brancos / votos:.2f}%"
)
###48###
numero = input("Digite um inteiro positivo: ")
numero = numero[::-1]
print(f"=> {numero}")
