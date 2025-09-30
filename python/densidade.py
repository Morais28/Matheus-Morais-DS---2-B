massa = float(input("Digite a massa: "))
volume = float(input("Digite o volume: "))

densidade = massa / volume

if densidade > 5:
    print("Material muito denso")
elif 2 <= densidade <= 5:
    print("Material com densidade média")
else:
    print("Material com pouca densidade")
