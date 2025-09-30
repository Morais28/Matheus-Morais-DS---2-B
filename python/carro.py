# def cria funções (ou métodos dentro da classe)
class Carro:
    marca = ""
    modelo = ""
    ano = 0
    cor = ""

    def buzinar(self):
        print(" Bi-Bi")

    def ligar(self):
        print("PHAM PHAM BRRRRRRRRRRRR")

        # acelerar
    def acelerar(self):
        print("VRUUUUUUUUUUMMMMMMM")

        # freiar
    def freiar(self):
        print("FIIIUUUUUUUUUUU")

        # desligar
    def desligar(self):
        print("IIIIIIIIIIIHHHHH")

c1 = Carro()
c1.marca = "Nissan"
c1.modelo = "Nissan GT3"
c1.ano = 2006
c1.cor = "Verde de Ben10"

print("Carro: ", c1.marca, "-", c1.modelo, "Ano: ", c1.ano, "Cor: ", c1.cor)
c1.ligar()
c1.buzinar()
c1.acelerar()
c1.freiar()
c1.desligar()