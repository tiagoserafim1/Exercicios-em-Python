#####10#####
num1=int(input("digite um numero--> "))
num2=int(input("digite outro numero--> "))
while num2<num1:
	num1=int(input("digite um numero--> "))
	num2=int(input("digite outro numero--> "))
else:
	for i in range(num1,num2,1):
		print(i)

#######12#######
        while 1==1:
    tabuada=int(input("infor a taboada que voce deseja ver--> "))
    numero=tabuada
    contador=0
    while (contador<=9):
        contador=contador+1
        print(numero,"*",contador,"=",tabuada)
        tabuada=tabuada+numero