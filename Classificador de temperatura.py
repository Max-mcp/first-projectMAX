 # Temperatura das cidades!


temperatura= float(input("Qual a temperatura está na sua cidade?"))

if temperatura < 15:
    print("Clima frio, AGASALHE-SE!")

elif temperatura >=15 and temperatura <= 25:
    print("Clima agradável!")

else:
    print("Clima muito quente, se hidrate!")