salario_bruto = float(input("Qual seu sálario bruto?"))

parcelas = float(input("quantas parcelas você deseja?"))

limite = salario_bruto * 0.30

if parcelas <= limite:
    print("Crédito aprovado")
else:
    print("crédito não aprovado")