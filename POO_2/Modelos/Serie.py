from Modelos.Programa import Programa

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} | Ano: {self.ano} | {self.likes} Likes | {self.temporadas} Temporadas" 