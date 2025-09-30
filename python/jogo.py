class jogo:
    nome = ""
    genero = ""
    jogadores = 0

    def iniciar(self):
        print("iniciando:", self.nome)
    def jogar(self):
        print("jogando", self.nome, "com", self.jogadores, "jogadores")

j1 = jogo()
j1.nome = "Minecraft"
j1.genero = "Sandbox"
j1.jogadores = 30

print("Jogo: ", j1.nome, "-", j1.genero)
j1.iniciar()
j1.jogar()


j2 = jogo()
j2.nome = "Hollow Knight"
j2.genero = "Metroidvania"
j2.jogadores = 1

print("Jogo: ", j2.nome, "-", j2.genero)
j2.iniciar()
j2.jogar()
