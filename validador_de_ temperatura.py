ano_de_nascimento= int(input("qual seu ano de nascimento?"))

idade= 2026 - ano_de_nascimento

if idade >= 16:
    print("conteúdo liberado!")
else:
    print("Conteúdo não recomendado para menores de 16 anos")