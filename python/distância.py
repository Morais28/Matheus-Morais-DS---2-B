# Entrada de dados
distancia = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))

# Processamento
velocidade = distancia / tempo

# Saída
print(f"Velocidade média: {velocidade:.2f} km/h")

if velocidade > 100:
    print("Trânsito livre")
elif velocidade >= 60:
    print("Trânsito moderado")
else:
    print("Trânsito lento")
