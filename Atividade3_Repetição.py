nome=str(input("informe um nome--> "))
while ( len(nome) <=  3 ):
	nome=str(input("informe um nome--> "))
idade=int(input("informe a idade--> "))
while ( idade > 150 or idade < 0 ):
	idade=int(input("informe a idade--> "))
salario=float(input("informe um sal�rio--> "))
while ( salario < 0 ):
	salario=float(input("informe um sal�rio--> "))
sexo=str(input("informe a inicial do seu sexo--> "))
while  sexo !="f" and sexo!="m" :
	sexo=str(input("informe a inicial do seu sexo--> "))
estado_civil=str(input("informe a inicial do seu estado civil-->"))
while ( estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" ):
	estado_civil=str(input("informe a inicial do seu estado civil-->"))