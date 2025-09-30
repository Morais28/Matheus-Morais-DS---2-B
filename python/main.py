peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura * altura)

print("Seu IMC é ", imc)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obesidade")
