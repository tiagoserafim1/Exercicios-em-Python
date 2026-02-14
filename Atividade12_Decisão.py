print("salario Bruto: ", salario_bruto)

if salario_bruto <= 900:
    print("Seu salario permanecerá o mesmo")
else:
    print("INSS: ", inss, "\nFGTS: ", fgts)

if salario_bruto > 900 and salario_bruto <= 1500:
    salario_liquido = float(salario_bruto) - float(ir1500) - float(inss)
    print("IR: ", ir1500, "\nSalario Liquido: ", salario_liquido)

elif salario_bruto > 1500 and salario_bruto <= 2500:
    salario_liquido = float(salario_bruto) - float(ir2500) - float(inss)
    print("IR: ", ir2500, "\nSalario Liquido: ", salario_liquido)

else:
    salario_liquido = float(salario_bruto) - float(irmaior) - float(inss)
    print("IR: ", iralto, "\nSalario Liquido: ", salario_liquido)