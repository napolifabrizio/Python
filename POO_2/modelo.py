
class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def dar_likes(self, quantidade):
        for i in range(quantidade):
            self._likes += 1

    def __str__(self):
        pass

###############################################################################
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} | Ano: {self.ano} | {self.likes} Likes | {self.duracao} minutos" 

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} | Ano: {self.ano} | {self.likes} Likes | {self.temporadas} Temporadas" 

class Playlist(list):

    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)
        
###############################################################################

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
tmep = Filme("todo mundo em pânico", 1999, 100)
suits = Serie("Suits", 2009, 9)
loki = Serie("Loki", 2022, 2)

vingadores.dar_likes(1000)
suits.dar_likes(250)
loki.dar_likes(200)
tmep.dar_likes(100)



filmes_e_series = [vingadores, suits, loki, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

for programa in filmes_e_series:
    print(programa)

