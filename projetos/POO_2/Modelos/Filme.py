from Modelos.Programa import Programa

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} | Ano: {self.ano} | {self.likes} Likes | {self.duracao} minutos" 