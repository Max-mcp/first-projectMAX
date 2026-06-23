import random

velocidade = random.randint(0, 150)

print(f"Velocidade gerada: {velocidade} km/h")

if velocidade > 80:
    print("Você foi multado por excesso de velocidade!")
else:
    print("Boa viagem, dirija com segurança!")
