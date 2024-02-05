from models.Avaliacao import Avaliacao
from models.cardapio.Item_cardapio import ItemCardapio

class Restaurante:
    restaurantes  = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo} | {restaurante.media_avaliacoes}')

    @property
    def ativo(self):
        return self._ativo

    def alternar_estado(self):
        self._ativo = (not self._ativo)

    def avaliar(self, cliente, nota):
        if nota > 5:
            nota = 5
        elif nota < 1:
            nota = 1
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas = len(self._avaliacao)
            media = round((soma_notas / quantidade_notas), 1)
            return media

    def add_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio | {self._nome}')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                print(f'{i}: {item} - {item.descricao} - R${item._preco}')
            else:
                print(f'{i}: {item} - {item._tamanho} mL - R${item._preco}')

