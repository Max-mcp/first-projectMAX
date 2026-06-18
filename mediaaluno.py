nota1=float(input("digiter sua primeira nota:"))
nota2=float(input("digite sua segunda nota:"))
nota3=float(input("digite sua terceira nota"))

media= nota1 + nota2 + nota3 / 3

if media >= 7 :
    print(f"Aluno aprovado com media: {media: .2f}")
elif media >=3 and media < 7 :
    print(f"Aluno (a) em recuperação com média :{media: .2f}")
    fez_recuperacao = input("Aluno já fez a recuperação? s/n")
    if fez_recuperacao == "s":
        nota_de_recuperacao = float(input("digite a nota de recuperação:"))
        if nota_de_recuperacao >=5:
            print("Aluno aprovado pela recuperação")
        else:
            print("Aluno não obteve nota suficiente para ser aprovado após a recuperação")
    else:
        print("Aluno continua de Recuperação")
else:
    print(f"Aluno reprovado com média {media: .2f}")


    

