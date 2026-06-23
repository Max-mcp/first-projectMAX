valor_da_compra=float(input("Iremos analisar seus DESCONTOS, Insira o valor da sua compra:"))

if valor_da_compra  <= 100 :
    print("compra sem descontos")
    1500
elif valor_da_compra <=300:

    desconto = valor_da_compra * 0.05

    print ("Você possuí 5% de desconto")

elif valor_da_compra <= 500:

    desconto = valor_da_compra * 0.1

    print("Você possuí 10% de desconto")
else:
   desconto = valor_da_compra * 0.15

print("Parábens você adiquiriu 15% de desconto na sua compra")

total = valor_da_compra - desconto

print ("\nConfira sua compra com desconto:")
print(f"\nValor original da compre: R$ {valor_da_compra: .2f}")
print(f"\nvalor do desconto aplicado : R$ {desconto: .2f}")
print(f"\nvalor total com descontos : R${total: .2f}")

finalizacao=input("vamos finalizar suas compras com esse desconto imperdivel? ")

if finalizacao == "sim":
    print("perfeito! Em breve encaminharemos sua compras no conforto da sua casa.")
else:
    print("Que pena! :(, se mudar de ideia seu cupom é valido por 50 minutos")