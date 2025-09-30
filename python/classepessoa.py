class Pessoa:
    nome = ""
    idade = 18

    def mostrarSituacao(self):
        if self.idade>= 18:
            print(self.nome, "Maior de idade")
        else:
            print(self.nome, "Menor de idade")

a1 =  Pessoa()
a1.nome = "Diego"
a1.idade = 18

a1.mostrarSituacao()

a2 =  Pessoa()
a2.nome = "Matheus Aliaga"
a2.idade = 16

a2.mostrarSituacao()

a3 =  Pessoa()
a3.nome = "Leandro"
a3.idade = 17

a3.mostrarSituacao()

a4 =  Pessoa()
a4.nome = "Yamil"
a4.idade = 16

a4.mostrarSituacao()

a5 =  Pessoa()
a5.nome = "Luan"
a5.idade = 16

a5.mostrarSituacao()

a6 =  Pessoa()
a6.nome = "Phellipe"
a6.idade = 16

a6.mostrarSituacao()

a7 =  Pessoa()
a7.nome = "Caua"
a7.idade = 17

a7.mostrarSituacao()

a8 =  Pessoa()
a8.nome = "Jhonathan"
a8.idade = 16

a8.mostrarSituacao()

a9 = Pessoa()
a9.nome = "Pizzo"
a9.idade = 16

a9.mostrarSituacao()

a10 =  Pessoa()
a10.nome = "Rodrigo"
a10.idade = 16

a10.mostrarSituacao()
