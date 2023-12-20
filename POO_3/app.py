from models.Restaurante import Restaurante

restaurante_vingadores = Restaurante("Vingadores", "Pizza")
restaurante_justica = Restaurante("justica", "Pizza")

restaurante_justica.avaliar("Fafa", 5)
restaurante_justica.avaliar("Fafa", 9)
restaurante_vingadores.avaliar("Fafa", 10)
restaurante_vingadores.avaliar("Fafa", 4)

Restaurante.listar_restaurantes()