area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))#usuario entra com o tamanho da area
litros-necessarios = (area / 6) * 1.1 #calcula os litros necessarios + 10% de folga
print(f'{litros_necessarios:.2f}')
latas_18 = int(litros_necessarios // 18) + (1 if litros_necessarios % 18 > 0 else 0)#latas
custo_latas_18 = latas_18 * 80
 
galoes_36 = int(litros_necessarios // 3.6) + (1 if litros_necessarios % 3.6 > 0 else 0)#galoes
custo_galoes_36 = galoes_36 * 25
 
latas_mistas = int(litros_necessarios // 18) #latas e galoes
resto_tinta = litros_necessarios - (latas_mistas * 18)
galoes_mistos = int(resto_tinta // 3.6) + (1 if resto_tinta % 3.6 > 0 else 0)
custo_misto = (latas_mistas * 80) + (galoes_mistos * 25)# custo total misturado
#  Resultados #
print(f"Para pintar uma área de {area:.2f} m², você precisará de:")
print("\nOpção 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas: {latas_18}")
print(f"Custo total: R$ {custo_latas_18:.2f}")
 
print("\nOpção 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões: {galoes_36}")
print(f"Custo total: R$ {custo_galoes_36:.2f}")
 
print("\nOpção 3: Misturar latas e galões")
print(f"Quantidade de latas: {latas_mistas}")
print(f"Quantidade de galões: {galoes_mistos}")
print(f"Custo total: R$ {custo_misto:.2f}")