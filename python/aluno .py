class Aluno:
    nome = ""
    nota = 0

    def mostrarSituacao(self):
        if self.nota>= 5:
            print(self.nome, "Foi aprovado")
        else:
            print(self.nome, "Foi reprovado")

a1 = Aluno()
a1.nome = "Diego"
a1.nota = 3

a1.mostrarSituacao()

a2 = Aluno()
a2.nome = "Rodrigo"
a2.nota = 10

a2.mostrarSituacao()

a3 = Aluno()
a3.nome = "Jonatha"
a3.nota = 5

a3.mostrarSituacao()

a4 = Aluno()
a4.nome = "Gabriel"
a4.nota = 7

a4.mostrarSituacao()

a5 = Aluno()
a5.nome = "Yamil"
a5.nota = 2

a5.mostrarSituacao()

a6 = Aluno()
a6.nome = "Luan"
a6.nota = 5

a6.mostrarSituacao()

a7 = Aluno()
a7.nome = "Lucca"
a7.nota = 10

a7.mostrarSituacao()
