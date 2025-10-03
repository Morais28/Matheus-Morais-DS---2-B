ip = input("Digite um IP: ")

if ip.startswith("192.168."):
    print ("Rede privada (Classe C)")
elif ip.startswith("10."):
    print ("Rede privada (Classe A)")
elif ip.startswith("172.16."):
    print ("Rede privada (Classe B)")
else:
    print("Rede pública")