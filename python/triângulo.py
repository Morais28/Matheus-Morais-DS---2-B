# Entrada de dados
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

# Cálculo da área
area = (base * altura) / 2

# Classificação
if area > 100:
    print("Triângulo grande")
elif 50 <= area <= 100:
    print("Triângulo médio")
else:
    print("Triângulo pequeno")
