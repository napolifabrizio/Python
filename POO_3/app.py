from models.Restaurante import Restaurante

restaurante_vingadores = Restaurante("Vingadores", "Pizza")
restaurante_justica = Restaurante("justica", "Pizza")

restaurante_justica.alternar_estado()

Restaurante.listar_restaurantes()
print(restaurante_justica.ativo)