from Avaliacao import Avaliacao

class Restaurante:
    restaurantes  = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo}")

    @property
    def ativo(self):
        return self._ativo

    def alternar_estado(self):
        self._ativo = (not self._ativo)

    def avaliar(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas = len(self._avaliacao)
            media = round((soma_notas / quantidade_notas), 1)
            return media