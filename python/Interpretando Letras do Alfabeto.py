# Programa: Interpretação de letras do alfabeto

# Entrada do usuário
letra = input("Digite uma letra do alfabeto: ").lower()

# Verificação se é apenas uma letra
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma única letra.")
else:
    # Verificando se é vogal ou consoante
    if letra in "aeiou":
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")
