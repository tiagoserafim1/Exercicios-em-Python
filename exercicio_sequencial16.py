area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
ltnc = area / 3  
latnc = int(ltnc / 18 + 0.9999)  
ct = latnc * 80 
print(f"Para pintar uma área de {area:.2f} m², você precisará de:")
print(f"Quantidade de latas: {latnc}")
print(f"Custo total: R$ {ct:.2f}")