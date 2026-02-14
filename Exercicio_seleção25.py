usuario_correto = "admin"
senha_correta = "1234"

tentativas = 3

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    tentativas -= 1
    print("Login incorreto. Tentativas restantes:", tentativas)

    if tentativas == 0:
        print("Conta bloqueada.")
