idade_do_atleta = int(input("Qual a idade do atleta?"))

if idade_do_atleta <= 9:
    print("Aluno MIRIM")
elif idade_do_atleta <=14:
    print("Aluno INFANTIL")
elif idade_do_atleta <= 19:
    print("Atleta ADULTO")
elif idade_do_atleta <= 25:
    print("Atleta MASTER")
else:
    print("Atleta SENIOR")
