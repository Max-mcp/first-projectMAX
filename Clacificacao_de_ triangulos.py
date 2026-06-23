reta_a = float(input("digite a 1° medida"))

reta_b = float(input("digite a 2° medida"))

reta_c = float(input("digite a 3° medida"))

if reta_a + reta_b > reta_c and reta_c + reta_b > reta_a and reta_a + reta_c > reta_c:
    if reta_c == reta_a == reta_b:
        print("este é um triangulo  EQUILATERO")
    elif reta_a == reta_b or reta_c == reta_b or reta_c == reta_a :
        print("este é um triangulo ISÓSCELES")

    else:
        print("este é um triangulo ESCALENO ")
else:
    print("Essas médidas não formam um triangulo")