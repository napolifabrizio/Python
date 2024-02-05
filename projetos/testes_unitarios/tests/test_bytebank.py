from source.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000"
        esperado = 24

        funcionario_teste = Funcionario("Teste", entrada, 1111)

        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Gold_Roger_deve_retornar_Roger(self):
        entrada = "Gold Roger"
        esperado = "Roger"

        gold = Funcionario(entrada, "11/11/1900", 100000000000)
        resultado = gold.sobrenome()

        assert resultado == esperado