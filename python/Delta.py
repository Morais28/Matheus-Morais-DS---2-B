# Entrada dos coeficientes
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Cálculo de delta
delta = b**2 - 4*a*c

# Saída do valor de delta
print("valor de Delta:", delta)

# Verificação das raízes
if delta > 0:
    print("A equação tem duas raízes reais")
elif delta == 0:
    print("A equação tem uma raiz real")
else:
    print("A equação não possuí raízes reais")
