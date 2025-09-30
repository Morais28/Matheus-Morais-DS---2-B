# Solicita a temperatura ao usuário
temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

# Classifica a sensação térmica com base na temperatura
if temperatura > 30:
    print("Sensação Térmica: Está muito quente!!!")
elif temperatura >= 15:
    print("Sensação Térmica: Temperatura agradável.")
else:
    print("Sensação Térmica: Está frio!")
