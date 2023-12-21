from models.Restaurante import Restaurante
from models.cardapio.Bebida import Bebida
from models.cardapio.Prato import Prato

restaurante_vingadores = Restaurante("Vingadores", "Pizza")
bebida_suco = Bebida("Suco de Melancia", 6.0, "Grande")
prato_pao = Prato("Pão", 2.0, "Pão Francês")

restaurante_vingadores.add_no_cardapio(bebida_suco)
restaurante_vingadores.add_no_cardapio(prato_pao)

bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

restaurante_vingadores.exibir_cardapio