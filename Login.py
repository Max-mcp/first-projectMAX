user= str(input("insira seu nome de usúario:"))
password= int(input("insira sua senha:"))

USER = "Admin"
SENHA = 9988
if user != USER and password != SENHA:
    print("Acesso negado!Verifique suas credenciais ")
else:
    print("Bem-vindo ADMIN ")