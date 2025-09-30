# Entrada
salario = float(input("Digite seu salario: "))

# Processamento
essenciais = salario * 0.50
prioridades = salario * 0.15
estilo = salario * 0.35

# Saída
print(f"Essenciais: R$ {essenciais: .2f}")
print(f"Prioridades: R$ {prioridades: .2f}")
print(f"Estilo: R$ {estilo: .2f}")
